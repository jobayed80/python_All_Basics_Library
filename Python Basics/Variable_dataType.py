
character_age = 23
character_name = "Jobayed"
ismale = False

print("\n")
# If the character will be String, we have to write plus + before and after variables
print("There once was a man named '" +character_name+ "',")

# If the character will be String, we have to write comma before and after variables
print("He was '"  ,character_age, "' years old")

# we can write another way for str and int function like below here
character_name = str("Rabbi")
character_age = int(23)
print("He really liked the name '"+character_name+ "',")
print("But didn't like being '" , character_age,     "',")

# Float Variable
weight = 80.56
print("How much your weight: ", weight)

# List variable like array
fruit = ["apple", "banana", "cherry"]
print("I like this kinds of fruits: ", fruit)

# Range variable like from 10 to 100
range= range(10,100)
print(list(range))

#
personal_info = ("Name : Jobayed", "Age: 25", "Location: Australia")
print("My details", personal_info, "\n" , type(personal_info))

if(ismale == True):(
    print("Yes, I am a Male")
)
elif (ismale == False):(
    print("No, I am not a Male")
)