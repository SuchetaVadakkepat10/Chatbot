import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_BREATHING = "I am a chatbot, hence I do not really breathe:) "
R_NEWS = "Today's news is that today is a good day"
R_PROBLEM = "I will address this query as soon as possible."

def unknown():
    response_list = ["Could you please re-phrase that? ", "...", "Sounds about right.", "What does that mean?", "I didn't understand your question. Please rephrase it.", "It will take some time for me to solve this query.", "Sorry, I did not get that.", "Can you repeat that?"]
    response = random.choice(response_list)
    return response