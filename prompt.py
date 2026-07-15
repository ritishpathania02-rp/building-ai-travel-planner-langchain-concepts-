from langchain_core.prompts import ChatPromptTemplate as cpt
# ai_prompt = cpt.from_template("""
# You are an expert travel planner.

# Create a travel itinerary based on the following details:

# Destination: {destination}
# Number of Days: {days}
# Budget: {budget}
# Interests: {interests}
# Travel Date: {travel_date}

# Provide:

# 1. Day-wise itinerary
# 2. Estimated budget breakdown
# 3. Packing suggestions
# 4. Local travel tips
# """)

itinerary_prompt = cpt.from_template("""
You are an expert travel planner.

Destination: {destination}
Days: {days}
Budget: {budget}
Interests: {interests}
Travel Date: {travel_date}

Generate a detailed day-wise itinerary and you have only generate itinerary , and there sould no budget and tips.
""")

budget_prompt = cpt.from_template("""
    "destination": {destination},
    "days": {days},
    "budget": {budget},
    "interests": {interests}

Estimate the budget in detail.

Include:
- Hotel
- Food
- Transport
- Activities
""")

tips_prompt = cpt.from_template("""
Destination: {destination}

Provide:

- Packing suggestions
- Safety tips
- Local travel tips
""")
