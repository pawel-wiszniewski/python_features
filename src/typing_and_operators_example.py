# tasks:
# 1 - replace all imported typing classes with builtin and Union operator
# 2 - refactor retrieve_records using walrus := operator
# 3 - refactor merge_records using union | or |= operator
# 4 - bonus - use type alias for retrieved records

import time
from typing import List, Dict, Optional


def main():
    records = retrieve_records()
    print(f"Records retrieved: {records}")
    assert len(records) == 4
    merged = merge_records(records)
    print(f"Records merged: {merged}")
    assert len(merged.keys()) == 4


def retrieve_records() -> List[Dict[str, str]]:
    param = 0
    all_records = []

    record = send_request(param)

    while record is not None:
        all_records.append(record)
        param += 1
        record = send_request(param)

    return all_records


def merge_records(records: List[Dict[str, str]]) -> Dict[str, str]:
    merged_record = {}
    for record in records:
        merged_record = {**merged_record, **record}
    return merged_record


def send_request(run_number: int) -> Optional[Dict[str, str]]:
    # this could be a long operation
    # time.sleep(1)
    if run_number <= 3:
        return {f"key{run_number}": "value"}
    else:
        return None


if __name__ == "__main__":
    main()
