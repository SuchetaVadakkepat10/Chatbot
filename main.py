import re
import longer_messages as longer

def percentage_match(matching_words, length_words):
    '''Calculates the match percentage between the matching words and length of the words'''
    return int((float(matching_words)/ float(length_words)) * 100)

def find_probability(user_message, key_words, single_response=False, required_words = []):
    '''Finds the match percentage between the user_input and the key_words that need to be present.'''
    match_words = 0
    has_reqd_words = True
    for word in user_message: 
        if word in key_words:
            match_words += 1 

    match_percentage = percentage_match(match_words, len(key_words))

    for word in required_words:
        if word not in user_message:
            has_reqd_words = False
            break

    if has_reqd_words or single_response:
        return match_percentage
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response_generation(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = find_probability(message, list_of_words, single_response, required_words)

    
    response_generation('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response_generation('See you!', ['bye', 'goodbye'], single_response=True)
    response_generation('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response_generation('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response_generation('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response_generation('Sorry to hear that:(', ['i', 'had', 'a', 'bad', 'day'], required_words=['bad', 'day'])
    response_generation('Have a good day!', ['have','a', 'good', 'day'], required_words=['good', 'day'])
    response_generation('I will address this query as soon as possible', ['can', 'you', 'please', 'solve', 'this', 'query'], required_words=['solve', 'query'])


    response_generation(longer.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response_generation(longer.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response_generation(longer.R_BREATHING,['do', 'you', 'breathe'], required_words=['breathe'] )
    response_generation(longer.R_NEWS,['what', 'is', 'the', 'news'], required_words=['news'] )
    response_generation(longer.R_PROBLEM,['facing', 'this', 'pi roblem', 'i', 'help'], required_words=['facing', 'problem', 'help'] )


    best_match = max(highest_prob_list, key=highest_prob_list.get)

    if highest_prob_list[best_match] < 1:
        return longer.unknown()  
    else:
        return best_match

def get_response(user_input_message):
    '''
    Has two functions: 1) Splits the user message into words 
    2) Returns the response of the chatbot
    '''
    split_words = re.split(r'\s+|[,;?!.-]\s*', string=user_input_message.lower())
    response = check_all_messages(split_words)
    return response
while True:
    user_input = input("You: ")
    print("Bot: " + get_response(user_input))