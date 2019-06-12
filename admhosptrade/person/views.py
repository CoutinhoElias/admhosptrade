# from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from admhosptrade.person.forms import PersonForm


def person_create1(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.save()
            # form.save_m2m()

            return HttpResponseRedirect('/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            print(form)
            return render(request, 'person_create_contact.html', {'form': form})
    else:
        context = {'form': PersonForm()}
        return render(request, 'person_create_contact.html', context)


def person_create(request):
    # Cria variável na session
    # request.session['person_id'] = 1

    if request.method == 'POST':
        form = PersonForm(request.POST)

        # # Retira toda validação do campo
        # form.errors.pop('user')

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return HttpResponseRedirect('/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            return render(request, 'person_create.html', {'form': form})
    else:
        context = {'form': PersonForm()}

        # Exclui variável da session
        # del request.session['person_id']

        return render(request, 'person_create.html', context)


# def person_create2(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         formset = ContactFormSet(request.POST)
#
#         if form.is_valid() and formset.is_valid():
#             with transaction.atomic():
#
#                 person_form = form.save()
#                 formset.instance = person_form
#                 formset.save()
#
#                 return redirect('/')
#
#     else:
#         form = PersonForm()
#
#         formset = ContactFormSet()
#
#     forms = [formset.empty_form] + formset.forms
#     context = {'form': form, 'formset': formset, 'forms': forms}
#     return render(request, 'person_create_contact.html', context)
