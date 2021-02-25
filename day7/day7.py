with open("input.txt", "r") as my_file:
	listas = my_file.read().splitlines()

	
	def finding_bag_which_contains_certain_color_bag(list_of_bags):
		'''
		Returns the list of the bags which contain the bags from the given list.
		'''
		final_list_of_bags = []
		for bag in list_of_bags:
			for row_in_file in listas:
				if bag in row_in_file:
					row_split_in_words = row_in_file.split(" ")
					first_bag = row_split_in_words[0] + " " + row_split_in_words[1]
					if first_bag != bag:
						final_list_of_bags.append(first_bag)

		return final_list_of_bags

	
	def finding_certain_bags_count(main_bag):
		'''
		Counts certain bags in file. Input must be a string. 

		'''
		bag_list_with_gold_bag = 0
		progress_list = []
		final_list = []
		initial_list = []
		initial_list.append(main_bag)
		while bag_list_with_gold_bag < 8:
			new_bag_list = finding_bag_which_contains_certain_color_bag(initial_list)
			for true_bag in new_bag_list:
				if true_bag not in progress_list:
					progress_list.append(true_bag)
			initial_list = progress_list.copy()
					
			for new_bag in progress_list:
				if new_bag not in final_list:
					final_list.append(new_bag)
			bag_list_with_gold_bag += 1
			progress_list = []
		
		print(len(final_list)) 

	finding_certain_bags_count("shiny gold")

