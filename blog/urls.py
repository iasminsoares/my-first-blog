#Aqui, estamos importando do Django a função url e todas as nossas views do aplicativo blog
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #especifica um padrão de URL
]
	#estamos agora atribuindo uma view chamada post_list à URL raiz
	#A última parte, name='post_list', é o nome da URL que será usado para identificar a view.
	#Como você pode ver, estamos agora atribuindo uma view chamada post_list à URL raiz. 
	#Este padrão de URL corresponde a uma sequência de caracteres vazia, e o resolvedor de URLs do Django irá ignorar o nome de domínio 
	#(ou seja, http://127.0.0.1:8000 /) que antecede o caminho completo da URL. Este padrão dirá ao Django que views.post_list 
	#é o lugar correto aonde ir se alguém entra em seu site pelo endereço 'http://127.0.0.1:8000 /'.
