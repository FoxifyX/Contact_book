import random
import string

print("\n----Welcome to master mind game----\n")
print("📒 Rule 📒\n1.Attemt to guess the 4 digit code\n2.You have 10 tries\n")

letters = random.choices(string.ascii_lowercase, k=6)
code = "".join(random.choices(letters, k=4))

print(f"The code is from this letters: ", end="")
for x in letters:
    print(f"{x} ", end="")

print("\n")

count = 0



while count<10:
    user_code = input("Guess the code: ")
    positive = 0
    negetive = 0

    if len(user_code) == 4 :
        if code == user_code:
            print("🚀 You have guessed the code..\n")    
            break

        for idx, x in enumerate(code):
            if user_code[idx] == code[idx]:
                positive += 1
            if user_code[idx] != code[idx]:
                negetive += 1

        print(f"✅ Matched: {positive}\n❌ Didn't Matched: {negetive}")

        count += 1
        print(f"📝 You have only {10-count} attempts\n")
    
    else:
        print("⚠️ Please enter a valid 4 digit code!\n")

    if count == 10:
        print(f"⚠️ You have failed to guess the code\n👉 The code: {code}\n")






