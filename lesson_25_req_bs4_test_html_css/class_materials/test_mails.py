import pytest


@pytest.fixture()
def set_up():
    print('Programm start')
    yield
    print('Programm finish')


def test_sending_first_email(set_up):
    print('message 1 was sending')


def test_sending_second_email(set_up):
    print('message 2 was sending')
