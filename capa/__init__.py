from snake.scale import FileType, scale


NAME = "capa"
VERSION = "1.0"

AUTHOR = "Brandon Carter"
AUTHOR_EMAIL = "bizarrechaos@bizarrechaos.com"

DESCRIPTION = "a module to run capa on binaries"

LICENSE = "https://github.com/bizarrechaos/capa-scale/blob/master/LICENSE"

URL = "https://github.com/bizarrechaos/capa-scale"


__scale__ = scale(
    name=NAME,
    description=DESCRIPTION,
    version=VERSION,
    author=AUTHOR,
    supports=[
        FileType.FILE
    ],
)
