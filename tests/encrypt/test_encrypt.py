from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(123, "xablau")
        encrypt_message("xablau", 123)

    assert encrypt_message("message", 10) == "egassem"
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("message", 2) == "egass_em"
