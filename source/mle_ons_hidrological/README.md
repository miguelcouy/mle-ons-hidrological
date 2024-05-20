# Mercado Livre de Energia - Dados Abertos do ONS: Hidrologia

Este projeto foi desenvolvido para automatizar a extração, transformação e carregamento (ETL) de dados referentes à Energia Natural Afluente (ENA) e Energia Armazenável (EAR) em reservatórios, bacias, subsistemas e REEs (Reservatório Equivalente de Energia) do Operador Nacional do Sistema Elétrico (ONS). A partir dos dados disponíveis publicamente no repositório do ONS, este projeto facilita a recuperação, limpeza e armazenamento dos dados de maneira estruturada.


## Instalação

O pacote mle_ons_hidrological está localizado no [PyPI](www.pypi.org).
Considere utilizar a versão mais recente do Python.
Você consegue instalá-lo via pip.

```bash
  #python3
  pip3 install mle_ons_hidrological
```
    
## Uso/Exemplos

```python
from pathlib import Path
from dateutil.relativedelta import relativedelta
import datetime as dt

import mle_ons_hidrological


my_path = Path('data')

today = dt.datetime.now()
two_years_ago = today - relativedelta(years = 2)

mle_ons_hidrological.get_ena_by_subsistema(
    subsistema = ['Norte'],
    date_from = two_years_ago,
    date_to = today,
    save_ok = True,
    save_where = my_path
)

mle_ons_hidrological.get_ear_by_subsistema(
    subsistema = ['Norte'],
    date_from = two_years_ago,
    date_to = today,
    save_ok = True,
    save_where = my_path
)
```


## Documentação do Código


#### Recuperar dados de energia natural afluente (ENA) por reservatório.
```python
  get_ena_by_reservatorio()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `reservatorios` | `list[str]` | **Opcional**. Lista de reservatórios registrados no SIN. |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia natural afluente (ENA) por subsistema.
```python
  get_ena_by_subsistema()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `subsistemas` | `list[str]` | **Opcional**. Lista de subsistemas registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia natural afluente (ENA) por bacia.
```python
  get_ena_by_bacia()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `bacias` | `list[str]` | **Opcional**. Lista de bacias registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia natural afluente (ENA) por Reservatório Equivalente de Energia (REE).
```python
  get_ena_by_ree()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `rees` | `list[str]` | **Opcional**. Lista de Reservatórios Equivalentes de Energia (REE) registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |


#### Recuperar dados de energia armazenável (EAR) por reservatório.
```python
  get_ear_by_reservatorio()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `reservatorios` | `list[str]` | **Opcional**. Lista de reservatórios registrados no SIN. |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia armazenável (EAR) por subsistema.
```python
  get_ear_by_subsistema()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `subsistemas` | `list[str]` | **Opcional**. Lista de subsistemas registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia armazenável (EAR) por bacia.
```python
  get_ear_by_bacia()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `bacias` | `list[str]` | **Opcional**. Lista de bacias registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Recuperar dados de energia armazenável (EAR) por Reservatório Equivalente de Energia (REE).
```python
  get_ena_by_ree()
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `rees` | `list[str]` | **Opcional**. Lista de Reservatórios Equivalentes de Energia (REE) registrados no SIN |
| `date_from` | `datetime` | **Opcional**. Data inicial para filtro de intervalo de datas |
| `date_to` | `datetime` | **Opcional**. Data final para filtro de intervalo de datas|
| `not_found_ok` | `bool` | **Opcional**. Ignorar se os dados não forem encontrados (padrão é True) |
| `clean_ok` | `bool` | **Opcional**. Indica se a limpeza é necessária (padrão é True) |
| `save_ok` | `bool` | **Opcional**. Indica se o salvamento é necessário (padrão é False) |
| `save_where` | `Path` | **Opcional**. Diretório onde o arquivo será salvo |

#### Valores de parâmetros permitidos:

Subsistemas: "Norte", "Nordeste", "Sudeste", "Sul".

Reservatórios Equivalentes de Energia (REE): "BELO MONTE", "IGUACU", "MADEIRA", "MANAUS-AMAPA", "NORDESTE", "NORTE", "PARANA", "PARANAPANEMA", "SUDESTE", "SUL", "TELES PIRES".

Bacias: "AMAZONAS", "ARAGUARI", "CAPIVARI", "DOCE", "GRANDE", "IGUACU", "ITABAPOANA", "ITAJAI", "JACUI", "JEQUITINHONHA", "MUCURI", "PARAGUACU", "PARAGUAI", "PARAIBA DO SUL", "PARANA", "PARANAIBA", "PARANAPANEMA", "PARNAIBA", "SANTA MARIA VIT", "SAO FRANCISCO", "TIETE", "TOCANTINS", "URUGUAI".

Reservatórios: "14 DE JULHO", "A. VERMELHA", "AIMORES", "B. BONITA", "B.COQUEIROS", "BAGUARI", "BAIXO IGUACU", "BALBINA", "BARIRI", "BARRA BRAUNA", "BARRA GRANDE", "BATALHA", "BELO MONTE", "BOA ESPERANÇA", "C. DOURADA", "C.BRANCO-1", "C.BRANCO-2", "CACHOEIRA CALDEIRAO", "CACONDE", "CACU", "CAMARGOS", "CAMPOS NOVOS", "CANA BRAVA", "CANASTRA", "CANDONGA", "CANOAS I", "CANOAS II", "CAPIVARA", "CASTRO ALVES", "CHAVANTES", "COARACY NUNES", "COLIDER", "CORUMBA", "CORUMBA-3", "CORUMBA-4", "CURUA-UNA", "D. FRANCISCA", "DARDANELOS", "E. DA CUNHA", "EMBORCAÇÃO", "ESPORA", "ESTREITO", "FERREIRA GOMES", "FONTES", "FOZ CHAPECO", "FOZ DO RIO CLARO", "FUNDÃO", "FUNIL", "FUNIL-MG", "FURNAS", "G. B. MUNHOZ", "G. P. SOUZA", "GARIBALDI", "GUAPORE", "GUILM. AMORIM", "HENRY BORDEN", "I. SOLTEIRA", "IBITINGA", "IGARAPAVA", "ILHA POMBOS", "IRAPE", "ITÁ", "ITAIPU", "ITAPARICA", "ITAPEBI", "ITAUBA", "ITIQUIRA I", "ITIQUIRA II", "ITUMBIARA", "ITUTINGA", "JACUI", "JAGUARA", "JAGUARI", "JAURU", "JIRAU", "JUPIA", "JURUMIRIM", "L. C. BARRETO", "LAJEADO", "LIMOEIRO", "M. MORAES", "MACHADINHO", "MANSO", "MARIMBONDO", "MASCARENHAS", "MAUA", "MIRANDA", "MONJOLINHO", "MONTE CLARO", "MOXOTO", "N. AVANHANDAVA", "NILO PEÇANHA", "NOVA PONTE", "OURINHOS", "P. AFONSO 1,2,3", "P. AFONSO 4", "P. COLOMBIA", "PARAIBUNA", "PASSO FUNDO", "PASSO REAL", "PASSO SAO JOAO", "PEDRA DO CAVALO", "PEIXE ANGICAL", "PEREIRA PASSOS", "PICADA", "PIMENTAL", "PIRAJU", "PONTE DE PEDRA", "PORTO ESTRELA", "PORTO PRIMAVERA", "PROMISSÃO", "QUEBRA QUEIXO", "QUEIMADO", "RETIRO BAIXO", "RONDON II", "ROSAL", "ROSANA", "S.DO FACÃO", "S.R.VERDINHO", "SA CARVALHO", "SALTO", "SALTO CAXIAS", "SALTO GRANDE CM", "SALTO GRANDE CS", "SALTO OSORIO", "SALTO PILAO", "SALTO SANTIAGO", "SAMUEL", "SANTA BRANCA", "SANTA CLARA-PR", "SANTO ANTONIO", "SAO DOMINGOS", "SAO JOSE", "SAO MANOEL", "SAO ROQUE", "SAO SALVADOR", "SÃO SIMÃO", "SEGREDO", "SERRA DA MESA", "SIMPLICIO", "SINOP", "SOBRADINHO", "SOBRAGI", "STA.CLARA-MG", "STO ANTONIO DO JARI", "SUIÇA", "TAQUARUÇU", "TELES PIRES", "TRÊS IRMÃOS", "TRÊS MARIAS", "TUCURUI", "VOLTA GRANDE", "XINGO".
## Melhorias

- [ ]  Implementar uma funcionalidade que permita a conversão automática de parâmetros repassados pelo usuário como strings para o formato datetime.
- [ ]  Adicionar uma funcionalidade que converta automaticamente parâmetros repassados como strings para o formato Path.
- [ ]  Desenvolver uma funcionalidade que permita ao usuário salvar o DataFrame em outros formatos de arquivo, como parquet ou xlsx, além do formato CSV atual, oferecendo maior versatilidade no armazenamento dos dados.
- [ ]  Implementar uma funcionalidade que permita ao usuário especificar um nome diferente para o arquivo de dados ao salvar.
## Autores

- Miguel Couy: [GitHub](https://github.com/miguelcouy) // [LinkedIn](https://www.linkedin.com/in/miguelcouy/)
