def CheckVowel(ch):
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'
         or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        return "Vowel"     
    else:
        return "Consonant"
        
def main():
    print("Enter a character : ")
    ch = (input())

    Ret = CheckVowel(ch)
    print("The character is  : ",Ret)

if __name__ == "__main__":
    main()