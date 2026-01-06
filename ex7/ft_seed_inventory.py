def ft_seed_inventory(type: str, nb: int, seed: str) -> None:
    holder = type.capitalize()
    if seed == "packets":
        print(f"{holder} seeds: {nb} packets available")
    elif seed == "grams":
        print(f"{holder} seeds: {nb} grams total")
    elif seed == "area":
        print(f"{holder} seeds: covers {nb} square meters")
    else:
        print("Unknown unit type")
