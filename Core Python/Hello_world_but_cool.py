from time import sleep
letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM! "

target = "Hello world!"
current = ""
iterator = 0

while current != target:
    for letter in letters:
        if target[iterator] == letter:
            current += letter
            iterator += 1
            print(current)
            sleep(0.05)

            if current == target:
                break
