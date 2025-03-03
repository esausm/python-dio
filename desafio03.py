import textwrap

class Banco:
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.usuarios = []
        self.contas = []
    
    def menu(self):
        opcoes = """
        ================ MENU ================
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q] Sair
        => """
        return input(textwrap.dedent(opcoes))
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:	R$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:		R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:		R$ {self.saldo:.2f}")
        print("==========================================")
    
    def criar_usuario(self):
        cpf = input("Informe o CPF (somente número): ")
        if self.filtrar_usuario(cpf):
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        self.usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("=== Usuário criado com sucesso! ===")
    
    def filtrar_usuario(self, cpf):
        return next((usuario for usuario in self.usuarios if usuario["cpf"] == cpf), None)
    
    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)
        if usuario:
            conta = {"agencia": self.AGENCIA, "numero_conta": len(self.contas) + 1, "usuario": usuario}
            self.contas.append(conta)
            print("\n=== Conta criada com sucesso! ===")
        else:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    
    def listar_contas(self):
        for conta in self.contas:
            print("=" * 100)
            print(textwrap.dedent(f"""
                Agência:	{conta['agencia']}
                C/C:		{conta['numero_conta']}
                Titular:	{conta['usuario']['nome']}
            """))
    
    def executar(self):
        while True:
            opcao = self.menu()
            if opcao == "d":
                self.depositar(float(input("Informe o valor do depósito: ")))
            elif opcao == "s":
                self.sacar(float(input("Informe o valor do saque: ")))
            elif opcao == "e":
                self.exibir_extrato()
            elif opcao == "nu":
                self.criar_usuario()
            elif opcao == "nc":
                self.criar_conta()
            elif opcao == "lc":
                self.listar_contas()
            elif opcao == "q":
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    Banco().executar()

