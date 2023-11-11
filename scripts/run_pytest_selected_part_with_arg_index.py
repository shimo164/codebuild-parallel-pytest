import glob
import os
import subprocess
import sys


def get_part_of_splitted_list(list_, split_num, target_index) -> list[str]:
    """
    Splits a list into `split_num` parts and returns the `target_index` part.
    Handles cases where the list is not perfectly divisible by `split_num`.
    """
    part_len = len(list_) // split_num
    extra_items = len(list_) % split_num

    start_index = part_len * (target_index - 1) + min(target_index - 1, extra_items)
    end_index = start_index + part_len + (1 if target_index <= extra_items else 0)

    return list_[start_index:end_index]


def get_target_index() -> int:
    """
    Retrieves the target index from the command line arguments.
    Raises an error if the index is not provided or invalid.
    """
    try:
        return int(sys.argv[1])
    except (IndexError, ValueError):
        raise ValueError(
            "Target index must be a valid integer provided as a command line argument."
        )


def get_split_num() -> int:
    """
    Retrieves the split number from the environment variables.
    Raises an error if the variable is not set or invalid.
    """
    try:
        return int(os.environ["SPLIT_NUM"])
    except KeyError:
        raise KeyError("Environment variable 'SPLIT_NUM' not set.")
    except ValueError:
        raise ValueError("Environment variable 'SPLIT_NUM' must be a valid integer.")


def main():
    try:
        target_index = get_target_index()
        split_num = get_split_num()

        all_test_files = sorted(glob.glob("tests/unit/**/*py", recursive=True))
        files_for_batch = get_part_of_splitted_list(
            all_test_files, split_num, target_index
        )

        subprocess.run(["python", "-m", "pytest"] + files_for_batch)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
