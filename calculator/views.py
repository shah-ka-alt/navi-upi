from django.shortcuts import render, redirect
from datetime import datetime, timedelta


def form(request):
    if request.method == 'POST':
        amount = request.POST('number')
        return redirect('transaction')
    
    return render(request, 'form.html')



def transaction(request):
    amount = request.POST.get('number')
    date = datetime.now().strftime("%Y-%m-%d")
    current_time_gmt = datetime.utcnow()
    ist_offset = timedelta(hours=5, minutes=30)
    current_time_ist = current_time_gmt + ist_offset
    time = current_time_ist.strftime("%H:%M:%S")
    month_codes = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
    month = month_codes[datetime.now().month]
    day = datetime.now().date
    year = datetime.now().year
    return render(request, 'transaction.html', locals())
