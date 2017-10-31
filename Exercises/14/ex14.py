from sys import argv
script, user_name =argv
prompt = '> '

print(f"Hi, {user_name}, I'm the {script} script!" )
print( "I'd like to ask you a few questions." )

likes = input( "Do you like me? " )
live = input( "Where abouts do you live? " )
computer = input( "What kind of computer do you own? " )

print(f"""
Alright, so you said {likes} about liking me.
You live in {live}. I'm not sure where that is!
And you have a {computer} computer. Cool!
""")
