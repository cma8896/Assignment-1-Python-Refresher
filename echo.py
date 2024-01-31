# Cade Anderson
# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    return (
        text[-repetitions:]
        + "\n"
        + text[-repetitions + 1 :]
        + "\n"
        + text[-repetitions + 2 :]
        + "\n"
        + "."
    )


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
