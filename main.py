from pyscript import document, display
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
plt.plot([0,1], [0,1])
plt.close()

days = []
absences = []

def submit_button(e):
    output = document.getElementById("output")
    day = document.getElementById('day_absences').value
    absence = document.getElementById('number_absences').value
    
    days.append(day)
    absences.append(absence)
    days_absences = np.array(absences)

    plt.clf() #This is used to so that the graph won't double when user clicks submit again (it clears previous graph)
    plt.plot(days, days_absences, marker='o')
    plt.show() #This shows the graph after the user clicks submit

    plt.title("Weekly Attendance") #Title of the graph
    plt.xlabel("Days of the Week") #Label of the x axis (the one at the bottom of the graph)
    plt.ylabel("Number of Absences")#Label for the y axis (left of the graph)
   

