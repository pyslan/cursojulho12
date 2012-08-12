# -*- coding: utf-8 -*-


# http://rochacbruno.com.br/custom-validator-for-web2py-forms/


class IS_VALID_BARCODE(object):
    def __init__(self, start_with="", error_message="INVALID BARCODE"):
        self.error_message = error_message
        self.start_with = start_with

    def __call__(self, value):
        error = None
        if not value.startswith(self.start_with):
            return (value, self.error_message)
        else:
            return (value, None)




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
