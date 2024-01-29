def speeding_ticket(speed, is_birthday):
    # Define speed limits
    no_ticket_limit = 60
    small_ticket_limit = 80

    # Adjust speed limits on birthday
    if is_birthday == "True":
        no_ticket_limit += 5
        small_ticket_limit += 5

    # Check speed and return the appropriate result
    if speed <= no_ticket_limit:
        return "No Ticket"
    elif speed <= small_ticket_limit:
        return "Small Ticket"
    else:
        return "Big Ticket"


speed = input("Enter the speed: ")
speed = int(speed) 

is_birthday = input("Is today his/her birthday:")

result = (speeding_ticket(speed, is_birthday))
print(result)
