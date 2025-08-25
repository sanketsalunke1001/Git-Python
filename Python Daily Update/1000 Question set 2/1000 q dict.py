
# Q651. Get value for key 'k2' in d={'k1': 2, 'k2': 3, 'k3': 4} with default 0.

# d={'k1': 2,
#    'k2': 3,
#    'k3': 4}

# value = d.get('k2', 0)
# print(value)  


#                         --------------------------------------------------------------------

# Q652. Update key 'k1' to 99 in d={'k1': 2, 'k2': 3, 'k3': 4}.


# d={'k1': 2, 'k2': 3, 'k3': 4}

# d['k1'] = 99

# print(d)


#                         --------------------------------------------------------------------

# Q653. Merge dicts d={'k1': 2, 'k2': 3, 'k3': 4} and e={'k1': 4, 'k2': 5, 'k3': 6, 'k4': 7, 'k5': 8} (Python 3.9+).

# d={'k1': 2, 'k2': 3, 'k3': 4} 
# e={'k1': 4, 'k2': 5, 'k3': 6, 'k4': 7, 'k5': 8}

# merge = dict(d) | dict(e)

# print(merge)

#                         --------------------------------------------------------------------

# Q654. Keys of d={'k1': 2, 'k2': 3, 'k3': 4}.

# d={'k1': 2, 'k2': 3, 'k3': 4}

# print(d.keys())

#                         --------------------------------------------------------------------

# Q655. Values of d={'k1': 2, 'k2': 3, 'k3': 4}.

# d={'k1': 2, 'k2': 3, 'k3': 4}

# print(d.values())

#                         --------------------------------------------------------------------

# Q656. Items of d={'k1': 2, 'k2': 3, 'k3': 4}.

# d={'k1': 2, 'k2': 3, 'k3': 4}

# print(d.items())


#                         --------------------------------------------------------------------

# Q657. Invert dict {'a':1,'b':2} (values unique).


# d = {'a': 1, 'b': 2}

# inverted = {v: k for k, v in d.items()}  

# print(inverted)

#                         --------------------------------------------------------------------

# Q658. Count frequency of elements in list [1,2,1,3,2,1] using dict.

# lst = [1,2,1,3,2,1]

# freq = {}

# for num in lst:
#     freq[num] = freq.get(num, 0) + 1

# print(freq)


#                         --------------------------------------------------------------------

# Q659. Max key by value in d={'a':3,'b':7,'c':5}.

# d={'a':3,'b':7,'c':5}

# max_key = max(d, key=d.get)

# print(max_key)


#                         --------------------------------------------------------------------

# Q660. Sort dict {'b':2,'a':3,'c':1} by value ascending (list of tuples).

# d =  {'b':2,'a':3,'c':1}

# sorted_items = sorted({'b': 2, 'a': 3, 'c': 1}.items(), key=lambda x: x[1])

# print(sorted_items)


#                         --------------------------------------------------------------------

# Q661. Get value for key 'k2' in d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6} with default 0.

# d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6}

# value = d.get('k2', 0)

# print(value)

#                         --------------------------------------------------------------------

# Q662. Update key 'k1' to 99 in d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6}.

# d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6}

# d['k1'] = 99

# print(d)

#                         --------------------------------------------------------------------

# Q663. Merge dicts d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6} and e={'k1': 5, 'k2': 6, 'k3': 7, 'k4': 8, 'k5': 9, 'k6': 10} (Python 3.9+).

# d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6}
# e={'k1': 5, 'k2': 6, 'k3': 7, 'k4': 8, 'k5': 9, 'k6': 10}

# merge = dict(d) | dict(e)

# print(merge)


#                         --------------------------------------------------------------------

# Q664. Keys of d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6}.

# d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6}

# keys = d.keys()

# print(keys)

#                         --------------------------------------------------------------------

# Q665. Values of d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6}.

# d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6}

# values = d.values()

# print(values)



#                         --------------------------------------------------------------------

# Q666. Items of d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6}.

# d={'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6}

# items = d.items()

# print(items)


#                         --------------------------------------------------------------------

# Q667. Invert dict {'a':1,'b':2} (values unique).

# d = {'a':1,'b':2}

# inverted = {v: k for k, v in d.items()}

# print("Inverted:", inverted)


#                         --------------------------------------------------------------------

# Q668. Count frequency of elements in list [1,2,1,3,2,1] using dict.

# lst = [1,2,1,3,2,1]

# freq = {}

# for x in lst:
#     freq[x] = freq.get(x, 0) + 1

# print(freq)


#                         --------------------------------------------------------------------

# Q669. Max key by value in d={'a':3,'b':7,'c':5}.

# d={'a':3,'b':7,'c':5}

# max_key = max(d, key=d.get)

# print("Key with max value:", max_key)


#                         --------------------------------------------------------------------

# Q670. Sort dict {'b':2,'a':3,'c':1} by value ascending (list of tuples).

# d = {'b':2,'a':3,'c':1}

# sorted_items = sorted(d.items(), key=lambda item: item[1])

# print("Sorted by value:", sorted_items)


#                         --------------------------------------------------------------------

# Q671. Get value for key 'k2' in d={'k1': 4, 'k2': 5, 'k3': 6, 'k4': 7, 'k5': 8} with default 0.
# Q672. Update key 'k1' to 99 in d={'k1': 4, 'k2': 5, 'k3': 6, 'k4': 7, 'k5': 8}.
# Q673. Merge dicts d={'k1': 4, 'k2': 5, 'k3': 6, 'k4': 7, 'k5': 8} and e={'k1': 6, 'k2': 7} (Python 3.9+).
# Q674. Keys of d={'k1': 4, 'k2': 5, 'k3': 6, 'k4': 7, 'k5': 8}.
# Q675. Values of d={'k1': 4, 'k2': 5, 'k3': 6, 'k4': 7, 'k5': 8}.
# Q676. Items of d={'k1': 4, 'k2': 5, 'k3': 6, 'k4': 7, 'k5': 8}.
# Q677. Invert dict {'a':1,'b':2} (values unique).
# Q678. Count frequency of elements in list [1,2,1,3,2,1] using dict.
# Q679. Max key by value in d={'a':3,'b':7,'c':5}.
# Q680. Sort dict {'b':2,'a':3,'c':1} by value ascending (list of tuples).