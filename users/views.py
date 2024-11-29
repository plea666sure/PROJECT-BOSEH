from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Akun, Customer, Admin
from .forms import CustomerRegisterForm, CustomerLoginForm

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = make_password(form.cleaned_data['password'])

            # Buat akun baru
            akun = Akun.objects.create(username=username, password=password, role='customer')

            # Buat data customer
            customer = form.save(commit=False)
            customer.id_akun = akun
            customer.save()

            return redirect('login')
    else:
        form = CustomerRegisterForm()
    return render(request, 'users/register_customer.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            akun = Akun.objects.get(username=username)
            if check_password(password, akun.password):
                # Set session berdasarkan role
                request.session['akun_id'] = akun.id
                if akun.role == 'customer':
                    return redirect('home_customer')
                elif akun.role == 'admin':
                    return redirect('admin_dashboard')
            else:
                return render(request, 'users/login.html', {'error': 'Password salah.'})
        except Akun.DoesNotExist:
            return render(request, 'users/login.html', {'error': 'Akun tidak ditemukan.'})

    return render(request, 'users/login.html')

def home_customer(request):
    akun_id = request.session.get('akun_id')
    if akun_id:
        try:
            customer = Customer.objects.get(id_akun_id=akun_id)
            return render(request, 'users/home_customer.html', {'customer': customer})
        except Customer.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')

def admin_dashboard(request):
    akun_id = request.session.get('akun_id')
    if akun_id:
        try:
            admin = Admin.objects.get(id_akun_id=akun_id)
            return render(request, 'users/admin_dashboard.html', {'admin': admin})
        except Admin.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')

def logout(request):
    request.session.flush()
    return redirect('login')
