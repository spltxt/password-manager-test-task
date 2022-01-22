from django.shortcuts import render, redirect
from .models import Account
from .forms import AccountForm

def AccountView(request):
    accounts = Account.objects.all()
    context = {
        'accounts': accounts,
    }
    return render(request, 'core.html', context)

def CreateAccount(request):
    form = AccountForm()

    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts')

    context = {
        'form': form
    }
    return render(request, "create-account.html", context)

def ViewAccount(request, pk):
    accountObj = Account.objects.get(id=pk)
    context = {
        'account': accountObj
    }
    return render(request, "account-details.html", context)

def EditAccount(request, pk):
    account = Account.objects.get(id=pk)
    form = AccountForm(instance=account)

    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)

        if form.is_valid():
            form.save()
            return redirect('accounts')

    context = {
        'form': form
    }
    return render(request, "create-account.html", context)

def DeleteAccount(request, pk):
    account = Account.objects.get(id=pk)
    context = {
        'account': account
    }
    if request.method == "POST":
        account.delete()
        return redirect('accounts')

    return render(request, "delete-account.html", context)

    
