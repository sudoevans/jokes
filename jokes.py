import requests
#Free Joke API
try:
    api='https://geek-jokes.sameerkumar.website/api'

    jokes=['\n']
    joke_number=0

#Loading Jokes
    def preload_jokes():
        print('**Loading Jokes**')
        for i in range(5):
            noris_joke=requests.get(api).json()
            jokes.append(noris_joke)
        print(jokes)
        

#calling the Function
    preload_jokes()
    print('Jokes Done Loading!')
    
except ConnectionError as e:
    print("Sorry No InterNet ")

