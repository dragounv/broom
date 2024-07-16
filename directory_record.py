import os
import json
from typing import Any


class DirRecord():
    """Holds information about archive directory, and can be serialized as JSON"""

    def __init__(self, path: str) -> None:
        self.path: str = path

        self.directories: list[DirRecord] = []
        self.no_archive_files: int = 0
        self.size_of_archive_files: int = 0
        self.has_open_warcs: bool = False

    def scan(self) -> None:
        with os.scandir(self.path) as dir_iter:
            for entry in dir_iter:
                if entry.is_file() and self._is_archive_file(entry):
                    self.no_archive_files += 1
                    self.size_of_archive_files += entry.stat().st_size
                elif entry.is_dir():
                    dir_record = DirRecord(os.fsdecode(entry.path))
                    self.directories.append(dir_record)
                    dir_record.scan()

    def _is_archive_file(self, entry: os.DirEntry) -> bool:
        name = os.fsdecode(entry.name)
        if name.endswith((".arc", ".arc.gz", ".warc", ".warc.gz")):
            return True
        elif name.endswith((".warc.open", ".warc.gz.open")):
            self.has_open_warcs = True
            return True
        return False

class DirRecordEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, DirRecord):
            return o.__dict__
        return super().default(o)