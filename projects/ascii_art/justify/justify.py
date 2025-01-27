import os
from argparse import ArgumentParser
from enum import Enum, unique


@unique
class AlignTypeEnum(str, Enum):
    RIGHT = 'right'
    LEFT = 'left'
    JUSTIFY = 'justify'


def justify(align_type: AlignTypeEnum, text: str) -> None:
    if align_type == AlignTypeEnum.RIGHT:
        return

    elif align_type == AlignTypeEnum.LEFT:
        return

    elif align_type == AlignTypeEnum.JUSTIFY:
        return

    raise ValueError(f'{align_type} is not a valid alignment type')


def justify_right(text: str) -> None: ...


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('text', type=str)
    parser.add_argument('-a', '--align', type=str)
    args = parser.parse_args()

    justify(args.align, args.text)
