class Config:
    """Class that holds parameters and settings"""

    MIN_ARGS: int = 2

    def __init__(self, argv: list[str]) -> None:
        self.work_dir: str = argv[1]
