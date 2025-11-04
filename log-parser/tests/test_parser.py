import json
from pathlib import Path
from parser import parser
from pytest_mock import MockerFixture


def test_success_parser(tmp_path: Path):
    log_file = tmp_path / "server.log"
    log_file.write_text(
        "2025-11-04 10:00:00 - [INFO] - Server started\n"
        "2025-11-04 10:05:00 - [ERROR] - Connection lost\n"
        "2025-11-04 10:10:00 - [INFO] - Server recovered\n"
    )

    parser(str(log_file))

    result = Path("data/result.json")
    assert result.exists()

    data = json.loads(result.read_text())
    assert data["summary"]["INFO"] == 2
    assert data["summary"]["ERROR"] == 1


def test_failed_success(mocker: MockerFixture):
    mocker_error = mocker.patch("parser.logger.error")
    parser("nonexistent.log")
    mocker_error.assert_called()
    called_msg = mocker_error.call_args[0][0]
    assert "File Not Found Error" in called_msg
