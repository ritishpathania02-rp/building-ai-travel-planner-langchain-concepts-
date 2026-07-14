from langchain_core.prompts import ChatPromptTemplate as cpt
ai_prompt = cpt.from_template("""
You are an expert travel planner.

Create a travel itinerary based on the following details:

Destination: {destination}
Number of Days: {days}
Budget: {budget}
Interests: {interests}
Travel Date: {travel_date}

Provide:

1. Day-wise itinerary
2. Estimated budget breakdown
3. Packing suggestions
4. Local travel tips
""")