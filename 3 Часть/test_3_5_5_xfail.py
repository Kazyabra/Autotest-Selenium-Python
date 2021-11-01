# запуск из консоли pytest -rx -v test_3_5_5_xfail.py
import pytest


@pytest.mark.xfail(strict=True)  # c этим параметром неожиданно прошедший тест XPASS считается зафейленным
def test_succeed():
    assert True
    # assert False


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False


if __name__ == '__main__':
    pytest.main()

# Ответ 1 failed, 1 skipped, 1 xfailed in 0.10s
