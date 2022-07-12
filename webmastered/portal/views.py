from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import messages
from django.template import loader
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.cache import cache_page

import stripe

from . import tools
from business.models import ServerUpgrade
from business.forms import ServerUpgradeForm


@login_required(login_url=settings.LOGIN_URL)
def homepage(request):
    this_user = request.user

    if not tools.is_client(this_user):
        messages.error(request, "You cannot access the client portal as you are not a client. If this is a mistake, "
                                "please contact the WM team.")
        if tools.is_staff(this_user):
            messages.warning(request, "You have been redirected to the admin portal as you are staff")
            return redirect('/engine')
        return redirect('/')
    else:
        this_client = tools.get_client(this_user)

    template = loader.get_template('portal/pages/home.html')

    context = {
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url=settings.LOGIN_URL)
def metrics(request):
    this_user = request.user

    if not tools.is_client(this_user):
        messages.error(request, "You cannot access the client portal as you are not a client. If this is a mistake, "
                                "please contact the WM team.")
        if tools.is_staff(this_user):
            messages.warning(request, "You have been redirected to the admin portal as you are staff")
            return redirect('/engine')
        return redirect('/')
    else:
        this_client = tools.get_client(this_user)

    template = loader.get_template('portal/pages/metrics.html')

    context = {
    }
    return HttpResponse(template.render(context, request))


@cache_page(60 * 15)
@vary_on_cookie
@login_required(login_url=settings.LOGIN_URL)
def metrics_server(request):
    this_user = request.user

    if not tools.is_client(this_user):
        messages.error(request, "You cannot access the client portal as you are not a client. If this is a mistake, "
                                "please contact the WM team.")
        if tools.is_staff(this_user):
            messages.warning(request, "You have been redirected to the admin portal as you are staff")
            return redirect('/engine')
        return redirect('/')
    else:
        this_client = tools.get_client(this_user)

    do_droplet = tools.Droplet(request, this_client)

    template = loader.get_template('portal/pages/metrics_server.html')

    context = {
        "region": do_droplet.region,
        "status": do_droplet.status,
        "cpu": do_droplet.cpu,
        "memory": do_droplet.memory,
        "disk": do_droplet.disk,
    }
    return HttpResponse(template.render(context, request))


@cache_page(60 * 15)
@vary_on_cookie
@login_required(login_url=settings.LOGIN_URL)
def metrics_website(request):
    this_user = request.user

    if not tools.is_client(this_user):
        messages.error(request, "You cannot access the client portal as you are not a client. If this is a mistake, "
                                "please contact the WM team.")
        if tools.is_staff(this_user):
            messages.warning(request, "You have been redirected to the admin portal as you are staff")
            return redirect('/engine')
        return redirect('/')
    else:
        this_client = tools.get_client(this_user)

    cf_data = tools.Cloudflare(request, this_client)

    template = loader.get_template('portal/pages/metrics_website.html')

    context = {
        "httpRequests1hGroups": cf_data.httpRequests1hGroups,
        "httpRequests1dGroups": cf_data.httpRequests1dGroups,
        "httpRequests1dChoroplethMap": cf_data.httpRequests1dChoroplethMap,
        'httpRequests1hGroupsTables': cf_data.httpRequests1hGroupsTables,
        'firewallEventsHistoryTable': cf_data.firewallEventsHistoryTable,
    }

    return HttpResponse(template.render(context, request))


@login_required(login_url=settings.LOGIN_URL)
def account(request):
    this_user = request.user

    if not tools.is_client(this_user):
        messages.error(request, "You cannot access the client portal as you are not a client. If this is a mistake, "
                                "please contact the WM team.")
        if tools.is_staff(this_user):
            messages.warning(request, "You have been redirected to the admin portal as you are staff")
            return redirect('/engine')
        return redirect('/')
    else:
        this_client = tools.get_client(this_user)

    template = loader.get_template('portal/pages/account.html')

    context = {
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url=settings.LOGIN_URL)
def account_billing(request):
    this_user = request.user

    if not tools.is_client(this_user):
        messages.error(request, "You cannot access the client portal as you are not a client. If this is a mistake, "
                                "please contact the WM team.")
        if tools.is_staff(this_user):
            messages.warning(request, "You have been redirected to the admin portal as you are staff")
            return redirect('/engine')
        return redirect('/')
    else:
        this_client = tools.get_client(this_user)

    template = loader.get_template('portal/pages/account_billing.html')


    stripe_customer_id = this_client.stripe_customer_id
    stripe.api_key = settings.STRIPE_API_KEY
    returnPath = str(request.build_absolute_uri()).replace('/stripe', '').replace('/billing', '')
    try:
        session = stripe.billing_portal.Session.create(
            customer=str(stripe_customer_id),
            return_url=returnPath
        )
        return redirect(session.url)
    except Exception as e:
        template = loader.get_template('portal/pages/billing-error.html')
        context = {
            'page_title': "Billing",
        }
        return HttpResponse(template.render(context, request))


@login_required(login_url=settings.LOGIN_URL)
def account_server_upgrades(request):
    this_user = request.user

    if not tools.is_client(this_user):
        messages.error(request, "You cannot access the client portal as you are not a client. If this is a mistake, "
                                "please contact the WM team.")
        if tools.is_staff(this_user):
            messages.warning(request, "You have been redirected to the admin portal as you are staff")
            return redirect('/engine')
        return redirect('/')
    else:
        this_client = tools.get_client(this_user)

    template = loader.get_template('portal/pages/account_server_upgrades.html')

    form_exists = False
    if request.method == 'POST':
        if ServerUpgrade.objects.filter(user=this_client.user).exists():
            existing_form_instance = ServerUpgrade.objects.get(user=this_client.user)
            existing_form_instance.delete()
            upgrade_form = ServerUpgradeForm(request.POST, user=this_client.user, readOnlyMode=False)
            messages.success(request, "Your upgrade request has been deleted. If this was accidental, please contact "
                                      "the WM team.")
        else:
            upgrade_form = ServerUpgradeForm(request.POST, user=this_client.user, readOnlyMode=False)
            if upgrade_form.is_valid():
                upgrade_form.save()
                messages.success(request, "Your upgrade request has been submitted, we will get back to you soon.")
                return redirect("/portal/account/server-upgrades")
    else:
        if ServerUpgrade.objects.filter(user=this_client.user).exists():
            existing_form_instance = ServerUpgrade.objects.get(user=this_client.user)
            upgrade_form = ServerUpgradeForm(user=this_client.user, instance=existing_form_instance, readOnlyMode=True)
            form_exists = True
        else:
            upgrade_form = ServerUpgradeForm(user=this_client.user, readOnlyMode=False)

    context = {
        'upgrade_form': upgrade_form,
        'form_exists': form_exists,
    }

    return HttpResponse(template.render(context, request))

@login_required(login_url=settings.LOGIN_URL)
def support(request):
    this_user = request.user

    if not tools.is_client(this_user):
        messages.error(request, "You cannot access the client portal as you are not a client. If this is a mistake, "
                                "please contact the WM team.")
        if tools.is_staff(this_user):
            messages.warning(request, "You have been redirected to the admin portal as you are staff")
            return redirect('/engine')
        return redirect('/')
    else:
        this_client = tools.get_client(this_user)

    template = loader.get_template('portal/pages/support.html')

    context = {
    }
    return HttpResponse(template.render(context, request))