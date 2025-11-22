import requests

def main():
    userinput = input("Enter a name for a pokemon: \n")
 
    url = f"https://pokeapi.co/api/v2/pokemon/{userinput}"

    response = requests.get(url)

    data = response.json()

    name = data["name"]

    stat = data["ability"]

    print(name)

    



print("Welcome To The Pokedex!\n")



main()