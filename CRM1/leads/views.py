from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
# from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic
from .models import Lead
from .forms import LeadForm, CustomUserCreationForm


# Create your views here.


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class Landing_Page(generic.TemplateView):
    template_name = "lands.html"


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "lead_create.html"
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email="magesh1699@gmail.com",
            recipient_list=["maaahi003@gmail.com"]

        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(LoginRequiredMixin,  generic.DeleteView):
    template_name = "lead_delete.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

    def get_success_url(self):
        return reverse("leads:lead-list")


def landing_page(request):
    return render(request, "lands.html")


def leads_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    context = {"lead": lead}
    print(lead)
    return render(request, "lead_detail.html", context)


def leads_list(request):
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, 'lead_list.html', context)


def lead_create(request):
    form = LeadForm
    context = {"form": form}
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    return render(request, 'lead_create.html', context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)
    context = {"lead": lead,
               "form": form}
    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    return render(request, "lead_update.html", context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
