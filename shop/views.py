from typing import Any

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse

from .models import Color


class ColorListView(LoginRequiredMixin, ListView):  # Should it be a FormView?
    login_url = 'users:login'
    model = Color
    template_name = 'shop/colors.html'
    paginate_by = 5  # Should it be hardcoded?
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        color = Color.objects.get(pk=int(request.POST['color_id']))
        user = request.user
        if user.balance < color.price:
            return render(request, self.template_name, {
                'message': 'No money, no honey',
                'object_list': self.get_queryset(),  # This is probably not good!
            })
            # This won't work..
            # return self.render_to_response({
            #     'message': 'Not enough money',
            #     'object_list': self.get_queryset(),
            # })#, **kwargs)
        user.balance -= color.price
        user.colors.add(color)
        user.save()
        return redirect('shop:colors')
