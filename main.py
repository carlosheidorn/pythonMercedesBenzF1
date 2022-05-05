# This is a sample Python script.
import mysql.connector
import matplotlib.pyplot as plt

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Solrac80$$",
  database=""
)

mycursor = mydb.cursor()

print(f'DESAFIO 2 : quantos veículos produzidos em 2019 por pais')

mycursor.execute("SELECT B.PAIS PAIS, COUNT(*) TOTAL \
            FROM world.veic AS A, world.cod_pais AS B \
            WHERE A.CodPais = B.COD  AND A.DTFLI LIKE '19%' \
            GROUP BY B.PAIS \
            ORDER BY 2 DESC LIMIT 10")

myresult = mycursor.fetchall()

Pais = []
Total = []
for i in myresult:
    Pais.append(i[0])
    Total.append(i[1])

print("Pais = ", Pais)
print("Total = ", Total)

plt.stem(Pais, Total)
plt.ylim(0, 15000)
plt.xlabel("Pais")
plt.ylabel("Total")
plt.title("Total Fabricação por Pais dos 10 maiores Paises")
plt.show()

print('')
print(f'DESAFIO 2 : qual % de veículos liberados com relação aos veículos')
mycursor.execute("SELECT Denominação, (COUNT(*) / \
                 (SELECT COUNT(*) FROM world.veic)) * 100 \
                   FROM world.veic \
                   WHERE DTLCO <> '0' \
                   GROUP BY Denominação \
                   ORDER BY 2 DESC LIMIT 5 ")

myresult = mycursor.fetchall()

Denominacao = []
Percentual = []
for i in myresult:
    Denominacao.append(i[0])
    Percentual.append(i[1])

print("Denominação = ", Denominacao)
print("Percentual = ", Percentual)

plt.bar(Denominacao, Percentual)
plt.ylim(0, 100)
plt.xlabel("Denominação")
plt.ylabel("Percentual")
plt.title("Percentual por Denominação das 5 maiores denominações")
plt.show()

print('')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
