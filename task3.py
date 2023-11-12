
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


def purchase_tickets(passengers_up, passengers_down, money_up, money_down, closed_up, closed_down):
    journey_up = int(input("\nEnter the journey number up (1 to 4): ")) - 1
    journey_down = int(input("Enter the journey number down (1 to 4): ")) - 1

    if not (0 <= journey_up < NUM_JOURNEYS) or not (0 <= journey_down < NUM_JOURNEYS):
        print("Invalid journey numbers. Please enter valid journey numbers.")
        return

    if closed_up[journey_up] or closed_down[journey_down]:
        print("One or both of the selected journeys are closed. Tickets cannot be purchased.")
        return

    num_tickets = int(input("Enter the number of tickets to purchase: "))

    if num_tickets <= 0:
        print("Invalid number of tickets. Please enter a valid number.")
        return

    if num_tickets * 2 > NUM_COACHES_NORMAL * SEATS_PER_COACH:
        print("Not enough seats available. Please reduce the number of tickets.")
        return

   
    total_price = num_tickets * TICKET_PRICE

    if num_tickets >= 10:
        free_tickets = num_tickets // 10
        total_price -= free_tickets * TICKET_PRICE

    passengers_up[journey_up] += num_tickets
    money_up[journey_up] += total_price
    passengers_down[journey_down] += num_tickets
    money_down[journey_down] += total_price

   
    print("\nPurchase Successful!")
    print(f"\nJourney {journey_up + 1} Up:")
    print(f"Passengers: {passengers_up[journey_up]}, Money: ${money_up[journey_up]:.2f}, Closed: {closed_up[journey_up]}")

    print(f"\nJourney {journey_down + 1} Down:")
    print(f"Passengers: {passengers_down[journey_down]}, Money: ${money_down[journey_down]:.2f}, Closed: {closed_down[journey_down]}")


def display_end_of_day(passengers_up, passengers_down, money_up, money_down):
    print("\nEnd of the Day - Statistics:")
    for i in range(NUM_JOURNEYS):
        print(f"\nJourney {i + 1} Up:")
        print(f"Passengers: {passengers_up[i]}, Money: ${money_up[i]:.2f}")

        print(f"\nJourney {i + 1} Down:")
        print(f"Passengers: {passengers_down[i]}, Money: ${money_down[i]:.2f}")


    total_passengers = sum(passengers_up) + sum(passengers_down)
    total_money = sum(money_up) + sum(money_down)
    print("\nTotal Statistics:")
    print(f"Total Passengers: {total_passengers}, Total Money: ${total_money:.2f}")

    
    max_passengers_journey = passengers_up.index(max(passengers_up)) + 1
    print(f"\nJourney {max_passengers_journey} Up had the most passengers.")

print("\nElectric Mountain Railway Simulation")

print("\nTask 1 - Start of the Day")
passengers_up, passengers_down, money_up, money_down, closed_up, closed_down = initialize_day()
display_start_of_day(passengers_up, passengers_down, money_up, money_down, closed_up, closed_down)

print("\nTask 2 - Purchasing Tickets")
purchase_tickets(passengers_up, passengers_down, money_up, money_down, closed_up, closed_down)

print("\nTask 3 - End of the Day")
display_end_of_day(passengers_up, passengers_down, money_up, money_down)
