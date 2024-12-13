'''
Создание генератора словарей: кодов ошибок и тестов
'''
nums = [101, 200, 201, 300, 303, 304, 400, 500]
results = ['Switching Protocols', 'OK', 'Created', 'Multiple Choices', 'See Other', 'Not Modified', 'Bad Request', 'Internal Server Error']

print({k: v for k, v in zip(nums, results)})
