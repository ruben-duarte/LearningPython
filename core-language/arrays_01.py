def create_list():
    with open('expenses.txt', 'r') as f:
        content = f.read()
        expenses = content.split(' ')
        clean_data = []
    for item in expenses:
        if item == '-' :
          expenses.remove('-')

    for index in range(len(expenses)-1):
        if index%2 != 0:
            continue
        clean_data.append((expenses[index],expenses[index+1]))
    return clean_data

"1. In Feb, how many dollars you spent extra compare to January?"

data = create_list()
data_list = []
for index in range(len(data)):
    data_list.append(list(data[index]))

for index in range(len(data_list)):
      data_list[index][1] = int(data_list[index][1])

delta_febr = data_list[1][1] - data_list[0][1]
print(delta_febr)