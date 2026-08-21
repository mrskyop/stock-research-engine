import time
from collections.abc import Callable
from typing import TypeVar


T = TypeVar("T")


def retry(
    func: Callable[[], T],
    retryable_exceptions: tuple[type[Exception], ...],
    max_attempts: int = 3,
    base_delay: float = 2.0,
) -> T:
    """
    Execute a function and retry only when a retryable
    exception is raised.
    """

    for attempt in range(1, max_attempts + 1):
        try:
            return func()

        except retryable_exceptions as error:
            if attempt == max_attempts:
                raise

            delay = base_delay * (2 ** (attempt - 1))

            print(
                f"Attempt {attempt} failed: {error}. "
                f"Retrying in {delay:.1f}s..."
            )

            time.sleep(delay)

    raise RuntimeError(
        "Retry operation ended unexpectedly"
    )