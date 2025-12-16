# from sklearn.metrics.pairwise import cosine_distances
# X = [[1, 1, 1], [1, 1, 1]]
# Y = [[1, 1, 1], [1, 1, 0]]
# cosindist = cosine_distances(X, Y)
# print(cosindist)

from generic_tools import *

ref = "Saint—Brupçue"
user= input("entre un mot :")

cosinedistance = get_distances(ref,user)

print(cosinedistance)