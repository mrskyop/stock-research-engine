from app.ingestion.retry import retry
from app.providers.exceptions import UpstoxServerError


attempts = 0


def unreliable_api_call():
    global attempts

    attempts += 1

    print(f"Attempting API call: {attempts}")

    if attempts < 3:
        raise UpstoxServerError(
            "Simulated server failure"
        )

    return {"status": "success"}


def main():
    result = retry(
        unreliable_api_call,
        retryable_exceptions=(
            UpstoxServerError,
        ),
        max_attempts=3,
        base_delay=0.5,
    )

    print(f"Final result: {result}")


if __name__ == "__main__":
    main()