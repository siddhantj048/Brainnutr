def connector():
    import mysql.connector as m
    con = m.connect(host='localhost', user='root', passwd='fashbooster2004!', database='bntr')
    if con.is_connected():
        print("success")
    else:
        print("error")

def plots():
    import matplotlib.pyplot as plt

    data = {'C':20, 'C++':15, 'Java':30,
        'Python':35}
    courses = list(data.keys())#[c,c++,java,py]
    values = list(data.values())#[20,15,30,35]

    plt.bar(courses, values, color ='cyan',
        width = 0.4)
 
    plt.xlabel("Courses offered")
    plt.ylabel("No. of students enrolled")
    plt.title("Students enrolled in different courses")
    plt.show()

