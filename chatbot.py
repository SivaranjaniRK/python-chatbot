responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! How can I assist you?",
    "whats your name?": "I'm Teddy, a simple python chatbot!",
    "who are you?": "I'm a chatbot created to assist you about chatbots.",
    "how are you?": "I'm doing great!",
    "bye": "Goodbye! Have a nice day! <3",
    "exit": "Goodbye! Have a nice day! <3",
    "what is chatbot?":"A chatbot is a software application designed to simulate human conversation through text or voice interactions. It is a form of artificial intelligence (AI) that allows users to communicate with a digital system in natural language, often through messaging platforms, websites, or apps. Chatbots can be as simple as rule-based programs that provide predefined answers or as advanced as AI-powered bots capable of understanding context, sentiment, and user intent.",
    "uses of chatbot":"Chatbots are widely used in customer service, education, healthcare, banking, entertainment, and e-commerce. Their main purpose is to automate conversations, provide instant responses, reduce human workload, and enhance user experience. For example, a chatbot on an e-commerce site can help customers track orders, answer questions about products, or even recommend items based on preferences.",
    "types of chatbots":"There are mainly two types of chatbots: \n1)Rule-based Chatbots: \n> Follow pre-set rules or decision trees. \n> Respond only to specific inputs. \n2) AI-based Chatbots (Smart Chatbots): \n> Use machine learning (ML) and Natural Language Processing (NLP). \n> Understand context, learn from interactions, and improve over time.",
    "how do chatbots work?":"At the core, a chatbot processes user input and generates a response using one of the following: \n1) Keyword Matching: Identifies specific words and triggers a response. \n2) Natural Language Processing (NLP): Understands and interprets human language. \n3)Machine Learning: Learns from past conversations to improve future interactions.",
    "advantages":"24/7 Availability – Always ready to assist users. \nInstant Response – No waiting time like with human support. \nCost-Effective – Reduces need for human agents. \nScalable – Can handle thousands of users simultaneously.",
    "disadvantages":"May fail with complex queries or emotions, Depend on training data and rules, Might misunderstand slang or ambiguous language.",
    "technologies used":"Python, JavaScript , NLP Libraries, Chatbot Platforms, APIs"
}

def chatbot():
    print("Welcome to the Python Chatbot! (Type 'bye' or 'exit' to quit)")
    while True:
        user_input = input("User: ").lower().strip()

        if user_input in ["bye", "exit"]:
            print("Bot:", responses["bye"])
            break

        response_found = False
        for key in responses:
            if key in user_input:
                print("Bot:", responses[key])
                response_found = True
                break

        if not response_found:
            print("Bot: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()
