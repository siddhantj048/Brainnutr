import matplotlib.pyplot as plt
def plots(l1,l2):

    plt.bar(l1, l2, color ='cyan',
        width = 0.4)
    
    plt.xlabel("students")
    plt.ylabel("streak")
    plt.title("streak of students demographic")
    plt.show()
