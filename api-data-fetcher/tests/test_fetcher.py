from pytest_mock import MockerFixture
from fetcher import fetcher


def test_success_fetcher(mocker: MockerFixture):
    mocker_get_request = mocker.patch("fetcher.requests.get")
    mocker_response = mocker.MagicMock()
    mocker_response.status_code = 200
    mocker_response.reason = "OK"
    mocker_response.ok = True
    mocker_response.json.return_value = {"name": "fetcher"}
    mocker_get_request.return_value = mocker_response

    mocker.patch("fetcher.json.dump")
    mocker.patch("fetcher.csv.DictWriter")

    url = "https://example.com"
    fetcher(url, 5)

    mocker_get_request.assert_called_once_with(url, timeout=5)


def test_failed_fetcher(mocker: MockerFixture):
    mocker_get_request = mocker.patch("fetcher.requests.get")
    mocker_response = mocker.MagicMock()
    mocker_response.status_code = None
    mocker_response.reason = "FAIL"
    mocker_response.ok = False
    mocker_response.json.return_value = {"name": "fetcher"}
    mocker_get_request.return_value = mocker_response

    mocker.patch("fetcher.json.dump")
    mocker.patch("fetcher.csv.DictWriter")

    url = "https://example.com"
    fetcher(url, 5)

    mocker_get_request.assert_called_once_with(url, timeout=5)
