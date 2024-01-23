import openai
openai.api_key = "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"

def predict_gpt(text):
    messages = [
        {"role": "system", 
         "content": """You are trained to analyze and detect the sentiment of given text. 
                   You must give just one answer : positive or negative or neutral."""},
        {"role": "user", "content": f"""Analyze the following product review 
        and determine if the sentiment is: positive or negative or neutral.  
        Return answer in single word as either positive or negative or neutral: {text}"""}
    ]
   
    response = openai.ChatCompletion.create(
                      model="gpt-3.5-turbo",
                      messages=messages, 
                      max_tokens=1, 
                      n=1, 
                      stop=None, 
                      temperature=0
                )

    response_text = response.choices[0].message.content.strip().lower()

    return response_text