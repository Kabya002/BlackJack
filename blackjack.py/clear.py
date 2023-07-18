def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)