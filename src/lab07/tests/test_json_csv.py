import pytest

import json
import csv
from src.lib.file_converting import json_to_csv, csv_to_json


@pytest.fixture
def sample_json(tmp_path):
    json_newfile = tmp_path / "people.json"
    text = [
        {"name": "Alice", "age": 25, "city": "Moscow"},
        {"name": "Bob", "age": 30, "city": "Saint Petersburg"},
        {"name": "Marie", "age": 28, "city": "Novosibirsk"},
    ]
    with open(json_newfile, "w", encoding="utf-8") as jf:
        json.dump(text, jf, ensure_ascii=False)
    return json_newfile


@pytest.fixture
def sample_csv(tmp_path):
    csv_newfile = tmp_path / "people.csv"
    text = [
        ["name", "age", "city"],
        ["Alice", "25", "Moscow"],
        ["Bob", "30", "Saint Petersburg"],
        ["Marie", "28", "Novosibirsk"],
    ]
    with open(csv_newfile, "w", encoding="utf-8", newline="") as cf:
        csv_writer = csv.writer(cf)
        csv_writer.writerows(text)
    return csv_newfile


def test_json_to_csv(sample_json, tmp_path):
    csv_file = tmp_path / "people_from_jf.csv"

    json_to_csv(str(sample_json), str(csv_file))
    assert csv_file.exists()

    with open(csv_file, 'r', encoding="utf-8") as cf:
        csv_reader = csv.DictReader(cf)
        rows = list(csv_reader)

        assert len(rows) == 3
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "25"
        assert rows[0]["city"] == "Moscow"


def test_csv_to_json(sample_csv, tmp_path):
    json_file = tmp_path / "people_from_cf.json"

    csv_to_json(str(sample_csv), str(json_file))
    assert json_file.exists()

    with open(json_file, 'r', encoding="utf-8") as jf:
        json_reader = json.load(jf)

        assert len(json_reader) == 3
        assert json_reader[0]["name"] == "Alice"
        assert json_reader[0]["age"] == "25"
        assert json_reader[0]["city"] == "Moscow"
