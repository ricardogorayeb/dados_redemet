import requests
import datetime
import string

def retorna_dados_estacao():
    dt = datetime.datetime.utcnow()
    hora = dt.hour
    minuto = dt.minute
    dia = dt.day
    mes = dt.strftime("%m")
    ano = dt.year
    api_key = 'v12b8I5cjvVF5d3d73Jlw9R30BeNMWD0rh4kT4OZ'
    localidade = 'SBEG'
    response = requests.get('https://api-redemet.decea.gov.br/aerodromos/info?api_key={}&localidade={}&datahora={}{}{}{}'.format(api_key, localidade, ano, mes, dia, hora))
    response2 = requests.get('https://api-redemet.decea.gov.br/mensagens/meteograma/{}?api_key={}&data_hora={}{}{}{}&horas=00'.format(localidade, api_key, ano, mes, dia, hora))
    print(response.json())
    print(response2.json())
    dados_estacao = response.json()
    dados_estacao = dados_estacao['data']
    dados_estacao2 = response2.json()
    dados_estacao2 = dados_estacao2['data']
    #print(type(dados_estacao))
    #print('Temperatura em Eduardo Gomes: {}'.format(dados_estacao['temperatura']))
    temperatura = dados_estacao['temperatura']
    ur = dados_estacao['ur']
    vnt_dir = dados_estacao2['vnt_dir']
    vnt_vel = dados_estacao2['vnt_vel']
    qnh = dados_estacao2['qnh']
    punc = '''!()-[]{};:'"\, <>.?@[]#ºC$%^&*_~'''
    for ele in temperatura:
        if ele in punc:
            temperatura = temperatura.replace(ele,"")

    for ele in ur:
        if ele in punc:
            ur = ur.replace(ele,"")

    #print('Umidade Relativa em Eduardo Gomes: {}'.format(dados_estacao['ur']))
    #print('Direcao do Vento em Eduardo Gomes: {}'.format(dados_estacao2['vnt_dir']))
    #print('Velocidade do Vento em Eduardo Gomes: {}'.format(dados_estacao2['vnt_vel']))
    #print('Direcao do Vento em Eduardo Gomes: {}'.format(dados_estacao2['vnt_dir']))
    #print('Pressao Atmosferica em Eduardo Gomes: {}'.format(dados_estacao2['qnh']))
    #arquivo = open('/EMS/scripts/inmet/arquivos/{}_{}{}{}_{}.txt'.format(localidade, ano, mes, dia, hora), 'w')
    arquivo = open('/tmp/{}_{}{}{}_{}.txt'.format(localidade, ano, mes, dia, hora), 'w')
    arquivo.write('SBEG {} {} {} {} //// //// {} //// //// {} //// //// //// //// //// {} //// //// {} {} //// //// //// / //// //// //// ='.
                  format(ano, mes, dia, hora, temperatura, ur, qnh[0],
                         vnt_vel[0], vnt_dir[0]))
    arquivo.close()
    #subprocess.call(["sed -i 's/ºC/''/g' /tmp/SBEG_20200915_15.txt"], shell=True)
    #subprocess.call(["sed -i 's/\'[/''/g'"], shell=True)
    #return(dados_estacao)

if __name__ == '__main__':
    retorna_dados_estacao()

