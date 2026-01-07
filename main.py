import requests
def get_random_joke():
    url="https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)
    if response.status_code==200:
        print(f"full JSON response:{response.json()}")

        joke_data=response.json()

        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "failed to retrieve joke"

def main():
    print("Welcome to random joke generator")
    while True:
        user_input=input("press enter to get a joke or press q or exit to quit").strip().lower()

        if user_input in("q","exit"):
            print("Goodbye")
            break
        joke=get_random_joke()
        print(joke)

if __name__=="__main__":
    main()