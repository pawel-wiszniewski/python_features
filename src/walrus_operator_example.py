import time
from typing import Any

Record = dict[str, Any]


def main():
    records = retrieve_records()
    print(records)
    assert len(records) == 12


def retrieve_records() -> list[int]:
    param = 0
    all_records = []

    records = send_request(param)

    while len(records) > 0:
        all_records.extend(records)
        param += 1
        records = send_request(param)

    return all_records


def send_request(run_number: int) -> list[int]:
    # this could be a long operation
    # time.sleep(1)
    if run_number <= 3:
        return [value for value in range(3)]
    else:
        return []


if __name__ == "__main__":
    main()
