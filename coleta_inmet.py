import requests

def convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    print(res_dct)
    return res_dct

def retorna_dados_estacao():
    response = requests.get('https://api-redemet.decea.gov.br/aerodromos/info?api_key=v12b8I5cjvVF5d3d73Jlw9R30BeNMWD0rh4kT4OZ&localidade=SBEG&datahora=2020091100')
    #print(response.status_code)
    #print(response.__dict__)
    print(response.json())
    #print(type(response.json()))
    dados_estacao = response.json()
    dados_estacao = dados_estacao['data']
    print(type(dados_estacao))
    print(dados_estacao['temperatura'])
    print(dados_estacao['ur'])
    #print(dados_cep['complemento'])
    #return(dados_estacao)

def retorna_dados_pokemon(pokemon):
    response = requests.get('http://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    retorna_dados_estacao()
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny'])
    #response = retorna_response('https://www.uol.com.br/')
    #print(response)