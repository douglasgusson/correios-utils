from correios import __version__
from correios.correios import (
    Servico,
    get_descricao_servico,
)

def test_get_descricao_servicos():
    assert get_descricao_servico(Servico.PAC.value) == "PAC"
    assert get_descricao_servico(Servico.SEDEX.value) == "SEDEX"
    assert get_descricao_servico(Servico.SEDEX_10.value) == "SEDEX 10"
    assert get_descricao_servico(Servico.SEDEX_12.value) == "SEDEX 12"
    assert get_descricao_servico(Servico.SEDEX_HOJE.value) == "SEDEX HOJE"

def test_get_descricao_servico_codigo_invalido():
    assert get_descricao_servico("CODIGO_INVALIDO") == "Não identificado"
