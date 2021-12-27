#To convert a number to words
#First we have to define terminology in lists
number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
nty_s=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
ten_s=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
n=int(input("Enter a number(between 0-5 digits): ")) #Input of assigned number
if n>99999:
    print("Sorry, please choose a number in a range of 5 digits")
else:
    s=[0,0,0,0,0] #indexing in python 0 1 2 3 4 as units, tens, hundreds and thousands
    i=0
    while n>0: #fragmenting the given number accordingly
        s[i]=n%10
        i+=1
        n=n//10
    num="" #defining for output
    if s[4]!=0: #indexing 5th digit to represent single or double like twent one(21)
        if(s[4]==1):
            num+=ten_s[s[3]]+ " Thousand "
        else:
            num+=nty_s[s[4]]+" "+number[s[3]]+  " Thousand " #Completed thousands and ten thousands place
    else:
        if s[3]!=0:
            num+=number[s[3]]+ " Thousand " #checked for thousand
    if s[2]!=0:
        num+=number[s[2]]+" Hundred "+"and " #checked for hundred place
    if s[1] != 0:
        if (s[1] == 1):
            num += ten_s[s[0]]      #checked for tens place
        else:
            num += nty_s[s[1]] + " " + number[s[0]] #Checked for sigle digit
    else:
        if s[0] != 0:
            num += number[s[0]] #repeat the process
    print(num)