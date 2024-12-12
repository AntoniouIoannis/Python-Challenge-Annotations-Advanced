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
    # Εισαγωγή Πίστες Formula1 με όνομα, τοποθεσία και χώρα.
    print("\n\nΠίστες Formula1 με όνομα, τοποθεσία και χώρα\n\t--------------------")
    races("Monza", "Lombardy", "Ιταλία")
    races("Silverstone", "Northamptonshire", "Ηνωμένο Βασίλειο")
    races("Suzuka", "Mie Prefecture", "Ιαπωνία")
    races("Interlagos", "Sao Paulo", "Βραζιλία", separator=" | ", end=".")
    races("Marina Bay Street Circuit", "Singapore", "Σιγκαπούρη", separator=" | ", end=".")
    races("Circuit de Barcelona-Catalunya", "Montmelo", "Ισπανία", separator=" | ", end=".")
    races("Shanghai International Circuit", "Shanghai", "Κίνα",  separator=" | ", end=".")
    races("Zandvoort", "Zandvoort", "Ολλανδία", separator=" | ", end=".")
    races("Hungaroring", "Mogyoród", "Ουγγαρία", separator=" | ", end=".")    
    races("Circuit de Monaco", "Monte Carlo", "Μονακό", separator=" | ", end=".")
    races("Spa-Francorchamps", "Stavelot", "Βέλγιο", separator=" | ", end=".")  
    races("Bahrain International Circuit", "Sakhir", "Μπαχρέιν", separator=" | ", end=".")
    races("Albert Park Circuit", "Melbourne", "Αυστραλία", separator=" | ", end=".")
    races("Hockenheimring", "Hockenheim", "Γερμανία", separator=" | ", end=".")
    races("Yas Marina Circuit", "Abu Dhabi", "Ηνωμένα Αραβικά Εμιράτα", separator=" | ", end=".")
    races("Circuit of the Americas", "Austin", "Ηνωμένες Πολιτείες της Αμερικής", separator=" | ", end=".")
    races("Kyalami", "Midrand", "Νότια Αφρική", separator=" | ", end=".")
    races("Circuit Paul Ricard", "Le Castellet", "Γαλλία", separator=" | ", end=".")
    races("Istanbul Park", "Tuzla", "Τουρκία", separator=" | ", end=".\n\t--------------------\n")


if __name__ == "__main__":
    main()


    
