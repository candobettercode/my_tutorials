from opps_proj import chatbook

lst = [1, 2, 3, 4, 5]
my_str = "Hello, World!"
my_int = 42

print(type(lst))  # Output: <class 'list'>
print(type(my_str))  # Output: <class 'str'>        
print(type(my_int))  # Output: <class 'int'>

listt = [1, 2, 3, 4, 5]

#function
len_list = len(listt)
print(f"Length of the list: {len_list}")   # Output: Length of the

user1 = chatbook()
user1.send_message("Hello, how are you?")  # Assuming send_message is implemented 

# using static methods
chatbook.set_id(1001)

user1 = chatbook()
print(user1.id)



