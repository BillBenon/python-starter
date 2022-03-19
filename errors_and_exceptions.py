try:
    f = open('simple.txt', 'r')
    f.write("Test write to simple.txt")
# except:     This is universal
except IOError:
    print("Could not find file or read data!")

else:
    print('SUCCESS')
    f.close()
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")

print("Hello World!")
