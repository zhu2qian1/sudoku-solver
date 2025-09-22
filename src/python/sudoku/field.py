class Field:
	def __init__(self, field: list[list[int]]=None):
		if not field:
			raise ValueError("Field cannot be empty")
		if len(field) != 9 or any(len(row) != 9 for row in field):
			raise ValueError("Field must be a 9x9 grid")
		for row in field:
			for cell in row:
				if not (0 <= cell <= 9):
					raise ValueError("Cell values must be between 0 and 9, where 0 represents an empty cell")
		self.field = field

	def __str__(self):
		lines = []
		for i, row in enumerate(self.field):
			if i % 3 == 0 and i != 0:
				lines.append("- - - + - - - + - - -")
			line = []
			for j, cell in enumerate(row):
				if j % 3 == 0 and j != 0:
					line.append("|")
				line.append(str(cell) if cell != 0 else "_")
			lines.append(" ".join(line))
		return "\n".join(lines)

	def is_solved(self) -> bool:
		for row in self.field:
			if any(cell == 0 for cell in row):
				return False
		# row check
		if len(set(row)) != 9:
			return False
		# column check
		for col in range(9):
			if len(set(self.field[r][col] for r in range(9))) != 9:
				return False
		# 3x3 box check
		for box_row in range(3):
			for box_col in range(3):
				box = set()
				for r in range(box_row * 3, box_row * 3 + 3):
					for c in range(box_col * 3, box_col * 3 + 3):
						box.add(self.field[r][c])
				if len(box) != 9:
					return False
		return True
