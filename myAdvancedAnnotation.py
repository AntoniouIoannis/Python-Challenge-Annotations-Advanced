def car_racing_tracks(name: str, location: str, country: str, separator: str = ", ", end: str = ".\t") -> None:
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
    print(f"Car Racing Tracks: {name}{separator}Location: {location}{separator}Country: {country}{end}")


def main() -> None:
    """Demonstrates the usage of the races function."""
    # Εισαγωγή Πίστες Formula1 με όνομα, τοποθεσία και χώρα.
    print("\n\nΠίστες Formula1 με όνομα, τοποθεσία και χώρα\n\t--------------------")
    car_racing_tracks("Monza", "Lombardy", "Ιταλία")
    car_racing_tracks("Silverstone", "Northamptonshire", "Ηνωμένο Βασίλειο")
    car_racing_tracks("Suzuka", "Mie Prefecture", "Ιαπωνία")
    car_racing_tracks("Interlagos", "Sao Paulo", "Βραζιλία", separator=" | ", end=".")
    car_racing_tracks("Marina Bay Street Circuit", "Singapore", "Σιγκαπούρη", separator=" | ", end=".")
    car_racing_tracks("Circuit de Barcelona-Catalunya", "Montmelo", "Ισπανία", separator=" | ", end=".")
    car_racing_tracks("Shanghai International Circuit", "Shanghai", "Κίνα",  separator=" | ", end=".")
    car_racing_tracks("Zandvoort", "Zandvoort", "Ολλανδία", separator=" | ", end=".")
    car_racing_tracks("Hungaroring", "Mogyoród", "Ουγγαρία", separator=" | ", end=".")    
    car_racing_tracks("Circuit de Monaco", "Monte Carlo", "Μονακό", separator=" | ", end=".")
    car_racing_tracks("Spa-Francorchamps", "Stavelot", "Βέλγιο", separator=" | ", end=".")  
    car_racing_tracks("Bahrain International Circuit", "Sakhir", "Μπαχρέιν", separator=" | ", end=".")
    car_racing_tracks("Albert Park Circuit", "Melbourne", "Αυστραλία", separator=" | ", end=".")
    car_racing_tracks("Hockenheimring", "Hockenheim", "Γερμανία", separator=" | ", end=".")
    car_racing_tracks("Yas Marina Circuit", "Abu Dhabi", "Ηνωμένα Αραβικά Εμιράτα", separator=" | ", end=".")
    car_racing_tracks("Circuit of the Americas", "Austin", "Ηνωμένες Πολιτείες της Αμερικής", separator=" | ", end=".")
    car_racing_tracks("Kyalami", "Midrand", "Νότια Αφρική", separator=" | ", end=".")
    car_racing_tracks("Circuit Paul Ricard", "Le Castellet", "Γαλλία", separator=" | ", end=".")
    car_racing_tracks("Istanbul Park", "Tuzla", "Τουρκία", separator=" | ", end=".\n\t--------------------\n")


if __name__ == "__main__":
    main()


    
