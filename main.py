class Conta(): 
	def __init__(self, num, saldo, status, limite):
		self._num = num
		self._saldo = saldo
		self._status = status
		self._limite = limite
		self._movimentacoes = []

	def get_num(self):
		return self._num

	def get_saldo(self):
		return self._saldo

	def get_status(self):
		if self._status == 's':
			return "Conta especial"  
		else:
			return "Conta comum"

	def get_limite(self):
		return self._limite 

	def get_mov(self):
		return self._movimentacoes

	def depositar(self, valor):
		if valor>0:
			print(f"R${valor:.2f} depositado(s) com sucesso!")
			self._saldo+=valor;
			self._movimentacoes.append(f"Depósito: R${valor:.2f}")
		else:
			print("Valor Inválido")

	def sacar(self, valor):
		if valor <= self._saldo:
			print(f"R${valor:.2f} sacado(s) com sucesso!")
			self._saldo-=valor
			self._movimentacoes.append(f"Saque: R${valor:.2f}")
		else:
			print("Valor excede o saldo disponível")

	def print_mov(self):
		if len(self._movimentacoes) > 0:
			print(f"Movimentações da conta")
			for i in self._movimentacoes:
				print(i)
		else:
			print("Nenhuma movimentação recente")
		

	def info(self):
		print(f"N° da conta: {self.get_num()}")
		print(f"Saldo da conta: R${(self.get_saldo()):.2f}")
		print(f"Tipo de conta: {self.get_status()}")
		print(f"Limite da conta: R${(self.get_limite()):.2f}")
		if len(self._movimentacoes) > 0:
			print(f"Movimentações da conta:")
			for i in self._movimentacoes:
				print(i)
		else:
			print("Nenhuma movimentação recente")
		

if __name__ == "__main__":
	Conta1 = Conta(423685, 43.50, 's', 5000.00)
	Conta1.info()
	Conta1.sacar(40)
	Conta1.sacar(2)
	Conta1.depositar(50)
	Conta1.print_mov()
	print()

	Conta2 = Conta(572115, 489.83, 's', 10000.00)
	Conta2.info()
	Conta2.sacar(500)
	print()

	Conta3 = Conta(9026011, 100.20, 'n', 3000.00)
	Conta3.sacar(80)
	Conta3.depositar(200)
	Conta3.info()