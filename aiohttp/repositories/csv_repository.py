async def get(self, **kwargs) -> dict | None:
    for row in self._get_all():
        if self._compare_kwargs(row, **kwargs):
            return row

    return None


async def create(self, **kwargs) -> dict: ...


async def update(self, **kwargs) -> dict: ...


async def delete(self, **kwargs) -> dict: ...


async def filter(self, **kwargs) -> [dict]:
    res = []
    for row in self.data:
        for key, value in kwargs.items():
            if row.get(key) != value:
                matches = False
                break  # Exit the loop if any condition fails
        if matches: res.append(row)
    return res
