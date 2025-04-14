from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ex: João Silva',
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ex: João Silva',
            }
        )
    )
    email_cadastro = forms.EmailField(
        label='Email Preferido',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ex: joaosilva@xpto.com'
            }
        )
    )
    senha_cadastro = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        )
    )
    confirmar_senha = forms.CharField(
        label='Confirmar Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                 raise forms.ValidationError('O nome não pode conter espaços.')
        else:
            return nome

    def clean_confirmar_senha(self):
        senha_cadastro = self.cleaned_data.get('senha_cadastro')
        confirmar_senha = self.cleaned_data.get('confirmar_senha')

        if senha_cadastro and confirmar_senha:
            if senha_cadastro != confirmar_senha:
                raise forms.ValidationError('As senhas não conferem!')
            else:
                return confirmar_senha