# tasks:
# 1 - replace all imported typing classes with builtin and Union operator
# 2 - refactor retrieve_records using walrus := operator
# 3 - refactor merge_records using union | or |= operator
# 4 - bonus - use type alias for retrieved records

import time
# from typing import List, Dict, Optional
from typing import TypeAlias

# record retrieved from the endpoint
Record: TypeAlias = dict[str, str]

def main():
    records = retrieve_records()
    print(f"Records retrieved: {records}")
    assert len(records) == 4
    merged = merge_records(records)
    print(f"Records merged: {merged}")
    assert len(merged.keys()) == 4


def retrieve_records() -> list[Record]:
    param = 0
    all_records = []

    while (record := send_request(param)) is not None:
        all_records.append(record)
        param += 1

    return all_records


def merge_records(records: list[Record]) -> dict[str, str]:
    merged_record = {}
    for record in records:
        merged_record |= record
    return merged_record


def send_request(run_number: int) -> Record | None:
    # this could be a long operation
    # time.sleep(1)
    if run_number <= 3:
        return {f"key{run_number}": "value"}
    else:
        return None


if __name__ == "__main__":
    main()
