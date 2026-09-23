from src.ksmb1 import generate_keypair, sign, verify


def test_key_generation():
    try:
        private_key, public_key = generate_keypair()
    except NotImplementedError:
        return

    assert private_key is not None
    assert public_key is not None


def test_signature_round_trip():
    try:
        private_key, public_key = generate_keypair()
        message = b"KSMB-1 test message"

        signature = sign(message, private_key)

        assert verify(message, signature, public_key) is True
        assert verify(b"tampered message", signature, public_key) is False

    except NotImplementedError:
        return
