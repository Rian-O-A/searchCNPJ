
# CNPJ Quick Search

Este é um script Python para realizar uma pesquisa rápida de CNPJ. Ele utiliza a biblioteca argparse para processar argumentos de linha de comando e permite especificar o CNPJ desejado, o número da página e o caminho para salvar o arquivo JSON.

## Pré-requisitos
Certifique-se de que você tenha Python instalado no seu sistema. Além disso, você pode precisar instalar algumas dependências. 

**Você pode instalá-las executando:**
    ```bash
        pip install -r requirements.txt

## Uso
Execute o script a partir da linha de comando, fornecendo os argumentos necessários. Abaixo estão os argumentos suportados:

- **search:** CNPJ desejado para pesquisa.
- **page:** Número da página a ser consultada.
- **path:** Caminho para salvar o arquivo JSON com os resultados da pesquisa.

**Exemplo de Uso**
    ```bash
    python script.py -search 12345678901234 -page 1 -path /caminho/para salvar/resultado.json

- **Nota:** O argumento -path é obrigatório. Certifique-se de fornecê-lo ao executar o script.

## Contribuição
Sinta-se à vontade para contribuir para este projeto. Se você encontrar problemas ou tiver sugestões de melhorias, por favor, abra uma issue ou envie um pull request.

## Licença
Este projeto é licenciado sob a MIT License.