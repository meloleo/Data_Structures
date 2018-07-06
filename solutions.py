#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:49:20 2018

@author: leoshen
"""

import string

print "------------------- Question 1 -------------------"

def question1(s, t):
    
    if not isinstance(t, str) or not isinstance(s, str):
        return False
    
    s = s.lower().replace(" ", "").translate(None, string.punctuation)
    t = t.lower().replace(" ", "").translate(None, string.punctuation)

    t_list = dict()
    s_list = dict()
    
    for i in t:
        t_list[i] = t_list.get(i, 0) + 1
    
    for i in range(0, len(s)):
        sliced_window = s[i:i+len(t)]
        for j in sliced_window:
            s_list[j] = s_list.get(j, 0) + 1
        if s_list == t_list:
            return True
        else:
            s_list = dict()
    
    return False


# Should return True
print "Example 1:", question1("udacity", "da")

# Should return True
print "Example 2:", question1("Alec Guinness", "Genuine Class")

# Should return False
print "Example 3:", question1("ELVIS", "sel")


print "------------------- Question 2 -------------------"

def question2(a):
    if not isinstance(a, str):
        return None
    
    s = a.lower().replace(" ", "").translate(None, string.punctuation)
    
    palindrome = ""
    
    for i in range(len(s)):
        for j in range(0, i):
            substring = s[j:i + 1]
            if substring == substring[::-1]:
                if len(substring) > len(palindrome):
                    palindrome = substring
    return palindrome

# Should return "454"
print "Example 1:", question2("12345421")

# Should return None
print "Example 2:", question2(None)

# Should return "amymustijujitsumyma"
print "Example 3:", question2("Amy, must I jujitsu my ma?")

print "------------------- Question 3 -------------------"

def question3(G):

    parent = dict()
    rank = dict()
        
    for node in G.keys():
        #print node
        parent[node] = node
        rank[node] = 0

#1. Sort all the edges in non-decreasing order of their weight.
    edge_list = []
    
    for node, edge in G.items():
        for dest, wt in edge:
            sort = []
            sort.extend([node, dest, wt])
            edge_list.append(sort)
    edge_list = sorted(edge_list, key=lambda e: e[2])
    
# 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. 
# If cycle is not formed, include this edge. Else, discard it.
    
    def find(node):
        if parent[node] == node:
            return node
        return find(parent[node])
 
    def union(node1, node2):
        p1 = find(node1)
        p2 = find(node2)
        if p1 != p2:
            if rank[p1] > rank[p2]: 
                parent[p2] = p1 # parent becomes whichever node with higher rank
            elif rank[p1] < rank[p2]: 
                parent[p1] = p2
            elif rank[p1] == rank[p2]:
                parent[p2] = p1
                rank[p2] += 1 # p2 rank increases by one if both ranks equal
                

    #3. Repeat step 2 until there are (V-1) edges in the spanning tree.
    adj_list = []
    e = 0

    while e < (len(parent) - 1):
        for edges in edge_list:
            p1 = find(edges[0])
            p2 = find(edges[1])
            if p1 != p2:
                union(p1, p2)
                adj_list.append(edges)
                e += 1 
    
    result = dict()
    
    for node, dest, wt in adj_list:
        result[node] = [(dest, wt)]
    return result

# Should return: {'A': [('B', 2)], 
#                    'C': [('D', 1)], 
#                    'B': [('D', 3)]}
print "Example 1:\n", question3({'A': [('B', 2)],
 'B': [('A', 2), ('C', 5), ('D', 3)],  
 'C': [('B', 5), ('D' , 1)],
 'D': [('B', 3)]})

# Should return: {'A': [('B', 2)], 
#                    'C': [('B', 5)]}
print "Example 2:\n", question3({'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]})

# Should return: {'A': [('B', 2)], 
#                    'C': [('D', 1)], 
#                    'B': [('D', 3)]}
print "Example 3:\n", question3({'A': [('B', 2)],
 'B': [('A', 2), ('C', 5), ('D', 3)],  
 'C': [('B', 5), ('D' , 1)],
 'D': [('B', 3), ('C' , 1)]})

print "------------------- Question 4 -------------------"

def question4(T, r, n1, n2):
    #T = tree matrix
    #r = root
    #n1 = node1 i.e. index of rows
    #n2 = node2
    # Goal: find least common ancestor of n1 and n2

    ancestor = r
    choices = []
    while r != None:    
        for i in range(len(T)):
            if T[ancestor][i] == 1:
                choices.append(i)
        if (n1 < ancestor) and (n2 < ancestor):
#            print "going left", n1, n2, "<", ancestor 
            ancestor = choices[0]
#            print "new ancs:", ancestor
            choices = []
        elif (n1 >= ancestor) and (n2 >= ancestor):
#            print "going right", n1, n2, ">=", ancestor 
            ancestor = choices[1]
#            print "new ancs:", ancestor
            choices = []
        else:
#            print "at root"
            return ancestor
        
    return None
                            

# Should return 3
print "Example 1:\n", question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          4,
          1)

# Should return 2: going left
print "Example 2:\n", question4([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0]],
          3,
          1,
          2)

# Should return 5: going right
print "Example 3:\n", question4([[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0]],
          2,
          3,
          6)

print "------------------- Question 5 -------------------"


# Creation of nodes and linkedlist functions for Q5
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    

def question5(ll, m):
    if m < 1:
        return None # Return None if m is negative or 0
    
# Goal: find node.data of position m of linked list
# where m = mth number from end. Slice?
    linklist_length = 1
    current = ll #ll is first node in linked list
    
    while current.next:
        current = current.next
        linklist_length += 1
    
    current = ll
    reverse_position = linklist_length - m #mth number from the end
    counter = 0

# reiterate through linkedlist to find position from end
    while counter <= reverse_position:
        if counter == reverse_position:
            return current.data
        current = current.next
        counter += 1
    return None



example1 = LinkedList(Node(1))
example1.append(Node(2))
example1.append(Node(3))
example1.append(Node(10))

# Should return None (0 numbers from the end doesn't exist)
print "Example 1:", question5(example1.head, 0)
    

example2 = LinkedList(Node(2))
example2.append(Node(5))
example2.append(Node(3))
example2.append(Node(20))

# Should return 3
print "Example 2:", question5(example2.head, 2)

example3 = LinkedList(Node(2))
example3.append(Node(5))
example3.append(Node(3))
example3.append(Node(20))
example3.append(Node(7))
example3.append(Node(100))

# Should return 100
print "Example 3:", question5(example3.head, 1)