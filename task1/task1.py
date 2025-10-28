def get_users_above_18(users):
    res = []
    for user in users:
        if user['age'] > 18:
            res.append(user['name'])
    return res

# Example        
users = [
    {'name': 'Akash', 'age': 21},
    {'name': 'Anvika', 'age': 11},
    {'name': 'Anupama', 'age': 49}
]

res = get_users_above_18(users)
print(res)