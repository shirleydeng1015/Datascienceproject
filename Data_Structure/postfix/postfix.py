import operator
from pythonds.basic.stack import Stack
'''THis is a postfix operation, for inputs like '4 5 /',
do calculations on input as '4/5', and return outputs.
'''
file = open("input.txt","r")

newlist = list(file.readlines(0))

def is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False


def postfixEval(postfixExpr):
	operandStack = Stack()
	tokenList = postfixExpr.split()

	for token in tokenList:
		#print(token + ', size: ' + str(operandStack.size()))
		if is_int(token):
			operandStack.push(int(token))
		else:
			operand2 = operandStack.pop()
			operand1 = operandStack.pop()
			result = doMath(token,operand1,operand2)
			operandStack.push(result)

	if(operandStack.size() == 0):
		return None
	else:
		return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return operator.mul(op1, op2)
    elif op == "/":
        return operator.truediv(op1, op2)
    elif op == "+":
        return operator.add(op1, op2)
    else:
        return operator.sub(op1, op2)

newfile = open('output.txt', 'w')
for i in range(0, len(newlist)):
    postfixExpr = newlist[i]
    # print(postfixExpr)
    # print(postfixEval(postfixExpr))
    output = str(postfixEval(postfixExpr)) + '\n'

    # newfile.write(str(postfixEval(postfixExpr)))
    i += 1
    print(output)
    newfile.write(output)
# print(newlist[2])
# # print(postfixEval(newlist[0]))
# # print(postfixEval(newlist[1]))
# print(postfixEval(newlist[2]))


# postfixEval('3 2 8 4 6 / 6 * * 3 4 / 5 * + + 5 - 2 * 10 + +')
