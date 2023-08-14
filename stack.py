from __future__ import annotations
from typing import Any


class StackElement:
  data: Any
  next: StackElement | None

  def __init__(self, data: Any, next: StackElement | None = None) -> None:
    self.data = data
    self.next = next

class Stack:
  _head: StackElement | None

  def __init__(self) -> None:
    self._head = None

  def __str__(self) -> str:
    cur = self._head
    string = ''
    while cur:
      string += str(cur.data)
      if cur.next:
        string += ' --> '
      cur = cur.next
    return string

  def is_empty(self) -> bool:
    if self._head:
      return False
    return True

  def push(self, data: Any) -> None:
    if self._head:
      new_elem = StackElement(data, self._head)
      self._head = new_elem
    else:
      self._head = StackElement(data)

  def pop(self) -> Any:
    if self._head:
      elem_data = self._head.data
      self._head = self._head.next
      return elem_data
    raise Exception('stack is empty')
  
  def peek(self) -> Any:
    if self._head:
      return self._head.data
    raise Exception('stack is empty')
  
  def size(self) -> int:
    len = 0
    cur = self._head
    while cur:
      len += 1
      cur = cur.next
    return len