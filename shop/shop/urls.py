"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from shopapp.forms import loginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path("base/",views.base,name="base"),
    path("address/",views.address,name="address"),
    path('',views.indexView.as_view(),name='index'),
    path("account/login/",auth_view.LoginView.as_view(template_name='shop\login.html', authentication_form=loginForm),name="user_login"),
    path("sign/",views.sign.as_view(),name="sign"),
    path("product_details/<int:pk>",views.product_details.as_view(),name="product_details"),
    path("mobiledata/<slug:data>",views.mobile,name="mobiledata"),
    path("mobile/",views.mobile,name="mobile"),
    path("laptopdata/<slug:data>",views.laptopView,name="laptopdata"),
    path("laptopView/",views.laptopView,name="laptopView"),

    path("topWeardata/<slug:data>",views.topWearView,name="topWeardata"),
    path("topWearView/",views.topWearView,name="topWearView"),

    path("bottomWeardata/<slug:data>",views.bottomWearView,name="bottomWeardata"),
    path("bottomWearView/",views.bottomWearView,name="bottomWearView"),
    
    path("profile/",views.profile.as_view(),name="profile"),
    path('logout/',auth_view.LogoutView.as_view(next_page='user_login'),name='logout'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='shop\passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='shop\passwordchangedone.html'),name='passwordchangedone'),

    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='shop\password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password_reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='shop\password_reset_done.html'),name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='shop\password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password_reset_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='shop\password_reset_complete.html'),name='password_reset_complete'),

    path("add-to-cart/",views.add_to_cart,name="add-to-cart"),
    path("show_cart/",views.show_cart,name="show_cart"),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),



    path('p/', views.product_list, name='product_list'),













]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
