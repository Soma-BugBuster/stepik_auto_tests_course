def test_list_comparison(expected_result, actual_result):
    assert actual_result == expected_result, f"expected {expected_result}, got {actual_result}"


test_list_comparison(8, 12)
