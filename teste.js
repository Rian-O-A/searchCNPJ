const fetch = require('node-fetch');
const fs = require('fs');

const numPage = 1;
const url = 'https://api.casadosdados.com.br/v2/public/cnpj/search';

// Headers for the request
const headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Origin': 'https://casadosdados.com.br',
  'Referer': 'https://casadosdados.com.br/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
};

// Data to be sent in the request body
const packetCNPJ = [];
for (let x = 1; x <= numPage; x++) {
  console.log(x);
  const data = {
    query: {
      termo: [],
      atividade_principal: [],
      natureza_juridica: [],
      uf: [],
      municipio: [],
      bairro: [],
      situacao_cadastral: 'ATIVA',
      cep: [],
      ddd: [],
    },
    range_query: {
      data_abertura: { lte: null, gte: null },
      capital_social: { lte: null, gte: null },
    },
    extras: {
      somente_mei: false,
      excluir_mei: false,
      com_email: false,
      incluir_atividade_secundaria: false,
      com_contato_telefonico: false,
      somente_fixo: false,
      somente_celular: false,
      somente_matriz: false,
      somente_filial: false,
    },
    page: x,
  };

  // Make the POST request
fetch(url, {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(data),
  })
    .then((response) => {
      // Check if the request was successful (status code 200)
      if (response.ok) {
        // Convert the response to JSON and process it
        return response.json();
      } else {
        throw new Error(`Error in request. Status code: ${response.status}`);
      }
    })
    .then((jsonResponse) => {
      packetCNPJ.push(...jsonResponse.data.cnpj);
    })
    .catch((error) => {
      console.error(error.message);
    });
}

console.log(packetCNPJ.length);
fs.writeFileSync('packetCNPJ.json', JSON.stringify(packetCNPJ, null, 6), 'utf-8');
