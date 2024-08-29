class NetworkTask13:
	""" Решение 13 задание ЕГЭ. """

	def __init__(self, *, ip:str=None, mask:str=None, net:str=None):
		self.data_input = []

		# Проврека ввода ip
		if not not ip:
			# Проверка правильного наприсания ip
			if self.validate(ip):
				self.ip = ip
				self.bin_ip = self.binary(ip)
				self.data_input.append(1)
			else:
				raise ValueError('Неверно введен ip')
		else:
			self.ip = None
			self.bin_ip = None
			self.data_input.append(0)

		# Проверка ввода mask
		if not not mask:
			# Проверка правильного наприсания mask 
			if self.validate(mask):
				self.mask = mask
				self.bin_mask = self.binary(mask)
				self.data_input.append(1)
			else:
				raise ValueError('Неверно введен mask')
		else:
			self.mask = None
			self.bin_mask = None
			self.data_input.append(0)

		# Проверка ввода net
		if not not net:
			# Проверка правильного наприсания net
			if self.validate(net):
				self.net = net
				self.bin_net = self.binary(net)
				self.data_input.append(1)
			else:
				raise ValueError('Неверно введен net')
		else:
			self.net = None
			self.bin_net = None
			self.data_input.append(0)

		# Нахождение mask по net + ip
		if self.data_input == [1, 0, 1]:
			str_ip = ''.join(self.bin_ip)
			str_net = ''.join(self.bin_net)

			def get_index() -> int:
				""" Получение индекса маски """
				for i in range(32):
					if str_ip[i] != str_net[i]:
						return i
				raise ValueError('Неверные данные для нахождения mask.')

			index_mask = get_index()

			str_mask = "0" * 32
			str_mask = "1" * index_mask * str_mask[index_mask:]

			self.bin_mask = [str_mask[i:i+8] for i in range(0, len(str_mask), 8)]

			self.mask = []
			for i in self.bin_mask:
				i = int(i, 2)
				i = str(i)
				self.mask.append(i)

		# Нахождение net по mask + ip
		if self.data_input == [1, 1, 0]:
			str_ip = ''.join(self.bin_ip)
			str_mask = ''.join(self.bin_mask)

			last_mask_index = str_mask.rfind('1')
			if last_mask_index != -1:
				str_net = str_ip[:last_mask_index + 1] + "0" * (32 - last_mask_index - 1)
				self.bin_net = [str_net[i:i+8] for i in range(0, len(str_net), 8)]

				self.net = []
				for i in self.bin_net:
					i = int(i, 2)
					i = str(i)
					self.net.append(i)

	def __str__(self):
		""" Отображение вывода print """
		return f'''\
IP:           {self.ip}
Binary IP:    {self.bin_ip}

Mask:         {self.mask}
Binary Mask:  {self.bin_mask}

NET:          {self.net}
Binary NET:   {self.bin_net}\
'''

	def validate(self, data:str) -> bool:
		""" Проверка воода """
		try:
			data = data.split('.')
			if len(data) != 4:
				return False
			for i in data:
				if not isinstance(i, str):
					continue
				if not i.isdigit() or not 0 <= int(i) <= 255:
					return False
			return True
		except ValueError or AttributeError as e:
			print(e)

	def binary(self, data:str) -> list:
		""" Перевод значений в бинарный вид """
		try:
			binary_values = []
			for i in data.split('.'):
				i = int(i)
				i = bin(i)[2:]
				i = i.zfill(8)
				binary_values.append(i)
			return binary_values
		except ValueError or AttributeError as e:
			print(e)


def main():
	''' Тестирование кода '''

	ip = '11.77.55.33'
	mask = '255.255.255.0'
	net = None

	network = NetworkTask13(ip=ip, mask=mask, net=net)

	print(network)

if __name__ == '__main__':
	main()