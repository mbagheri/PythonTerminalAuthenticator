import pyotp

"""
OTP class for generating the OTPs
"""

class OTP:

    """
    Method which receives the base32secret as parameter
    and uses the pyotp method to generate a new time-based OTP
    """
    def get_TOTP(self, b32s):
        totp = pyotp.TOTP(b32s)
        return totp.now()