# Напишите декоратор obfuscator
def obfuscator(func):
    def wrapper():
        dct = func()
        
        name = dct['name']
        password = dct['password']
        
        dct['name'] = (
            name[0] + 
            ('*' * (len(name) - 2) ) + 
            name[-1])
        
        dct['password'] ='*' * len(password)
        
        return dct
    return wrapper




@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())