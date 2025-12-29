# Electronics Shop Chatbot


# available items
available_items = {
    "tv": {"name": "LED TV", "price": 14999, "discount": "5% off"},
    "fridge": {"name": "Refrigerator", "price": 11999, "discount": "No discount"},
    "refrigerator": {"name": "Refrigerator", "price": 11999, "discount": "No discount"},
    "washing machine": {"name": "Washing Machine", "price": 17999, "discount": "7% off"},
    "mobile": {"name": "Smartphone", "price": 10999, "discount": "15% off"},
    "microwave": {"name": "Microwave Oven", "price": 7000, "discount": "No discount"},
    "laptop": {"name": "Laptop", "price": 72999, "discount": "12% off"},
    "headphone": {"name": "Headphone", "price": 1299, "discount": "12% off"},
    "bluetooth": {"name": "Bluetooth Speakers", "price": 1599, "discount": "9% off"},
}

def shop_chatbot(user_input):
    
    greeting = "\tWelcome to  Partha Electronics!\n"

    # informations
    responses = {
        "opening time": "We open our shop at 10:00 AM every day.\nFull day close on Saturday and Sunday.",
        "closing time": "We close at 9:00 PM.\nFull day close on Saturday and Sunday.",
        "address": "Our shop is located in Kolkata, West Bengal, India.",
        "location": "Our shop is located in Kolkata, West Bengal, India.",
        "owner": "The shop is owned by Mr. Partha Konai.",
        "products": "We sell TVs, refrigerators, washing machines, mobile phones, and more.",
        "items": "We sell TVs, refrigerators, washing machines, mobile phones, and more.",
        "discount": "Currently, we have special discounts on selected items. Ask about a product!",
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What would you like to know?",
        "hey": "Hi there! What would you like to know?",
        "bye": "Thank you for visiting! Have a great day!",
        "name": "I haven't any specific name as human\nI'm AI Bot to assist you."
    }

    
    user_input = user_input.lower()

    # Check if user is asking about a product
    for item in available_items:
        if item in user_input:
            product = available_items[item]
            return (greeting +
                    f"{product['name']} is available at ₹{product['price']} "
                    f"({product['discount']}).")

    # Search for matching response
    for key in responses:
        if key in user_input:
            return greeting + responses[key]

    # Default response
    return greeting + "Sorry, I don’t have information on that. Please Contact our shop.\nPlease ask about shop timings, address, owners, or products."

#    Example Conversation 
while True:
    user = input("Customer: ")
    if user.lower() in ["exit", "quit", "bye"]:
        print("Chatbot:", shop_chatbot("bye"))
        break
    else:
        print("Chatbot:", shop_chatbot(user))
