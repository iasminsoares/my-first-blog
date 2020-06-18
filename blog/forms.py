from django import forms #importando o módulo de formulários do Django

from .models import Post

class PostForm(forms.ModelForm): #PostForm é o nome do nosso formulário

    class Meta: #dizemos ao Django qual modelo deverá ser usado para criar este formulário
        model = Post
        fields = ('title', 'text',) #quais campos devem entrar no nosso formulário

        #Tudo o que precisamos fazer agora é usar o formulário em uma view e mostrá-lo em um template.
		#Novamente, criaremos um link para a página, uma URL, uma view e um template.