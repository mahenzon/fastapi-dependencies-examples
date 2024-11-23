from typing import Annotated

from fastapi import Header


class BaseGreat:
    name: str
    default: str

    def as_dict(self) -> dict[str, str]:
        return {
            "name": self.name,
            "default": self.default,
        }


class GreatHelper(BaseGreat):
    def __init__(self, name: str, default: str) -> None:
        self.name = name
        self.default = default


class GreatService(BaseGreat):
    def __init__(
        self,
        name: Annotated[
            str,
            Header(alias="x-great-service-name"),
        ],
        default: Annotated[
            str,
            Header(alias="x-great-service-default-value"),
        ],
    ) -> None:
        self.name = name
        self.default = default
