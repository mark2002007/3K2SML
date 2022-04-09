import os
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Programs\MyPrograms\Python\ML\3K2SML\IT\train.csv', nrows=100000).dropna()
colNum = data.shape[1]
recNum = data.shape[0]
print(colNum)
print(recNum)

try:
    while True:
        os.system('cls')
        user_input = input('1. AllCorrelations\n2. CorrelationsWithTarget\n3. Scatter feature vs feature\n4. Bar Charts\nChoose : ')
        match user_input:
            case '1':
                print(data.corr())
                plt.matshow(data.corr())
                plt.show()
            case '2':
                
                user_input2 = input('Target Feature : ')
                if(user_input2 == '?'):
                    print(*data.columns, sep='\n')
                    user_input2 = input('Target Feature : ')
                print(data.corr()[user_input2])
                plt.bar(data.corr().index, data.corr()['RowId'])
                plt.xticks(rotation=90)
                plt.subplots_adjust(bottom=0.4)
                plt.show()
            case '3':
                while True:
                    user_input21 = input('First Feature : ')
                    if user_input21 == '?': 
                        print(*data.columns, sep='\n')
                    else:
                        break
                while True:
                    user_input22 = input('Second Feature : ')
                    if user_input22 == '?': 
                        print(*data.columns, sep='\n')
                    else:
                        break
        
                plt.scatter(data.loc[:,user_input21], data.loc[:, user_input22])
                plt.show()
            case '4':
                object_col_names = list(data.select_dtypes(include='object'))
                print('#'*50)
                print('Available features : ')
                print('#'*50)
                print(*object_col_names, sep='\n')
                print('#'*50)
                user_input2 = input('Choose : ')
                freqencies = data[user_input2].value_counts()
                plt.bar(freqencies.index, freqencies)
                plt.xticks(rotation=90)
                plt.subplots_adjust(bottom=0.35, left=0.03, right=0.995)
                plt.show()
            case '5':
                user_input2 = input('Select feature')
                print(data[user_input2])
            

        input()
except KeyboardInterrupt:
    print('\n[-] Detected Ctrl + C. Quiting...')