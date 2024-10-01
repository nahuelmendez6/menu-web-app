from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username', 'password1', 'password2']
        labels = {
            'email':'Correo electrónico',
            'username':'Nombre del local',
            'password1':'Contraseña',
            'password2':'Repite contraseña'
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = False

        if commit:
            user.save()
            # Asignación a grupo (si es necesario)
            # group = Group.objects.get(name='owners')
            # user.groups.add(group)
        return user
