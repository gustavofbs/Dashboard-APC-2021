import plotly.graph_objects as go      #fazer os gráficos  
import pandas as pd                    #abrir e manipular a tabela
import dash                            #faz abrir uma pagina html pelo python       #O html é uma Linguagem de Marcação de Hipertexto
import dash_core_components as dcc     #abrir o grafico na pag html
import dash_html_components as html    #usar as funções html no python
from numpy import NaN, nan             #é usada para realizar cálculos Nan = valores não numéricos

#*****************************************************//Código leandro e daniel//********************************************************

linhas = pd.read_csv("https://raw.githubusercontent.com/artur-jack/Dashboard-APC-2021/main/athletes.csv", sep=",")  #usa o pandas para abrir a tabela

#--------------------------------------------------------------------------------------------------------------------------------

dic = {}    #Os dicionários são usados ​​para armazenar valores de dados em pares chave(país): valor(medalha de ouro). 
for nacionalidade, medalha in zip(linhas["nationality"],linhas["gold"]):   #zip parea duas listas
    if nacionalidade in dic:
        dic[nacionalidade] += int(medalha)
    else:
        dic[nacionalidade] = int(medalha)

Paises = [] 
Medalhas = []

for i in dic:
    Paises.append(i)           #armazena um por um os paises na lista vazia acima
    Medalhas.append(dic[i])    #armazena um por um as medalhas de ouro na lista vazia acima

#---------------------------------------------------------------------------------------------------------------------------------
linha1 = go.Bar(  #usa a bibliotaca importada para gerar um grafico de barra
    x = Paises,   #coloca paises no eixo x
    y = Medalhas, #coloca as medalhas de ouro no eixo y
)

#**********************************************************Código Elmar********************************************************************

alturas = linhas.loc[:,'height'].dropna() #Remova os valores ausentes.
paises = linhas.loc[:,'nationality']


def media(pais):
    soma = 0
    n = 0

    for alt, ps in zip(alturas, paises):
        if ps == pais:
            soma += alt
            n += 1
    return round(soma / n, 4)


paises= ['ESP', 'USA', 'ITA', 'BRA', 'POL', 'ETH','NED','JPN','MEX','RUS','GER','AUS']
medias= []
for x in paises:
   medias.append(media(x))

linha2 = go.Bar(
     orientation = 'h',  #deixar as barras na horizontal
     x = medias,
     y = paises,
    marker = dict(                    #variavel q guarda um dicionario e dentro desse dicionario tem a cor da barra 
        color='rgba(155, 89, 182, 1)'
    )
)

#********************************************************* Código Arthur***************************************************************

pesos = linhas.loc[:,'weight'].dropna() #dropna vai remover os valores nulos(NaN) que tinha nos dados.
paises = linhas.loc[:,'nationality']

def media(pais):  #Definimos uma função para fazer a média de peso.
    soma = 0
    n = 0

    for pe, ps in zip(pesos, paises): 
        if ps == pais:  #Se o ps(que recebe os paises) for igual ao país, vai atribuir na variavel soma: soma(o valor q já estava) + o peso(pe), tbm vai somar 1 na variavel n.
            soma += pe # soma = soma + pe
            n += 1
    return round(soma / n, 2) #round vai limitar as casas decimais que aparecerão no gráfico.

Paises= ['ESP', 'USA', 'ITA', 'BRA', 'POL', 'ETH','NED','JPN','MEX','RUS','GER','AUS','CAN','CHI']
Pesos= []
for x in Paises:
   Pesos.append(media(x))

linha3 = go.Line(
        y = Pesos,
        x = Paises
)

#**************************************************************Código Karol e Flávio*****************************************************
sport = linhas.loc[:, 'sport']      # O loc serve para escolher apenas a parte selecionada, nesse caso ele vai pegar todos os componentes da coluna sport
sex = linhas.loc[:, 'sex']
esportes = set()     # Serve como uma lista, mas a diferença é que o set() não deixa repetir elementos.

for sp in sport:
    esportes.add(sp) 

esportes2 = esportes.copy()      #O copy() Serve para fazer uma cópia,nesse caso foi criada uma cópia do "esportes", que vai ser atribuída ao esporte2
macho = []
femea = []


def quantity(spt):
    global macho, femea, esportes

    lst_female = []
    lst_male = []

    for sp, sexo in zip(sport, sex):      #zip() parea duas listas ex: primeiro elemento com primeiro e etc.
        if sp == spt:
            if sexo == 'male':
                lst_male.append(sexo)
            elif sexo == 'female':
                lst_female.append(sexo)

    males = len(lst_male)
    females = len(lst_female)

    if spt in esportes:
        macho.append(males)     #append() Serve pra adicionar elementos no final da lista.
        esportes.discard(spt)
    else:
        macho.append(0)

    if spt in esportes2:
        femea.append(females)
        esportes2.discard(spt)
    else:
        femea.append(0)


for sp in sport:
    quantity(sp)

    if esportes2 == set():
        break

# ---------------------------------------------------------------------------------------------------------------------------------------
linha4 = go.Bar(
    x=sport,
    y=macho,
    name='Homens'

    # name = "Quantidade",
    # go.Bar #É pra definir o tipo do gráfico, nesse caso o gráfico de barras
    # hovertemplate = '%{y} unidades'.center(8) + '<br>'  + '%{x}' #São utilizados o as informações de Y e de X para vizualização do dado
)
linha5 = go.Bar(
    x=sport,
    y=femea,
    name='Mulheres'

)
#**********************************************************Amanda e Gustavo***********************************************************

# Filtro das modalidades e medalhas

    # Esse filtro tem como função separar todas as modalidades em uma lista, e o total de suas medalhas de ouro respectivamente 
    # em uma outra lista.

dic = {}
for sport,medalha in zip(linhas['sport'],linhas['gold']):
    if sport in dic:
        dic[sport] += int(medalha)
    else:
        dic[sport] = int(medalha)

sport = []
Medalhas = []

for i in dic:
    sport.append(i)
    Medalhas.append(dic[i])

# Filtro dos países com suas medalhas.

# Aqui é definido uma nova função onde seleciona um esporte e mostra qual país liderou com a quantidade de medalhas.

def winner(modalidade):

    # Para fazer o somatório das medalhas, é necessário que todos os países se iniciem no 0 para que façam a contagem.

    global result
    result = {x: 0 for x in linhas['nationality']}

# Aqui, ele vai percorrer nas listas 'sport', 'nationality' e 'gold' com a finalidade de saber onde colocar as suas 
# medalhas nos seus respectivos esportes e países.

    for sp, ct, gd in zip(linhas['sport'], linhas['nationality'], linhas['gold']):
        if sp == modalidade:
            result[ct] += gd

# Essa 'key' tem como função separar os maiores valores 'val' através do '[max(result.values())]' e colocá-los em uma nova lista,
# além de retornar elementos repetidos caso possuam valores repetidos.

    key = [modalidade + ' ' + key + ' ' + str(val) for m in [max(result.values())] for key,val in result.items() if val == m]
    return key

# Lista dos esportes para ser usada mais tarde em um novo filtro

lista_sp = ['athletics', 'fencing', 'taekwondo', 'cycling', 'triathlon', 'volleyball', 'aquatics', 'rugby sevens', 'wrestling', 'football', 'shooting', 'boxing', 'equestrian', 'rowing', 'judo', 'handball', 'badminton', 'hockey', 'modern pentathlon', 'table tennis', 'canoe', 'basketball', 'golf', 'archery', 'weightlifting', 'sailing', 'tennis', 'gymnastics']
resultados = list(map(winner, lista_sp))

# Separação das strings.

    # Criação de listas com as seguintes variáveis:

spt = []
country = []
medal = []

    # A função 'winner()' é executada com cada esporte da 'lista_sp', onde iremos receber três listas no formato 'esporte, país, medalhas', 
    # ou seja, separa o nome dos esportes, a sigla dos países, e a quantidade de medalhas através do atributo split, colocando-os
    # em três listas diferentes: 'spt', 'country', 'medal'. Vale dar um adendo de que essa estrutura a seguir está filtrando o resultado
    # para a função 'winner', logo, a separação do dataframe 'athletes.csv' não funciona aqui, fazendo então, uma nova separação de listas. 

for sp in (lista_sp):
    for x in winner(sp):

        # Essa condição verifica se nas duas palavras de um esporte (caso seja um nome composto), o primeiro e o segundo elemento
        # (índice 0 e 1, repectivamente) são maiores que 3 caracteres, para assim, constatar se as duas palavras fazem parte do 
        # nome do esporte, como o 'table tennis', onde as duas palavras simbolizam um único esporte. Isso acontece devido ao '> 3',
        # para saber quando é um esporte ou um país, sabendo que a sigla dos países sempre vai ter exatamente 3 caracteres. Então, 
        # caso ocorra, utiliza-se duas aspas: ' ' para determinar o espaço entre os dois elementos do nome composto. E assim, todos
        # esses dados já formatados vão para a lista 'spt'.

        if len(x.split(' ')[0]) > 3 and len(x.split(' ')[1]) > 3:
            spt.append(x.split(' ')[0] + ' ' + x.split(' ')[1])
        else:
            spt.append(x.split(' ')[0])

        # Nessa outra condição, ele verifica se o segundo elemento (índice 1) é um país caso tenha exatos 3 caracteres. E caso o esporte
        # tenha duas palavras, o 'elif' constata se o terceiro elemento (índice 2) é um país através do mesmo método usado anteriormente. 
        # Aqui, os dados já formatados vão para a lista 'country'

        if len(x.split(' ')[1]) == 3:
            country.append(x.split(' ')[1])
        elif len(x.split(' ')[2]) == 3:
            country.append(x.split(' ')[2])

        # Aqui, adiciona o total de medalhas em uma lista, e o '[-1]' significa que vai ser a última lista a ser representada,
        # no caso, a lista 'medal'.

        medal.append(x.split(' ')[-1])

# Gráfico.

    # Nessa parte é determinado o tipo de gráfico que se deseja, no caso o Sunburst. 

grafico5 = go.Figure(go.Sunburst(

    # Aqui é onde o gráfico funciona baseado nos dados que os filtros anteriores nos deram. 'Labels' é uma lista de nomes 
    # que vão aparecer no gráfico. (no caso o 'olympics 2016', todos os esportes e os países)

    labels = ['Olympics 2016'] + sport + country,

    # Parents é uma lista que vai se relacionar com labels para dizer quais elementos são filhos de quem. Então, o [''] significa 
    # que o 'olympics 2016' não é filho de ninguém. E todos os outros esportes são filhos do 'olympics 2016', repetindo 29 vezes 
    # (quantidade de elementos da lista sport). Depois, os países tornam-se filhos de um esporte específico através da lista 'spt'.

    parents = [''] + ['Olympics 2016'] * len(sport) + spt,

    # Values vai fazer uma referência a labels, atribuindo valores. Onde o [0] significa que o nome 'olympics 2016' e a lista sports 
    # possuem valor 0, e em seguida, atribuímos aos países as suas respectivas medalhas através da lista 'medal'.

    values = [0] * 29 + medal

))

# Tamanho do gráfico definido por 'height'.

grafico5.update_layout(height = 700)

#--------------------------------------------------------------------------------------------------------------------------------------
# Importação de um css externo
css = ["https://bootswatch.com/4/darkly/bootstrap.css"] # O css é usado para estilizar elementos escritos em uma linguagem de marcação como HTML

app= dash.Dash(     #cria a pag 
    
    external_stylesheets = css # CSS exterior é importado para dentro da página
)    
fig_names = ['Medalhas de Ouro', 'Média de Altura','Média de Peso','Sexo por modalidade','Medalhas por modalidade'] #opções dropdown
fig_dropdown = html.Div([html.Div(html.Center('Olimpíadas Rio 2016'),   #div é uma caixa de elementos  #titulo  
style = {"font-size":"35px", "text-align":"center"},className="card-header"), #classname pro codigo usar as configurações do css exterior
    html.Div([
        html.Div(dcc.Dropdown(              #dropdown caixa para escolher o gráfico
        id='fig_dropdown',
        options=[{'label': x, 'value': x} for x in fig_names], #colocar os nomes da variavel fig_names como opções
        placeholder ="Escolha o Gráfico",                      #palavra q aparece dentro da caixa quando vc não escolhe nada
        value = 'Medalhas de Ouro',                            #Opção q aparece sempre q vc abrir
        style = {"width":"400px", "border-radius":"10px", "border":" 1px solid white", "font-weight":"bold","color":"#000000"},
        #css do q tá dentro do dropdown
)
,style ={"margin-left":"720px"}, className = "nav-item dropdown")],className="card-body")]
,className="card text-white bg-primary mb-3") #css do dropdown

fig_plot = html.Div(id='fig_plot')     #id pro cod ser edentificado pelo callback
app.layout = html.Div([fig_dropdown, fig_plot])  #div com uma lista formada por variaveis dentro

@app.callback(         #Para coletar entradas e saídas (Input/Output) o Dash traz o decorator @app.callbacks()
dash.dependencies.Output('fig_plot', 'children'),# primeiro parâmetro o id do componente que será utilizado para exibição do resultado, 
[dash.dependencies.Input('fig_dropdown', 'value')])# e no segundo a propriedade deste componente que será modificada pelo Input;



def name_to_figure(fig_name):   #função para gerar o gráfico
    figure1 = go.Figure()
    figure2 = go.Figure()
    figure3 = go.Figure()
    figure4 = go.Figure()
    figure5 = go.Figure()

#------------------------------------------------------------LAYOUT(Medalhas de Ouro)-------------------------------------------------------------
    figure1.update_layout( #Deifição das configurações de layout
                    xaxis_title = dict( #Adição de um título que deixará mais claro que tipo de informação será exibida no eixo X
                    text = "<b>Países<b>", #Texto que será exibido, colocado em negrito para maior destaque por meio do comando "<b><b>", da linguagem html
                    font = dict( #São atribuídas algumas propriedades para o texto
                    family = 'bold', #A fonte do texto
                    color = 'white', #A cor do texto
                    size = 25 #Tamanho do texto em pixels
                )
            ),
            xaxis = dict( #São atribuídas propriedades para o eixo X e para seus dados
                rangeslider=dict(visible=True), #Um filtro do próprio Plotly
                showline = True, #Mostrar a linha do Eixo X
                tickmode = "linear", #É atribuído 'linear' no tipo de 'tick' para que se possa definir um valor incial para a exibição dos valores em X(tick0) e um passo(dtick)
                showgrid = False, #Não mostrar a grade de linhas do eixo X,
                tickfont = dict(color = "white"),
                linecolor = 'rgb(63, 64, 63)', #Cor da linha do eixo X
                linewidth = 4, #Espessura da linha do eixo X
                ticks = 'outside' #Adição de "traços" do lado de fora do gráfico para melhor vizualização dos dados
            ),
            yaxis = dict( #Atribuição de propriedades para o eixo Y e seus respectivos dados
                gridcolor = 'rgb(63, 64, 63)', #Definição da cor da grade de linhas do eixo Y
                linewidth = 4,
                tickfont = dict(color = "white"),
                zeroline = False, #Para que a linha zero do eixo Y se mostre é atribuido "False" ao comando "zeroline"
                linecolor = "rgb(63, 64, 63)", #É atrbuído uma cor a linha do eixo Y
                showticklabels = True #É dado o comando para não mostrar a legenda padrão do Plotly
            ),
            margin = dict( #Configurações com relação as margens do gráfico
                t = 50,    #Distância do gráfico do topo da página em pixels
                l = 100    #Distância do gráfico da lateral esquerda em pixels
            ),

            plot_bgcolor = '#f7f8fa', #Definição de cor do background do gráfico,
            paper_bgcolor = "#393b45",
            height=550,
            hoverlabel = dict( #Atrubuição das propriedades para o HOVER
            bgcolor = '#3F3F3F', #Cor do background do HOVER
            align = 'auto', #Alinhamento do texto do hover automático
            font = dict( #Configurações para o texto do hover
                family = 'bold', #Fonte do texto
                size = 16, #Tamanho do texto em pixels
                color = 'white' #Cor do texto
            )
        )
)

#------------------------------------------------------------LAYOUT(Media de Altura)-------------------------------------------------------------
    figure2.update_layout( #Deifição das configurações de layout
                    xaxis_title = dict( #Adição de um título que deixará mais claro que tipo de informação será exibida no eixo X
                    font = dict( #São atribuídas algumas propriedades para o texto
                )
            ),
            xaxis = dict( #São atribuídas propriedades para o eixo X e para seus dados
                showline = True, #Mostrar a linha do Eixo X
                tickmode = "linear", #É atribuído 'linear' no tipo de 'tick' para que se possa definir um valor incial para a exibição dos valores em X(tick0) e um passo(dtick)
                showgrid = False, #Não mostrar a grade de linhas do eixo X,
                tickfont = dict(color = "white"),
                linecolor = 'rgb(63, 64, 63)', #Cor da linha do eixo X
                linewidth = 4, #Espessura da linha do eixo X
                ticks = 'outside' #Adição de "traços" do lado de fora do gráfico para melhor vizualização dos dados
            ),
            yaxis = dict( #Atribuição de propriedades para o eixo Y e seus respectivos dados
                gridcolor = 'rgb(63, 64, 63)', #Definição da cor da grade de linhas do eixo Y
                linewidth = 4,
                tickfont = dict(color = "white"),
                zeroline = False, #Para que a linha zero do eixo Y se mostre é atribuido "False" ao comando "zeroline"
                linecolor = "rgb(63, 64, 63)", #É atrbuído uma cor a linha do eixo Y
                showticklabels = True #É dado o comando para não mostrar a legenda padrão do Plotly
            ),
            margin = dict( #Configurações com relação as margens do gráfico
                t = 50,    #Distância do gráfico do topo da página em pixels
                l = 100    #Distância do gráfico da lateral esquerda em pixels
            ),

            plot_bgcolor = '#f7f8fa', #Definição de cor do background do gráfico,
            paper_bgcolor = "#393b45",
            hoverlabel = dict( #Atrubuição das propriedades para o HOVER
            bgcolor = '#3F3F3F', #Cor do background do HOVER
            align = 'auto', #Alinhamento do texto do hover automático
            font = dict( #Configurações para o texto do hover
                family = 'bold', #Fonte do texto
                size = 16, #Tamanho do texto em pixels
                color = 'white' #Cor do texto
            )
        )
)

#------------------------------------------------------------LAYOUT(Média de peso)-------------------------------------------------------------
    figure3.update_layout( #Deifição das configurações de layout
                    xaxis_title = dict( #Adição de um título que deixará mais claro que tipo de informação será exibida no eixo X
                    text = "<b>Países<b>", #Texto que será exibido, colocado em negrito para maior destaque por meio do comando "<b><b>", da linguagem html
                    font = dict( #São atribuídas algumas propriedades para o texto
                    family = 'bold', #A fonte do texto
                    color = 'white', #A cor do texto
                    size = 25 #Tamanho do texto em pixels
                )
            ),
            xaxis = dict( #São atribuídas propriedades para o eixo X e para seus dados
                rangeslider=dict(visible=True), #Um filtro do próprio Plotly
                showline = True, #Mostrar a linha do Eixo X
                tickmode = "linear", #É atribuído 'linear' no tipo de 'tick' para que se possa definir um valor incial para a exibição dos valores em X(tick0) e um passo(dtick)
                showgrid = False, #Não mostrar a grade de linhas do eixo X,
                tickfont = dict(color = "white"),
                linecolor = 'rgb(63, 64, 63)', #Cor da linha do eixo X
                linewidth = 4, #Espessura da linha do eixo X
                ticks = 'outside' #Adição de "traços" do lado de fora do gráfico para melhor vizualização dos dados
            ),
            yaxis = dict( #Atribuição de propriedades para o eixo Y e seus respectivos dados
                gridcolor = 'rgb(63, 64, 63)', #Definição da cor da grade de linhas do eixo Y
                linewidth = 4,
                tickfont = dict(color = "white"),
                zeroline = False, #Para que a linha zero do eixo Y se mostre é atribuido "False" ao comando "zeroline"
                linecolor = "rgb(63, 64, 63)", #É atrbuído uma cor a linha do eixo Y
                showticklabels = True #É dado o comando para não mostrar a legenda padrão do Plotly
            ),
            margin = dict( #Configurações com relação as margens do gráfico
                t = 50,    #Distância do gráfico do topo da página em pixels
                l = 100    #Distância do gráfico da lateral esquerda em pixels
            ),

            plot_bgcolor = '#f7f8fa', #Definição de cor do background do gráfico,
            paper_bgcolor = "#393b45",
            hoverlabel = dict( #Atrubuição das propriedades para o HOVER
            bgcolor = '#3F3F3F', #Cor do background do HOVER
            align = 'auto', #Alinhamento do texto do hover automático
            font = dict( #Configurações para o texto do hover
                family = 'bold', #Fonte do texto
                size = 16, #Tamanho do texto em pixels
                color = 'white' #Cor do texto
            )
        )
)

#----------------------------------------------------------LAYOUT(Sexo por Modalidade)------------------------------------------------

    figure4.update_layout(  # Deifição das configurações de layout
    xaxis_title=dict(  # Adição de um título que deixará mais claro que tipo de informação será exibida no eixo X
        text="<b>Modalidades<b>",
        # Texto que será exibido, colocado em negrito para maior destaque por meio do comando "<b><b>", da linguagem html
        font=dict(  # São atribuídas algumas propriedades para o texto
            family='bold',  # A fonte do texto
            color='Black',  # A cor do texto
            size=25  # Tamanho do texto em pixels
        )
    ),
    xaxis=dict(  # São atribuídas propriedades para o eixo X e para seus dados
        rangeslider=dict(visible=True),  # Um filtro do próprio Plotly
        showline=True,  # Mostrar a linha do Eixo X
        tickmode="linear",
        # É atribuído 'linear' no tipo de 'tick' para que se possa definir um valor incial para a exibição dos valores em X(tick0) e um passo(dtick)
        showgrid=False,  # Não mostrar a grade de linhas do eixo X,
        tickfont=dict(color="Black"),  
        linecolor='rgb(63, 64, 63)',  # Cor da linha do eixo X
        linewidth=4,  # Espessura da linha do eixo X
        ticks='outside'  # Adição de "traços" do lado de fora do gráfico para melhor vizualização dos dados
    ),
    yaxis=dict(  # Atribuição de propriedades para o eixo Y e seus respectivos dados
        gridcolor='rgb(63, 64, 63)',  # Definição da cor da grade de linhas do eixo Y
        linewidth=4,
        tickfont=dict(color="white"),
        zeroline=False,  # Para que a linha zero do eixo Y se mostre é atribuido "False" ao comando "zeroline"
        linecolor="rgb(63, 64, 63)",  # É atrbuído uma cor a linha do eixo Y
        showticklabels=True  # É dado o comando para não mostrar a legenda padrão do Plotly
    ),
    margin=dict(  # Configurações com relação as margens do gráfico
        t=50,  # Distância do gráfico do topo da página em pixels
        l=100  # Distância do gráfico da lateral esquerda em pixels
    ),
    height=580,  # Altura do gráfico em pixels
    plot_bgcolor='#D5E4F7',  # Definição de cor do background do gráfico,
    paper_bgcolor="#cddeca",
    hoverlabel=dict(  # Atrubuição das propriedades para o HOVER
        bgcolor='#3F3F3F',  # Cor do background do HOVER
        align='auto',  # Alinhamento do texto do hover automático
        font=dict(  # Configurações para o texto do hover
            family='bold',  # Fonte do texto
            size=16,  # Tamanho do texto em pixels
            color='white'  # Cor do texto
        )
    )
)

#----------------------------------------------------------------------------------------------------------------------------------
    figure5.update_layout( #Deifição das configurações de layout
                    xaxis_title = dict( #Adição de um título que deixará mais claro que tipo de informação será exibida no eixo X
                    text = "<b>Países<b>", #Texto que será exibido, colocado em negrito para maior destaque por meio do comando "<b><b>", da linguagem html
                    font = dict( #São atribuídas algumas propriedades para o texto
                    family = 'bold', #A fonte do texto
                    color = 'white', #A cor do texto
                    size = 25 #Tamanho do texto em pixels
                )
            ),
            xaxis = dict( #São atribuídas propriedades para o eixo X e para seus dados
                rangeslider=dict(visible=True), #Um filtro do próprio Plotly
                showline = True, #Mostrar a linha do Eixo X
                tickmode = "linear", #É atribuído 'linear' no tipo de 'tick' para que se possa definir um valor incial para a exibição dos valores em X(tick0) e um passo(dtick)
                showgrid = False, #Não mostrar a grade de linhas do eixo X,
                tickfont = dict(color = "white"),
                linecolor = 'rgb(63, 64, 63)', #Cor da linha do eixo X
                linewidth = 4, #Espessura da linha do eixo X
                ticks = 'outside' #Adição de "traços" do lado de fora do gráfico para melhor vizualização dos dados
            ),
            yaxis = dict( #Atribuição de propriedades para o eixo Y e seus respectivos dados
                gridcolor = 'rgb(63, 64, 63)', #Definição da cor da grade de linhas do eixo Y
                linewidth = 4,
                tickfont = dict(color = "white"),
                zeroline = False, #Para que a linha zero do eixo Y se mostre é atribuido "False" ao comando "zeroline"
                linecolor = "rgb(63, 64, 63)", #É atrbuído uma cor a linha do eixo Y
                showticklabels = True #É dado o comando para não mostrar a legenda padrão do Plotly
            ),
            margin = dict( #Configurações com relação as margens do gráfico
                t = 50,    #Distância do gráfico do topo da página em pixels
                l = 100    #Distância do gráfico da lateral esquerda em pixels
            ),

            plot_bgcolor = '#f7f8fa', #Definição de cor do background do gráfico,
            paper_bgcolor = "#dcdee8",
            height=800,
            hoverlabel = dict( #Atrubuição das propriedades para o HOVER
            bgcolor = '#3F3F3F', #Cor do background do HOVER
            align = 'auto', #Alinhamento do texto do hover automático
            font = dict( #Configurações para o texto do hover
                family = 'bold', #Fonte do texto
                size = 16, #Tamanho do texto em pixels
                color = 'white' #Cor do texto
            )
        )
)

    if fig_name == 'Medalhas de Ouro':         #Dependendo do q eu selecionar no dropdown essa prate da função vai gerar o gráfico
        figure1.add_trace(linha1)
        return dcc.Graph(figure = figure1)
    if fig_name == 'Média de Altura': 
        figure2.add_trace(linha2)
        return dcc.Graph(figure = figure2)
    if fig_name == 'Média de Peso': 
        figure3.add_trace(linha3)
        return dcc.Graph(figure = figure3)       
    if fig_name == 'Sexo por modalidade': 
        figure4.add_trace(linha4)
        figure4.add_trace(linha5)
        return dcc.Graph(figure = figure4)
    if fig_name == 'Medalhas por modalidade': 
        figure5.add_trace(go.Sunburst(
    labels = ['Olympics 2016'] + sport + country,
    parents = [''] + ['Olympics 2016'] * len(sport) + spt,
    values = [0] * 29 + medal))
        return dcc.Graph(figure = figure5)
        

app.run_server(debug=True, use_reloader=False)      
#usereloader pagina carrega só quando o grafico carrega e debug mostra se tiver erro.
