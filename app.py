from chain import chain1, chain2, chain3

destination = input("Enter Destination: ")
days = input("Enter Number of Days: ")
budget = input("Enter Budget: ")
interests = input("Enter Interests: ")
travel_date = input("Enter Travel Date: ")

ans1 = chain1.invoke({
        "destination": destination,
        "days": days,
        "budget": budget,
        "interests": interests,
        "travel_date": travel_date
    })


ans2 = chain2.invoke({
    "destination": destination,
    "days": days,
    "budget": budget,
    "interests": interests
    })

ans3 = chain3.invoke({
    "destination":destination
})

print("======iternarty========")
print(ans1)
print('======budget==========')
print(ans2)
print("======tips=====")
print(ans3)
