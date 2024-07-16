import sys
import json

from directory_record import DirRecord, DirRecordEncoder


MIN_ARGS: int = 2
USAGE: str = "python3 main.py [dir_to_analyze]"


def main() -> None:
    if not_enough_args():
        print("error: not enugh commandline arguments", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        sys.exit(1)
    else:
        config = {
            "work_dir": sys.argv[1]
        }
        run(config)
        sys.exit(0)


def not_enough_args() -> bool:
    return len(sys.argv) < MIN_ARGS


def run(config: dict) -> None:
    root_record = DirRecord(config["work_dir"])
    root_record.scan()
    sys.stdout.write(DirRecordEncoder().encode(root_record))
    # json.dump(root_record.totals(), sys.stdout)

if __name__ == "__main__":
    main()
