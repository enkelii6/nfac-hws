import csv
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


class CSVRepository(BaseRepository):
    def __init__(self, path: str):
        with open(path) as file:
            self.csv_reader = csv.DictReader(file)

    async def _get_all(self) -> [dict]:
        data_list = []
        for row in self.csv_reader:
            data_list.append(row)

        return data_list

    async def get(self, **kwargs):
        for row in self._get_all():
            if self._compare_kwargs(row, **kwargs):
                return row

        return None

    async def create(self, **kwargs) -> dict: ...
    async def update(self, **kwargs) -> dict: ...
    async def delete(self, **kwargs) -> dict: ...
    async def filter(self, **kwargs) -> [dict]: ...


class JSONRepository(BaseRepository): ...
