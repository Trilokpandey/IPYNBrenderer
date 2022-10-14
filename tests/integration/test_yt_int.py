import pytest 
from IPYNBrenderer import render_YouTube_video
from IPYNBrenderer.custom_exception import InvalidURLException

class TestYTvideoRenderer:
    URL_test_success_data = [
        ("https://youtu.be/P4wWU2MEQLw", "success"),
        ("https://www.youtube.com/watch?v=P4wWU2MEQLw", "success"),
        ("https://www.youtube.com/watch?v=P4wWU2MEQLw&t=60s", "success"),
    ]
    URL_test_bad_data = [
        ("https://www.youtube.com/watch?v=P4wWU2MEQLwabcd"),
        ("https://www.youtube.com/watch?v=P4wWU2MEQLw00"),
        ("https://www.youtube.com/watch?v=P4wWU2MEQLw__"),
        ("https://www.youtube.com/watch?v=P4wWU2MEQLwpp"),
        ("https://www.youtube.com/watch?v=P4wWU2MEQLw2s&t"),
        ("https://www.youtube.com/watch?v=P4wWU2MEQLw2s&t==60s"),
        ("https://www.youtube.com/watch?v==P4wWU2MEQLw2s&t=60s"),
    ]

    @pytest.mark.parametrize("URL, response", URL_test_success_data)
    def test_render_YT_success(self, URL, response):
        assert render_YouTube_video(URL) == response

    @pytest.mark.parametrize("URL", URL_test_bad_data)
    def test_render_YT_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_YouTube_video(URL)