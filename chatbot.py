def chatbot():
    print("Hi! I'm ChatBot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'exit':
            print("ChatBot: Goodbye! Have a nice day!")
            break
        elif any(greet in user_input for greet in ['hello', 'hi', 'hey']):
            print("ChatBot: Hello! How can I assist you today?")
        elif 'how are you' in user_input:
            print("ChatBot: I'm just a program, but I'm functioning well. How about you?")
        elif 'your name' in user_input:
            print("ChatBot: I'm ChatBot, your virtual assistant.")
        elif 'help' in user_input:
            print("ChatBot: I can chat with you, tell jokes, do simple math, and answer a few questions.")
        elif 'weather' in user_input:
            print("ChatBot: I can't check real-time weather, but I hope it's nice where you are!")
        elif 'joke' in user_input:
            print("ChatBot: Why did the scarecrow win an award? Because he was outstanding in his field!")
        elif 'add' in user_input or 'sum' in user_input or '+' in user_input:
            import re
            numbers = re.findall(r'\d+', user_input)
            if len(numbers) >= 2:
                total = sum(map(int, numbers))
                print(f"ChatBot: The sum is {total}.")
            else:
                print("ChatBot: Please provide two or more numbers to add.")
        elif 'subtract' in user_input or 'minus' in user_input or '-' in user_input:
            import re
            numbers = re.findall(r'-?\d+', user_input)
            if len(numbers) >= 2:
                result = int(numbers[0]) - int(numbers[1])
                print(f"ChatBot: The result of subtraction is {result}.")
            else:
                print("ChatBot: Please provide two numbers to subtract.")
        elif 'multiply' in user_input or 'times' in user_input or '*' in user_input:
            import re
            numbers = re.findall(r'\d+', user_input)
            if len(numbers) >= 2:
                product = 1
                for num in numbers:
                    product *= int(num)
                print(f"ChatBot: The product is {product}.")
            else:
                print("ChatBot: Please provide two or more numbers to multiply.")
        elif 'divide' in user_input or '/' in user_input:
            import re
            numbers = re.findall(r'\d+', user_input)
            if len(numbers) >= 2:
                try:
                    result = int(numbers[0]) / int(numbers[1])
                    print(f"ChatBot: The division result is {result}.")
                except ZeroDivisionError:
                    print("ChatBot: Cannot divide by zero.")
            else:
                print("ChatBot: Please provide two numbers to divide.")
        elif any(farewell in user_input for farewell in ['bye', 'goodbye', 'see you']):
            print("ChatBot: Goodbye! Looking forward to chatting again.")
            break
        else:
            print("ChatBot: Sorry, I don't understand that. Can you ask something else?")

if __name__ == '__main__':
    chatbot()
