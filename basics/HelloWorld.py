message="Hellow God's world"
print(message)
print(len(message))
print(message[0:5])
#Retunrs the number occurrence of a string or character
print(message.count('w'))
#Returns the index of the character or string. For string, it returns the start index
print(message.find('l'))
#Replaces character or string
updated_message=message.replace("God's","")
print(updated_message)
#Formatted message with placeholders
greeting='{}, {}. Welcome!'.format('Hello','Thyagu')
#Formatting using F strings
greeting1=f'{message[:6]},{'Thyagu'}. Welcome'
print(greeting1)