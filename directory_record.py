class DirRecord:
    """Holds information about archive directory, and can be serialized as JSON"""

    """
    name
    
    """

    def __init__(self, dir_path: str) -> None:
        self.dir_path: str = dir_path