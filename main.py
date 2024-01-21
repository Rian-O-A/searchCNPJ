def main():
    
    from app.controller import start
    import argparse
    # Criação do parser e definição dos argumentos
    parser = argparse.ArgumentParser(description='Pesquisa rapida de cnpj')
    
    # Adiciona o argumento -page
    parser.add_argument('-page', type=int, help='Número da página')

    # Adiciona o argumento -path
    parser.add_argument('-path', type=str, help='Caminho para salvar o arquivo json')

    # Faz o parsing dos argumentos
    args = parser.parse_args()

    # Verifica se os argumentos foram fornecidos
    if args.page is None:
        parser.error('O argumento -page é necessário.')

    # Agora você pode acessar os valores dos argumentos
    pages = args.page
    path = args.path

    
    
    start(pages=pages, path=path)

if __name__ == '__main__':
    main()