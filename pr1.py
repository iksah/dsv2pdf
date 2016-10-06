import matplotlib.pyplot as plt
import os
import csv



def bar_mode(args = []):
    spam = plt.figure()
    plt.bar([1, 2 ,3], args[2])
    plt.title(args[0])
    plt.grid = 0
    plt.show()
    


def pie_mode(args = []):
    spam = plt.figure()
    plt.pie(x = args[2], labels = args[1],
        shadow = 0,
        startangle = 95,
        autopct = '%1.1f%%')
    plt.title(args[0])
    plt.show()

args = ['lulz', ['ivan', 'Ilia', 'Alex'], [25, 25, 50]]
pie_mode(args)
#bar_mode(args)
