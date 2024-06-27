import time
def dprint(string):
   for letter in string:
        __builtins__.print(letter,end = '', flush=True)
        time.sleep(.1)
   __builtins__.print("")

print = dprint

print("Test 123 wie geht das?")