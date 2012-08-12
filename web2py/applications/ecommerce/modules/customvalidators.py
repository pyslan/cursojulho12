# -*- coding: utf-8 -*-

# TEMPLATES
class VALIDATOR(object):
    def __init__(self, error_message="SOMETHING WRONG"):
        self.error_message = error_message

    def __call__(self, value):
    	error = None
    	# CONDITION COMES HERE
        if "ERROR":
            error = self.error_message

        # IF error != None - value is invalid 
        return (value, error)

class TRANSFORMATION(object):
	def __init__(self, search, replace):
		self.search = search
		self.replace = replace

	def __call__(self, value):
		error = None
		try:
			# TRANSFORMATION COMES HERE
			value = value.replace(self.search, self.replace)
		except:
			error = "Not possible to transform"
		return (value, error)
# / TEMPLATES
