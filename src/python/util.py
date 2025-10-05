def ordinal(n: int) -> str:
    a = abs(n)
    suffix = (
        "th"
        if (a % 100) > 10 and (a % 100) < 14  # special case for 11th, 12th, 13th
        else {1: "st", 2: "nd", 3: "rd"}.get(a % 10, "th")
    )
    return f"{n}{suffix}"
