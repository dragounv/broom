import sys

from config import Config
from directory_record import DirRecord


USAGE: str = "python3 main.py [dir_to_analyze]"


def main() -> None:
    if not_enough_args():
        print("error: not enugh commandline arguments", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        sys.exit(1)
    else:
        config = Config(sys.argv)
        run(config)
        sys.exit(0)


def not_enough_args() -> bool:
    return len(sys.argv) < Config.MIN_ARGS

def run(config: Config) -> None:
    root_dir = DirRecord(config.work_dir)

if __name__ == "__main__":
    main()
