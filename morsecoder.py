import string

chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."] * 2 + [".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", "/"]

morseOutput = ""

print("- Welcome to Morse Coder. -\n\nThis program translates your input into Morse Code. Only letters, numbers and spaces are accepted. Any other characters will be omitted.\n")

while True:
  morseOutput = ""
  stringInput = input("Enter your input: ")

  for i in range(len(stringInput)):
    if stringInput[i] in chars:
      morseOutput += (morse[chars.index(stringInput[i])] + " ")
    
  print(f"Your output:\n\n{morseOutput}\n")
