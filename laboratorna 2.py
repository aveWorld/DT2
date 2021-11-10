from tabulate import tabulate

def count_5(mat):
    income = 5 * mat[1]
    waste = 5 * mat[3]
    expected_win = income * mat[2] + waste * mat[4] - mat[0]
    return income, waste, expected_win

def count_4(mat, mat_cof):
    income = 4 * mat[1]
    waste = 4 * mat[3]
    expected_win = income * mat_cof[2] + waste * mat_cof[3] - mat[0]
    return income, waste, expected_win

def if_esle(A, B):
    if A > B:
        win = A
    else:
        win = B
    return win

def table_show(header, data1, data2):
    table = [header, data1, data2]
    show = tabulate(table, headers='firstrow', tablefmt='fancy_grid', 
                    showindex=range(1, len(table)), colalign=("center", "center"))
    print(show)

mat = []
with open ('laboratorna 2.txt', 'r') as file:
    for line in file:
        strip = line.strip()
        split = strip.split(' ')
        split = [float(i) for i in split]
        mat.append(split)

income_A_5, waste_A_5, win_A_5 = count_5(mat[0])
income_B_5, waste_B_5, win_B_5 = count_5(mat[1])

income_A_4, waste_A_4, win_A_4 = count_4(mat[0], mat[2])
income_B_4, waste_B_4, win_B_4 = count_4(mat[1], mat[2])

win_A_B_4 = if_esle(win_A_4, win_B_4)

win_C1_4 = mat[2][0] * win_A_B_4
win_C2_4 = mat[2][1] * 0
win_C_5 = if_esle(win_C1_4, win_C2_4)

header_5 = ["План", "Дохід за\n5 років", "Витрати за\n5 років", "Середній\nвиграш за\n5 років",]
data1_5 = ["Великий завод", income_A_5, waste_A_5, win_A_5]
data2_5 = ["Малий завод", income_B_5, waste_B_5, win_B_5]
print("Таблиця розрахунків для 5 років:")
table_show(header_5, data1_5, data2_5)

header_4 = ["План", "Дохід за\n4 років", "Витрати за\n4 років", "Середній\nвиграш за\n4 років",]
data1_4 = ["Великий завод", income_A_4, waste_A_4, win_A_4]
data2_4 = ["Малий завод", income_B_4, waste_B_4, win_B_4]
print("Таблиця розрахунків для 4 років:")
table_show(header_4, data1_4, data2_4)

result_header = ["Середній\nвиграш\nстратегі А", "Середній\nвиграш\nстратегі Б", "Середній\nвиграш\nстратегі В"]
data = [win_A_5, win_B_5, win_C_5]
result_table = [result_header, data]
resulr_show = tabulate(result_table , headers='firstrow', tablefmt='fancy_grid', 
                    showindex=range(1, len(result_table)), colalign=("center", "center"))
print("Таблиця середніх виграшів для всіх стратегій:")
print(resulr_show)

win_strategy = max(data)

if win_strategy == win_A_5:
    print('Переможна стратегія є стратегія A, її середній виграш:', win_strategy)
    print('Тому хорошим варіантом є будівництво великого заводу!')
elif win_strategy == win_B_5:
    print('Переможна стратегія є стратегія Б, її середній виграш:', win_strategy)
    print('Тому хорошим варіантом є будівництво малого заводу!')
elif win_strategy == win_C_5:
    print('Переможна стратегія є стратегія В, її середній виграш:', win_strategy)
    print('Тому хорошим варіантом є відкладка будівництва на рік!')