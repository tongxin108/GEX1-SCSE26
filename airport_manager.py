######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################


airport_info = ("", None, "")
allowed_gates = None
restricted_destinations = None
flights = None
allowed_gates = set()
restricted_destinations = set()
flights = {}

## Logic to find if a flight exists
def find_flight(flights, flight_number):
    if not isinstance(flight_number, str):
        return None

    key = flight_number.strip().upper()

    if key in flights:
        return key

    return None   


## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    if not isinstance(passenger_name, str):
        return False

    target = passenger_name.strip().lower()

    for passenger in passengers:
        if isinstance(passenger, str) and passenger.strip().lower() == target:
            return True

    return False

## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    key = find_flight(flights, flight_number)

    if key is None:
        return "FLIGHT_NOT_FOUND"

    if not isinstance(passenger_name, str) or passenger_name.strip() == "":
        return "EMPTY_NAME"

    flight = flights[key]
    passengers = flight["passengers"]

    if passenger_exists(passengers, passenger_name):
        return "DUPLICATE"

    if flight["destination"] in restricted_destinations:
        return "RESTRICTED"

    if len(passengers) >= flight["capacity"]:
        return "FULL"

    passengers.append(passenger_name.strip().title())
    return "OK"


## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    key = find_flight(flights, flight_number)

    if key is None:
        return "FLIGHT_NOT_FOUND"

    if not isinstance(passenger_name, str):
        return "PASSENGER_NOT_FOUND"

    target = passenger_name.strip().lower()
    passengers = flights[key]["passengers"]

    for i in range(len(passengers)):
        if isinstance(passengers[i], str) and passengers[i].strip().lower() == target:
            passengers.pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"


# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    key = find_flight(flights, flight_number)

    if key is None:
        return "FLIGHT_NOT_FOUND"

    if not isinstance(new_gate, str):
            return "INVALID_GATE"

    normalized_gate = new_gate.strip().upper()

    if normalized_gate not in allowed_gates:
        return "INVALID_GATE"

    flights[key]["gate"] = normalized_gate
    return "OK"


# Logic to get the status of a flight
def flight_status(flight):
    passengers = flight["passengers"]
    capacity = flight["capacity"]

    if len(passengers) >= capacity:
        return "FULL"

    if capacity > 0 and len(passengers) / capacity >= 0.75:
        return "ALMOST FULL"

    return "AVAILABLE"



# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    key = find_flight(flights, flight_number)

    if key is None:
        return None

    return sorted(flights[key]["passengers"])


# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    total = 0

    for flight in flights.values():
        total += len(flight["passengers"])

    return total


# Logic to check if any flight is full
def any_full_flight(flights):
    for flight in flights.values():
        if len(flight["passengers"]) >= flight["capacity"]:
            return True

    return False


# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    if not flights:
        return False

    for flight in flights.values():
        if len(flight["passengers"]) == 0:
            return False

    return True