"""Solution for Advent of Code - Day 1"""
from collections import Counter

def parse_input(input_data):
    list1 = []
    list2 = []

    for line in input_data.strip().split("\n"):
        left, right = map(int,line.split())
        list1.append(left)
        list2.append(right)
    return list1, list2

def calculateDistance(left,right):
    left.sort();
    right.sort();
    sums = sum(abs(left[i] - right[i]) for i in range(len(left)))    
    return sums

def solve_part_1(input_data):
    left_list, right_list = parse_input(input_data)
    return calculateDistance(left_list,right_list)



## PART 2 OF QUESTION   

def makeList2Map(right):
    counts = Counter(right);
    return counts

def calculateSimilarity(left,count):
    totalSum = 0
    for i in range(len(left)):
        occurence = count.get(left[i],0)
        if occurence == 0:
            totalSum += 0
        else:
            totalSum += left[i] * occurence
    return totalSum


def solve_part_2(input_data):
    left_list, right_list = parse_input(input_data)
    count = makeList2Map(right_list)
    return calculateSimilarity(left_list,count)
