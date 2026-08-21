from app.ingestion.retry import retry
from app.providers.exceptions import UpstoxAuthenticationError, UpstoxServerError


attempts = 0


def authentication_failure():
    global attempts

    attempts += 1

    print(f"Attempting API call: {attempts}")

    raise UpstoxAuthenticationError(
        "Simulated invalid token"
    )


def main():
    try:
        retry(
            authentication_failure,
            retryable_exceptions=(
                UpstoxServerError,
            ),
            max_attempts=3,
            base_delay=0.5,
        )

    except UpstoxAuthenticationError as error:
        print(f"Authentication error: {error}")


if __name__ == "__main__":
    main()