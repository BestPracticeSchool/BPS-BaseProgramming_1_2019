print("Kek")
print(1 / 0)

# NOT WORKING
# RUNTIME === WORKING
# FALLEN 
# GRACEFUL SHUTDOWN

#PERFECT: NOT WORKING --> RUNTIME -- > GRACEFUL SHUTDOWN -- > NOT WORKING


# WE HAVE: NOT WORKING -- > RUNTIME -- > FALLEN --> NOT WORKING 

# OUR SOLUTION: NOT WORKING -- >RUNTIME -- >FALLEN -- >RUNTIME --> GRACEFUL SHUTDOWN


# EXCEPTION === RUNTIME -- >FALLEN 
# EXCEPTIONS HANDLING ==== RUNTIME -- >FALLEN -- >RUNTIME