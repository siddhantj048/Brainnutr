import matplotlib.pyplot as plt
def plots(l1,l2):

    plt.bar(l1, l2, color ='cyan',
        width = 0.2)
    
    plt.xlabel("Students")
    plt.ylabel("Streak")
    plt.title("Streak of students demographic")
    plt.show()
