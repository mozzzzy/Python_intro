import random

#0.0~1.0までのfloat値を返す
print random.random()

#0.0から100.0までのfloat値を返す
print random.uniform(0,100)

#0から100までのint値を返す
print random.randint(0,100)

#パラメータ内の1文字を返す
print random.choice('1234567890abcdefghij')

#リストの順序をシャッフルする
sample_list = ['python','random','test']
random.shuffle(sample_list)
print sample_list
