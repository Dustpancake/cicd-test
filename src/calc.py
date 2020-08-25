

def conv(val):
	try:
		val = int(val)
	except Exception as e:
		try:
			val = float(val)
		except:
			val = str(val)
	finally:
		return val

def addn(*args):
	args = list(map(conv, args))
	if any(type(i) == str for i in args):
		return "".join(map(str, args))
	else:
		return sum(args)


if __name__ == '__main__':
	print(addn("hello", "world"))
	print(addn("hello", 1))
