""" 1.	В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
 """
SEQ = []
for i in range(2, 100):
    SEQ.append(i)
# при использовании генератора pylint снижает балл
# Unnecessary use of a comprehension. Излишне сложно???
# SEQ = [i for i in range(2, 100)]
COUNT_ARRAY = [0] * 13

for j in range(13):
    spam = SEQ[j]
    for item in SEQ:
        if not item % spam:
            COUNT_ARRAY[j] += 1
    print(f"{SEQ[j]:>4} {COUNT_ARRAY[j]:>4}")
