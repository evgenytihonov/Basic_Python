src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 2, 2, 34523452343, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2,
       2, 2, 7, 23, 1, 232356, 44, 44, 3, 2, 10, 7, 4, 11,2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 45643, 2,
       2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 2, 7, 23, 1,
       44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 2, 2, 2, 7, 35545, 23, 1, 44, 44, 3, 2,
       10, 7, 4, 11, 2, 2, 2, 7, 23, 4523452, 1, 44, 44, 3, 2, 10, 7, 4, 11, 10, 7, 4, 11]

srs = [i for i in src if src.count(i) == 1]

print(srs)
