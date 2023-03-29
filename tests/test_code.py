import pytest
from main import Loader


@pytest.fixture()
def loader():
    return Loader()


@pytest.mark.parametrize("file_1, file_2, expected_result", [({"line_1", "line_2"}, {"line_1"}, {"line_1"}),
                                                             ({"line_1", "line_2"}, {"line_2"}, {"line_2"}),
                                                             ({"line_1", "line_2"}, {"line_1", "line_2"},
                                                              {"line_1", "line_2"})])
def test_same_lines(loader, file_1, file_2, expected_result):
    result = loader.write_same_lines(file_1, file_2)
    assert result == expected_result


@pytest.mark.parametrize("file_1, file_2, expected_result", [({"line_1", "line_2"}, {"line_1", "line_3"}, {"line_2",
                                                                                                           "line_3"}),
                                                             ({"line_1", "line_3"}, {"line_2"}, {"line_1", "line_2",
                                                                                                 "line_3"}),
                                                             ({"line_1"}, {"line_3", "line_2", "line_1"}, {"line_2",
                                                                                                           "line_3"})])
def test_diff_lines(loader, file_1, file_2, expected_result):
    result = loader.write_diff_lines(file_1, file_2)
    assert result == expected_result
