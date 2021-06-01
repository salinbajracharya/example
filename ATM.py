salin = 10000
pin = 4865 
print('Welcome to Nepal Bank ATM Service','\nPlease insert your Pin Number')
yourPin=input()
try:
    int(yourPin)
except Exception:
    print('Your Pin does not Match')
    pass      # or whatever
if pin==int(yourPin):
  print('Please proceed for your further option')