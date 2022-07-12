from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name="portal_homepage"),

    path('metrics', views.metrics, name="portal_metrics"),
    path('metrics/server', views.metrics_server, name="metrics_server"),
    path('metrics/website', views.metrics_website, name="metrics_website"),

    path('account', views.account, name="portal_account"),
    path('account/billing', views.account_billing, name="account_billing"),
    path('account/server-upgrades', views.account_server_upgrades, name="account_server_upgrades"),

    path('support', views.support, name="portal_support"),
    # path('billing', views.billing, name="portal_billing"),
    # path('billing/stripe', views.stripe_customer_portal, name="portal_billing_stripe"),
    # path('website-metrics', views.website_metrics, name="portal_website_metrics"),
    # path('server-metrics', views.server_metrics, name="portal_server_metrics"),
    # path('upgrades', views.upgrades, name="portal_server_upgrades"),
    # path('dns-records', views.dns_records, name="portal_dns_records"),
    # path('add-features', views.add_features, name="portal_add_features"),
    # path('priority-support', views.priority_support, name="portal_priority_support"),

    path('account/', include('allauth.urls')),
]