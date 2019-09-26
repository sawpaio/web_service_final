from aiohttp import web
import json
from files.numerosromanos.source.int2roman_lucas import roman_number
from files.valida_cpf.source.validacpf_lucas import CPFvalidator
from files.distancia_entre_zeros.source.count_zeros_lucas import Count_zeros
from files.generate_passwords.source.generate_password_lucas import random_pass
from files.classificador_senhas.source.classificador_senhas_lucas import Classifica
from files.encryption_password.source.encrypto_password import crypto_pass
from jinja2 import Environment, PackageLoader, Template
import aiohttp_jinja2
import jinja2
import cgi

class Wrapper:

    @aiohttp_jinja2.template('index.html')
    async def get_main(request):
        response_obj = "Desafio - WebService"
        return {'index': response_obj}


    @aiohttp_jinja2.template('roman_ini.html')
    async def get_roman_ini(request):
        response_obj = "Conversor de inteiros para Números Romanos."
        return {'index': response_obj}

    @aiohttp_jinja2.template('roman_final.html')
    async def get_roman_final(request):
        number = request.match_info.get('number')
        resposta = roman_number.keyboard2roman(number)
        return {'result': resposta}
    
    @aiohttp_jinja2.template('cpf_ini.html')
    async def get_cpf_ini(request):
        response_obj = "Validador de CPF"
        return {'index': response_obj}

    @aiohttp_jinja2.template('cpf_final.html')
    async def get_cpf_final(request):
        number = request.match_info.get('number')
        response_obj = CPFvalidator.valida_cpf(number)
        return {'result': response_obj}

    @aiohttp_jinja2.template('zeros_ini.html')
    async def get_zeros_ini(request):
        response_obj = "Contagem de Sequência de Zeros"
        return {'index': response_obj}

    @aiohttp_jinja2.template('zeros_final.html')
    async def get_zeros_final(request):
        number = request.match_info.get('number')
        response_obj = Count_zeros.zeros_count(number)
        return {'result': response_obj}

    @aiohttp_jinja2.template('get_senhas.html')
    async def get_senhas(request):
        response_obj = random_pass()
        final1 = "Senha gerada: {}".format(response_obj)
        classificador = Classifica.classifica_senha(response_obj)
        final2 = "Classificação da senha: {}".format(classificador)

        return {'index': final1, 'result': final2}

app = web.Application()
aiohttp_jinja2.setup(app, loader= jinja2.FileSystemLoader('/home/semantix/workspace/desafiosTakeshi/http_takeshi/templates'))
app.router.add_get("/", Wrapper.get_main)
app.router.add_get('/roman/', Wrapper.get_roman_ini)
app.router.add_get('/roman/{number}', Wrapper.get_roman_final)
app.router.add_get('/cpf/', Wrapper.get_cpf_ini)
app.router.add_get('/cpf/{number}', Wrapper.get_cpf_final)
app.router.add_get('/zeros/', Wrapper.get_zeros_ini)
app.router.add_get("/zeros/{number}", Wrapper.get_zeros_final)
app.router.add_get("/senha/", Wrapper.get_senhas)
web.run_app(app, host='localhost', port=7777)

