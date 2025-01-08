"""lpGBT control library exception types"""


class LpgbtException(Exception):
    """Generic exception type for all lpGBT related errors"""


class LpgbtTimeoutError(LpgbtException):
    """Timeout exception for various lpGBT components"""


class LpgbtI2CMasterBusError(LpgbtException):
    """I2C master bus fault exception"""


class LpgbtI2CMasterTransactionError(LpgbtException):
    """I2C master exception for transaction failures"""


class LpgbtFuseError(LpgbtException):
    """Fusing process related exception"""
