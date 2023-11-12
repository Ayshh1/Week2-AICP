
NUM_JOURNEYS = 4
NUM_COACHES_NORMAL = 6
NUM_COACHES_LAST_TRAIN = 8
SEATS_PER_COACH = 80
TICKET_PRICE = 25.0


def initialize_day():
   
    passengers_up = [0] * NUM_JOURNEYS
    passengers_down = [0] * NUM_JOURNEYS

    money_up = [0.0] * NUM_JOURNEYS
    money_down = [0.0] * NUM_JOURNEYS

    closed_up = [False] * NUM_JOURNEYS
    closed_down = [False] * NUM_JOURNEYS

    return passengers_up, passengers_down, money_up, money_down, closed_up, closed_down

def display_start_of_day(passengers_up, passengers_down, money_up, money_down, closed_up, closed_down):
    print("\nStart of the Day - Screen Display:")
    for i in range(NUM_JOURNEYS):
        print(f"\nJourney {i + 1} Up:")
        print(f"Passengers: {passengers_up[i]}, Money: ${money_up[i]:.2f}, Closed: {closed_up[i]}")

        print(f"\nJourney {i + 1} Down:")
        print(f"Passengers: {passengers_down[i]}, Money: ${money_down[i]:.2f}, Closed: {closed_down[i]}")


print("\nElectric Mountain Railway - Start of the Day")


passengers_up, passengers_down, money_up, money_down, closed_up, closed_down = initialize_day()


display_start_of_day(passengers_up, passengers_down, money_up, money_down, closed_up, closed_down)
