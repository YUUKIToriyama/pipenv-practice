import pandas as pd

csv = pd.read_csv("~/デスクトップ/kyoto.test.csv", names = ['氏名', '郵便番号', '住所', '電話番号'])
#print(csv)

name = csv['氏名'].str.split('　', expand=True)
name.rename(columns={0: '苗字', 1: '名前'}, inplace=True)

print(name)
csv = pd.concat([name, csv], axis=1)
print(csv)