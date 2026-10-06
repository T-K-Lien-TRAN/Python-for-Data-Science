ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# list
try:
    ft_list.append("World!")
except Exception as e:
    print(f"Issue with list!, {e}") 

# tuple
try:
    ft_tuple = ft_tuple[:1] + ("France!",)
except Exception as e:
    print(f"Issue with tuple!, {e}")

# set
try:
    ft_set.remove("tutu!")
    ft_set.add("Nice!")
except Exception as e:
    print(f"Issue with set!, {e}")

# dict
try:
    ft_dict["Hello"] = "42Nice!"
except Exception as e:
    print(f"Issue with dict!, {e}")

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
