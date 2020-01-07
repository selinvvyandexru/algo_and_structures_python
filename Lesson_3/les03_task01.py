""" 1. 	В диапазоне натуральных 
чисел от 2 до 99 определить,
 сколько из них кратны каждому 
 из чисел в диапазоне от 2 до 9.
 """
SEQ = []
for i in range(2, 100):
    SEQ.append(i)
# при использовании генератора pylint снижает балл
# Unnecessary use of a comprehension. Излишне сложно???
# SEQ = [i for i in range(2, 100)]
COUNT_ARRAY = [0] * 8
print(f"Число | Кол-во кратных ему"
      f"\n--------------------------")
for j in range(8):
    spam = SEQ[j]
    for item in SEQ:
        if not item % spam:
            COUNT_ARRAY[j] += 1
    print(f"{SEQ[j]:<5} |{COUNT_ARRAY[j]:^19}")
