import json
from pathlib import Path

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

HISTORY_FILE = Path("chat_history.json")


def load_history(file_path: Path):
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
            except json.JSONDecodeError:
                pass
    return []


def save_history(file_path: Path, history):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=2)


def format_history(history):
    if not history:
        return "No previous conversation yet."

    formatted = []
    for entry in history:
        role = entry.get("role", "unknown")
        content = entry.get("content", "")
        formatted.append(f"{role}: {content}")
    return "\n".join(formatted)


# destination = input("Enter your travel destination: ")
# days = input("Enter the number of days for your trip: ")
# budget = input("Enter your budget for the trip: ")
# interest = input("Enter your interests for the trip: ")
destination = "manali"
days = "4"
budget = "20000"
interest = "adventure, nature, and local culture"

history = load_history(HISTORY_FILE)

prompt1 = ChatPromptTemplate.from_template('''
you are a Travel planner,
here are some information from the user:
destination: {destination}
days: {days}
budget: {budget}
interest: {interest}
from above information, please provide a travel plan for the user.
which includes the following:
1. Day-wise itinerary
2. budget breakdown
3. tips for the user''')

llm = ChatOllama(model="llama3:latest")
parser = StrOutputParser()
chain = prompt1 | llm | parser
result = chain.invoke({"destination": destination, "days": days, "budget": budget, "interest": interest})
print(result)

history.append({"role": "user", "content": f"destination: {destination}, days: {days}, budget: {budget}, interest: {interest}"})
history.append({"role": "assistant", "content": result})
save_history(HISTORY_FILE, history)

print("would you like to continue with chat [y/n]?")
if input().lower() in ("no", "n"):
    print("Thank you for using the travel planner!")
else:
    print('for future you want to close chat, please type "exit"')
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Thank you for using the travel planner!")
            break

        prompt2 = ChatPromptTemplate.from_template('''
        you have already provided a travel plan for the user based on the following information:
        destination: {destination}
        days: {days}
        budget: {budget}
        interest: {interest}
        previous conversation:
        {history}
        user question: {user_input}
        please provide a response to the user question
        based on the previous travel plan
        and information provided''')

        chain2 = prompt2 | llm | parser
        result2 = chain2.invoke({
            "destination": destination,
            "days": days,
            "budget": budget,
            "interest": interest,
            "history": format_history(history),
            "user_input": user_input,
        })
        print(result2)

        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": result2})
        save_history(HISTORY_FILE, history)
