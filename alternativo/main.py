def gerar_relatorio_por_estado(uf):
    with open('cleaneddata.txt', 'r') as arquivo:
        total_por_area = {}
        total_por_uf = {}
        for linha in arquivo:
            cidade, estado, tipo_despesa, codigo_area, valor = linha.strip().split('/')
            if estado == uf:
                if cidade not in total_por_uf:
                    total_por_uf[cidade] = 0
                if codigo_area not in total_por_area:
                    total_por_area[codigo_area] = 0
                total_por_uf[cidade] += float(valor)
                total_por_area[codigo_area] += float(valor)
        print(f'Relatório para o estado {uf}:')
        print(f'Total de gastos por cidade:')
        for cidade, total in total_por_uf.items():
            print(f'{cidade}: R${total:.2f}')
        print(f'Total de gastos por área:')
        for codigo, total in total_por_area.items():
            print(f'{codigo}: R${total:.2f}')

def gerar_relatorio_por_cidade(cidade):
    with open('cleaneddata.txt', 'r') as arquivo:
        total_por_area = {}
        total_por_cidade = {}
        for linha in arquivo:
            nome_cidade, estado, tipo_despesa, codigo_area, valor = linha.strip().split('/')
            if nome_cidade == cidade:
                if codigo_area not in total_por_area:
                    total_por_area[codigo_area] = 0
                if estado not in total_por_cidade:
                    total_por_cidade[estado] = 0
                total_por_cidade[estado] += float(valor)
                total_por_area[codigo_area] += float(valor)
        print(f'Relatório para a cidade de {cidade}:')
        print(f'Total de gastos por estado:')
        for estado, total in total_por_cidade.items():
            print(f'{estado}: R${total:.2f}')
        print(f'Total de gastos por área:')
        for codigo, total in total_por_area.items():
            print(f'{codigo}: R${total:.2f}')

escolha = input('Você deseja fazer um relatório por cidade ou por estado? [CIDADE/ESTADO]')
if escolha == 'CIDADE':
    nome = input('Digite o nome da cidade: ')
    gerar_relatorio_por_cidade(nome)
elif escolha == 'ESTADO':
    uf = input('Digite a sigla do estado: ')
    gerar_relatorio_por_estado(uf)
