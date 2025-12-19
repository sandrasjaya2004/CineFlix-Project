from django.shortcuts import render,redirect

from django.views import View

from . models import SubscriptionPlans

from . forms import SubscriptionPlanForm

# Create your views here.

class SubscriptionsView(View):

    template = 'subscriptions/subscription-list.html'

    def get(self,request,*args,**kwargs):

        plans = SubscriptionPlans.objects.all()

        data = {'plans':plans}

        return render(request,self.template,context=data)
    
class SubscriptionCreateView(View):

    form_class = SubscriptionPlanForm

    template = 'subscriptions/subscription-create.html'

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data = {'page':'Create Movie',
                'form':form
                }

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():

            form.save()
            
            return redirect('subscription-list')
        
        data = {'form':form,'page':'Create Subscription'}
        
        return  render(request,self.template,context=data)