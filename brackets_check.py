from stack import Stack


def check_brackets(brackets: str) -> str:
  brackets_stack = Stack()
  str_ok = 'Сбалансированно'
  str_not_ok = 'Несбалансированно'

  for letter in brackets:
    if letter == '(' or letter == '[' or letter == '{':
      brackets_stack.push(letter)
    elif brackets_stack.is_empty():
      return str_not_ok
    elif letter == ')' and brackets_stack.peek() == '(':
      brackets_stack.pop()
    elif letter == ']' and brackets_stack.peek() == '[':
      brackets_stack.pop()
    elif letter == '}' and brackets_stack.peek() == '{':
      brackets_stack.pop()
    else:
      return str_not_ok
  
  if brackets_stack.is_empty():
    return str_ok
  return str_not_ok

def demo():
  demo_data = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
  ]

  for data in demo_data:
    print(check_brackets(data))

if __name__ == '__main__':
  demo()