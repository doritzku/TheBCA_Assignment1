precedence = {9: ["**"], 8: ["~"], 7: ["*", "/", "%", "//"], 6: ["+", "-"], 5: [">>", ">>"]
	, 4: ["&"], 3: ["^", "|"],
	          2: ["<", "<=", "==", ">=", ">", "!="], 1: ["and", "or", "not"]}


def find_precedence(symbol):
	for key, operators in precedence.items():
		if symbol in operators:
			return key
	else:
		print("Operator not found in precedence dictionary.")
		print("Exiting...")
		exit(0)


def postfix(ex):
	s = []
	stack = []
	for i in ex:
		if i.isalpha() or i.isalnum():
			s.append(i)
		else:
			p = find_precedence(i)
			if len(stack) == 0:
				stack.append([i, p])
			else:
				if p < stack[-1][1]:
					s.append(stack.pop()[0])
					stack.append([i, p])
				else:
					while len(stack) > 0 and p > stack[-1][1]:
						stack.append([i, p])
						break
	str1 = ""
	for i in stack[1::-1]:
		s.append(i[0])
	return str1.join(s)


def prefix(ex):
	s = []
	stack = []
	for i in ex[::-1]:
		if i.isalpha() or i.isalnum():
			s.append(i)
			# print(s)
		else:
			p = find_precedence(i)
			if len(stack) == 0:
				stack.append([i, p])
			else:
				if p < stack[-1][1]:
					s.append(stack.pop()[0])
					stack.append([i, p])
				else:
					while len(stack) > 0 and p > stack[-1][1]:
						stack.append([i, p])
						# print(stack)
						break
	str1 = ""
	for i in stack[::-1]:
		s.append(i[0])
	# s.append(stack[::-1][0])
	return str1.join(s)


# ex = input("Enter the expression: ")
ex = "a*b+c*d"
if ex.isalnum() or ex.isalpha() or ex.isdigit():
	print("Postfix: ", ex)
	print("Prefix: ", ex)
else:
	postfix = postfix(ex)
	print("Postfix: ", postfix)
	prefix = prefix(ex)
	print("Prefix: ", prefix[::-1])