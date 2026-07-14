from chain import travelchain

destination = input("Enter Destination: ")
days = input("Enter Number of Days: ")
budget = input("Enter Budget: ")
interests = input("Enter Interests: ")
travel_date = input("Enter Travel Date: ")

ans = travelchain.invoke(    {
        "destination": destination,
        "days": days,
        "budget": budget,
        "interests": interests,
        "travel_date": travel_date
    })
print(ans)