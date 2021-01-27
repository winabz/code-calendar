import string

with open("input.txt", "r") as my_file:
	
	def counting_yes_answers(my_file):
		listas = my_file.read().splitlines()
		empty_list = []
		first_member = True
		sum_yes = 0
		for person in listas:
			if person:
				if first_member == True:
					full_list = list(string.ascii_lowercase)
					for question in person:
						empty_list.append(question)
					same_values_in_set = set(full_list).intersection(set(empty_list))
					empty_list = []	
					first_member = False
				else:
					for question in person:
						empty_list.append(question)
					same_values_in_set = set(same_values_in_set).intersection(set(empty_list))
					empty_list = []	
			else:
				sum_yes += len(same_values_in_set)
				same_values_in_set = ()
				first_member = True
		sum_yes += len(same_values_in_set)
		print(sum_yes)

	counting_yes_answers(my_file)

	