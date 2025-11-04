import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.checker import checker
from pytest_mock import MockerFixture


def test_success_checker(mocker: MockerFixture):
    mocker_get_request = mocker.patch("src.checker.requests.get")

    mocker_res = mocker.MagicMock()
    mocker_res.status_code = 200
    mocker_res.reason = "OK"
    mocker_res.ok = True

    mocker_get_request.return_value = mocker_res
    mocker.patch("src.checker.storage_to_json_csv")

    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://httpstat.us/404",
        "https://httpstat.us/500",
        "https://www.nonexistent12345.com",
        "https://10.255.255.1",
        "invalid-url",
    ]

    result = checker(urls, 5)

    assert mocker_get_request.call_count == len(urls)
    assert result[0]["status_code"] == 200
    assert result[0]["is_up"] == True


# test the failed case in the checker
def test_failed_checker(mocker: MockerFixture):
    mocker_get_request = mocker.patch("src.checker.requests.get")

    mocker_res = mocker.MagicMock()
    mocker_res.status_code = None
    mocker_res.reason = "FAIL"
    mocker_res.ok = False

    mocker_get_request.return_value = mocker_res
    mocker.patch("src.checker.storage_to_json_csv")

    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://httpstat.us/404",
        "https://httpstat.us/500",
        "https://www.nonexistent12345.com",
        "https://10.255.255.1",
        "invalid-url",
    ]

    result = checker(urls, 5)

    assert mocker_get_request.call_count == len(urls)
    assert result[0]["status_code"] is None
    assert result[0]["is_up"] is False
