# Simple program to validade password with max number of attempt
# Author Rocken2k 

secret = 'password123@' # select the password
pw = ''
auth = False
count = 0
max_attempt = 5 # select the maximum attempt

while pw != secret:
    count += 1    
    if count > max_attempt: break
    pw = input(f"{count} attempt: What's the secret word? ")
else:
    auth = True

print ("Authorized!" if auth else "*** Not Authorized ***")
