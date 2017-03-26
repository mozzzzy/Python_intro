#coding:utf-8
import Mystack2

Mystack2.newStack('stack1')
Mystack2.newStack('stack2')

Mystack2.push('stack1',1)
Mystack2.push('stack1',2)
Mystack2.push('stack1',3)

print Mystack2.top('stack1')
Mystack2.pop('stack1')
print Mystack2.top('stack1')
Mystack2.pop('stack1')
print Mystack2.top('stack1')
Mystack2.pop('stack1')
