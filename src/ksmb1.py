"""
KSMB-1
Experimental cryptographic research implementation.

WARNING:
This implementation is experimental and is NOT suitable
for protecting real funds, private keys, passwords, or
sensitive information.
"""

__version__ = "0.1.0"


def generate_keypair():
    """Generate a KSMB-1 private/public keypair."""
    raise NotImplementedError


def sign(message, private_key):
    """Create a KSMB-1 signature."""
    raise NotImplementedError


def verify(message, signature, public_key):
    """Verify a KSMB-1 signature."""
    raise NotImplementedError
