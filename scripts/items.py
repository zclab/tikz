
from pathlib import Path


class TomlData:

    template = """
    [[items]]
    title = ""
    image = ""
    thumb = ""
    alt = ""
    description = ""
    url = ""
    """

    def __init__(self, src_dir, out_dir) -> None:
        self._src_dir = src_dir
        self._out_dir = out_dir

    @property
    def src_dir(self):
        return self._src_dir

    @property
    def out_dir(self):
        return self._out_dir
