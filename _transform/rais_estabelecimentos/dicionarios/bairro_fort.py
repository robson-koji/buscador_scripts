# -*- coding: utf8 -*-


def bairro_fort_dic():
    bairros = {
        "0001": "Alagadiço",
        "0002": "Alagadiço Novo",
        "0003": "Aldeota",
        "0004": "Alto Alegre",
        "0005": "Alto da Balança",
        "0006": "Alvaro Weyne",
        "0007": "Amadeu Furtado",
        "0008": "Antonio Bezerra",
        "0009": "Antonio Diogo",
        "0010": "Barra do Ceara",
        "0011": "Bela Vista",
        "0012": "Benfica",
        "0013": "Bom Futuro",
        "0014": "Bom Jardim",
        "0015": "Bonsucesso",
        "0016": "Cachoeirinha",
        "0017": "Cajazeiras",
        "0018": "Cambeba",
        "0019": "Castelao",
        "0020": "Centro",
        "0021": "Cidade dos Funcionari",
        "0022": "Coco",
        "0023": "Conjunto Ceara",
        "0024": "Conjunto Esperança",
        "0025": "Cristo Redentor",
        "0026": "Damas",
        "0027": "Democrito Rocha",
        "0028": "Dias Macedo",
        "0029": "Dionisio Torres",
        "0030": "Edson Queiroz",
        "0031": "Farias Brito",
        "0032": "Fatima",
        "0033": "Genibau",
        "0034": "Granja Portugal",
        "0035": "Henrique Jorge",
        "0036": "Itaperi",
        "0037": "Jacarecanga",
        "0038": "Jangurussu",
        "0039": "Jardim America",
        "0040": "Joaquim Tavora",
        "0041": "Joquei Clube",
        "0042": "Jose Bonifacio",
        "0043": "Lagoa Redonda",
        "0044": "Manuel Satiro",
        "0045": "Maraponga",
        "0046": "Meireles",
        "0047": "Messejana",
        "0048": "Mondubim",
        "0049": "Monte Castelo",
        "0050": "Montese",
        "0051": "Moura Brasil",
        "0052": "Mucuripe",
        "0053": "Papicu",
        "0054": "Parangaba",
        "0055": "Parque Presidente Var",
        "0056": "Parque Sao Jose",
        "0057": "Parquelandia",
        "0058": "Passare",
        "0059": "Pici",
        "0060": "Praia de Iracema",
        "0061": "Prefeito Jose Walter",
        "0062": "Presidente Tancredo N",
        "0063": "Rodolfo Teofilo",
        "0064": "Serrinha",
        "0065": "Tauape",
        "0066": "Varjota",
        "0067": "Vicente Pinzon",
        "0068": "Vila Ellery",
        "0069": "Vila Peri",
        "0070": "Vila União",
        "0071": "Vila Velha",
        "9999": "Outros Municípios do Ceará",
        "0": "Ignorado"
    }

    d = {int(k):  unicode(v, 'utf8') for k, v in bairros.items()}
    return d
