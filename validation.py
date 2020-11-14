#a form validation algorithm

class Validation(object) :
	def __init__ (self, password = '')  :
		self.password = password

	def lower (self) :
		lower = any(c.islower() for c in self.password)
		return lower

	def upper (self) :
		upper = any(c.isupper() for c in self.password)
		return upper

	def digit (self) :
		digit = any (c.isdigit()for c in self.password)
		return digit

	def authenticate (self) :
		lower = self.lower()
		upper = self.upper()
		digit = self.digit()

		length = len(self.password)

		report = lower and upper and digit and length>= 8

		if report :
			print('Valid password')
			return True

		elif not lower:
			print('Password must contain a lower case character')
			return False
			quit()


		elif not upper:
			print('Password must contain a upper case character')
			return False
			quit()

		elif not digit:
			print('Password must contain a digit character')
			quit()

		elif len(self.password) < 8:
			print('Password must contain at least 6 characters ')
			quit()

		else :
			pass


class Authentication(object) :
	def __init__ (self, user = '')  :
		self.user = user

	def lower (self) :
		lower = any(c.islower() for c in self.user)
		return lower

	def upper (self) :
		upper = any(c.isupper() for c in self.user)
		return upper

	def validate(self) :
		lower = self.lower()
		upper = self.upper()

		length = len(self.user)

		result = lower and upper and length >= 8

		if result :
			print('Valid username')
			return True

		elif not lower:
			print('Username must contain a lower case character')
			quit()
			return False

		elif not upper:
			print('Username must contain a upper case character')
			quit()
			return False

		elif len(self.user) < 8:
			print('Username must contain at least 6 characters ')
			quit()
			
		else :
			pass












	

			










