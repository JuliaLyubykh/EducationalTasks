def delete_imports(code, language):
    if language == 'Python':
        return code.replace('import ', '')
    elif language == 'SQL':
        return code
    elif language == 'C++':
        return code.replace('#include ', '')
    else:
        return code
    

def delete_commands(code, language):
    if language == 'Python':
        return code.replace('eval', '').replace('exec', '')
    elif language == 'SQL':
        return code.replace('drop', '').replace('delete', '')
    else:
        return code
    

def delete_comments(code, language):
    if language == 'SQL':
        return code.replace('--', '')
    else:
        return code
    

def cleaner(code, language):
    code = delete_imports(code, language)
    code = delete_commands(code, language)
    code = delete_comments(code, language)
    return code


mycode = """
import os, sys

a = 1
eval(a)
"""
mylanguage = 'Python'

print(cleaner(mycode, mylanguage))
