with open("input.txt", "r") as my_file:

	listas = my_file.read().splitlines()
	nulinis_didziausias_narys = []
	list_with_places = []

	def place_from_barcode(barcode):
		eiles = list(range(0, 128))
		vietos = list(range(0, 8))

		for raide in barcode[0:7]:
			if raide == "F":
				eiles = eiles[:len(eiles)//2]
								
			if raide == "B":
				eiles = eiles[len(eiles)//2:]
				
		for raide in barcode[7:10]:		
			if raide == "L":
				vietos = vietos[:len(vietos)//2]
								
			if raide == "R":
				vietos = vietos[len(vietos)//2:]

		return eiles[0], vietos[0]

	def max_id(list_of_barcodes):
		for eilute in list_of_barcodes:
			row_and_place = place_from_barcode(eilute)
			vietos_id = int(row_and_place[0]) * 8 + int(row_and_place[1])
			nulinis_didziausias_narys.append(vietos_id)
		max_value = max(nulinis_didziausias_narys)
		return max_value

	
	def empty_generated_grid(rows, columns):
		gridas = [[0 for dummy_col in range(0, columns)]
							for dummy_row in range(0, rows)]
	
		return gridas
	
	def list_of_places(list_of_barcodes):
		empty_grid = empty_generated_grid(128, 8)
		for eilute in list_of_barcodes:
			row_and_place = place_from_barcode(eilute)
			empty_grid[row_and_place[0]][row_and_place[1]] = "X"	
		return empty_grid

	def finding_empty_place():
		line_index = 0
		column_index = 0
		full_grid = list_of_places(listas)
		for line in full_grid:
			if line.count(0) == 1:
				epmty_place = line.index(0)
				print("Row: " + str(line_index)+ " Place: " + str(epmty_place))
				break
			line_index += 1

	finding_empty_place()
