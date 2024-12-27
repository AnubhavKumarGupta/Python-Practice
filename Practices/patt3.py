# def generate_pattern(rows):
#     start_char = ord('A')  # Starting character ('A')

#     for i in range(rows):
#         row = ""
#         current_char = start_char + i

#         for j in range(i + 1):
#             row += chr(current_char)
#             current_char += 1

#         print(row)

# # Get the number of rows from the user
# num_rows = int(input("Enter the number of rows: "))

# # Generate the pattern
# generate_pattern(num_rows)

# Import instaloader package
import instaloader

# creating an Instaloader() object
ig=instaloader.Instaloader()

# Taking the instagram username as input from user
usrname=input("Enter username:")

#Fetching the details of provided useraname using instaloder object
profile=instaloader.Profile.from_username(ig.context, usrname)

# Printing the fetched details and storing the profile pic of that account
print("Username: ", profile.username)
print("Number of Posts Uploaded: ", profile.mediacount)
print(profile.username+" is having " + str(profile.followers)+' followers.')
print(profile.username+" is following " + str(profile.followees)+' people')
print("Bio: ", profile.biography)
instaloader.Instaloader().download_profile(usrname,profile_pic_only=True)