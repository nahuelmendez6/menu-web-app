from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile  # Asegúrate de que estás importando tu modelo Profile

class RegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)  # Cambiado a required=False
    address = forms.CharField(max_length=255, required=False)  # Corregido el nombre de 'max_lenght'

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.is_staff = False

        if commit:
            user.save()
            # Asignación a grupo (si es necesario)
            # group = Group.objects.get(name='owners')
            # user.groups.add(group)

        # Crea un perfil asociado al usuario
        profile = Profile.objects.create(
            user=user,
            phone_number=self.cleaned_data['phone_number'],  # Añadir si tu modelo Profile tiene un campo para el número de teléfono
            address=self.cleaned_data['address']  # Añadir si tu modelo Profile tiene un campo para la dirección
        )

        return user
