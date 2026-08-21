class UpstoxError(Exception):
    """Base exception for Upstox-related errors."""


class UpstoxAuthenticationError(UpstoxError):
    """Raised when authentication fails."""


class UpstoxBadRequestError(UpstoxError):
    """Raised when the API request is invalid."""


class UpstoxRateLimitError(UpstoxError):
    """Raised when the API rate limit is exceeded."""


class UpstoxServerError(UpstoxError):
    """Raised when the provider returns a server-side error."""