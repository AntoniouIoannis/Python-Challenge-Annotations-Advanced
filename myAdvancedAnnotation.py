def races(name: str, location: str, country: str, separator: str = ", ", end: str = ".\t") -> None:
    """
    _briefcase by i-antoniou_,
    Short Description:
        Prints dynamically the name of a Formula 1 race track with its location and country.

    Parameters:
        name (str): The name of the race track.
        location (str): The region where the race track is located.
        country (str): The country where the race track is located.
        separator (str, optional): A symbol to separate the fields. Default is ", ".
        end (str, optional): A symbol to end the printed line. Default is ".\t".
    """
    print(f"Race track: {name}{separator}Location: {location}{separator}Country: {country}{end}")


def main() -> None:
    """Demonstrates the usage of the races function."""
    # Adding Formula 1 tracks with name, location, and country
    races("Monza", "Lombardy", "Italy")
    races("Silverstone", "Northamptonshire", "United Kingdom")
    races("Suzuka", "Mie Prefecture", "Japan")
    races("Interlagos", "Sao Paulo", "Brazil", separator=" | ", end=".\n")


if __name__ == "__main__":
    main()


    