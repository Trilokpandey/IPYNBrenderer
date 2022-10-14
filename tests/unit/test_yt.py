import pytest
from IPYNBrenderer import get_time_info
from IPYNBrenderer.custom_exception import InvalidURLException

good_url_data = [
    ("https://youtu.be/P4wWU2MEQLw",0),
    ("https://www.youtube.com/watch?v=P4wWU2MEQLw",0),
    ("https://www.youtube.com/watch?v=P4wWU2MEQLw&t=60s",60),
]

URL_id_bad_data = [
    ("https://www.youtube.com/watch?v=P4wWU2MEQLwabcd"),
    ("https://www.youtube.com/watch?v=P4wWU2MEQLw&t"),
    ("https://www.youtube.com/watch?v==P4wWU2MEQLw==60s"),
    ("https://www.youtube.com/watch?v=P4wWU2MEQLw&t==60s")
]

@pytest.mark.parametrize("URL,response",good_url_data)
def test_get_time_info(URL,response):
    assert get_time_info(URL)==response

@pytest.mark.parametrize("URL", URL_id_bad_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)
    