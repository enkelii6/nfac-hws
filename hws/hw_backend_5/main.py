from fastapi import FastAPI, Request, Form, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from repository import user_repo, flower_repo, purchase_repo
import os
import uuid

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

sessions = {}


@app.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.post("/signup")
async def signup(
        email: str = Form(...),
        full_name: str = Form(...),
        password: str = Form(...),
        photo: UploadFile = File(None)
):
    if user_repo.get_user_by_email(email):
        raise HTTPException(400, "Email уже занят")

    photo_path = None
    if photo:
        os.makedirs("static/uploads", exist_ok=True)
        filename = f"{uuid.uuid4()}.jpg"
        with open(f"static/uploads/{filename}", "wb") as f:
            f.write(await photo.read())
        photo_path = f"/uploads/{filename}"

    user_repo.create_user(email, full_name, password, photo_path)
    return RedirectResponse("/login", status_code=303)


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    user = user_repo.get_user_by_email(email)
    if not user or user["password"] != password:
        raise HTTPException(401, "Неверный email или пароль")

    session_id = str(uuid.uuid4())
    sessions[session_id] = user["id"]

    response = RedirectResponse("/profile", status_code=303)
    response.set_cookie(key="session_id", value=session_id)
    return response


@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    session_id = request.cookies.get("session_id")
    user_id = sessions.get(session_id) if session_id else None
    user = user_repo.get_user_by_id(user_id) if user_id else None

    if not user:
        return RedirectResponse("/login", status_code=303)

    return templates.TemplateResponse("profile.html", {
        "request": request,
        "user": user,
        "photo_url": user["photo_path"]
    })

@app.get("/flowers", response_class=HTMLResponse)
async def flowers_page(request: Request):
    return templates.TemplateResponse("flowers.html", {
        "request": request,
        "flowers": flower_repo.get_all_flowers()
    })


@app.post("/flowers")
async def add_flower(
        name: str = Form(...),
        count: int = Form(...),
        cost: float = Form(...)
):
    flower_repo.add_flower(name, count, cost)
    return RedirectResponse("/flowers", status_code=303)

@app.post("/cart/items")
async def add_to_cart(
        request: Request,
        flower_id: int = Form(...)
):
    if not flower_repo.get_flower_by_id(flower_id):
        raise HTTPException(404, "Цветок не найден")

    cart = request.cookies.get("cart", "").split(",")
    cart.append(str(flower_id))
    cart_str = ",".join(filter(None, cart))

    response = RedirectResponse("/flowers", status_code=303)
    response.set_cookie(key="cart", value=cart_str)
    return response


@app.get("/cart/items", response_class=HTMLResponse)
async def view_cart(request: Request):
    cart_ids = [int(id) for id in request.cookies.get("cart", "").split(",") if id.isdigit()]
    flowers = []
    total = 0.0

    for fid in cart_ids:
        flower = flower_repo.get_flower_by_id(fid)
        if flower:
            flowers.append(flower)
            total += flower["cost"]

    return templates.TemplateResponse("cart.html", {
        "request": request,
        "flowers": flowers,
        "total": total
    })

@app.post("/purchased")
async def make_purchase(request: Request):
    user_id = sessions.get(request.cookies.get("session_id", ""))
    if not user_id:
        return RedirectResponse("/login", status_code=303)

    cart_ids = [int(id) for id in request.cookies.get("cart", "").split(",") if id.isdigit()]
    for fid in cart_ids:
        purchase_repo.add_purchase(user_id, fid)

    response = RedirectResponse("/purchased", status_code=303)
    response.delete_cookie("cart")
    return response


@app.get("/purchased", response_class=HTMLResponse)
async def view_purchased(request: Request):
    user_id = sessions.get(request.cookies.get("session_id", ""))
    if not user_id:
        return RedirectResponse("/login", status_code=303)

    purchases = purchase_repo.get_user_purchases(user_id)
    flowers = []
    total = 0.0

    for p in purchases:
        flower = flower_repo.get_flower_by_id(p["flower_id"])
        if flower:
            flowers.append(flower)
            total += flower["cost"]

    return templates.TemplateResponse("purchased.html", {
        "request": request,
        "flowers": flowers,
        "total": total
    })