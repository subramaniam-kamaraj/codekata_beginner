s=input()

if len(s)==1 and s.isalpha()==True:
	if (s=='a' or s=='e' or s=='i'or s=='o' or s=='u' or s=='A' or s=='E' or s=='I' or s=='O'or s=='U'):
		print("vowel")
	else:
		print("consonant")
else:
	print("invalid")
	
