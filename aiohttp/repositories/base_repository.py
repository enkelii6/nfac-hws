from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    async def get(self, **kwargs) -> dict: ...

    @abstractmethod
    async def create(self, **kwargs) -> dict: ...

    @abstractmethod
    async def update(self, **kwargs) -> dict: ...

    @abstractmethod
    async def delete(self, **kwargs) -> dict: ...

    @abstractmethod
    async def filter(self, **kwargs) -> [dict]: ...

    async def _compare_kwargs(self, data: dict, **kwargs) -> bool:
        for key, value in kwargs.items():
            if data.get(key) != value:
                return False

        return True