from .models import Account

def get_avatar(backend, response, user=None, *args, **kwargs):
        url = None
 
        if backend.name == 'vk-oauth2':
            url = response.get('photo', '')

        elif backend.name == "facebook": 
            url=response['user']['picture']
 
        if url:
            account = Account.objects.get_or_create(user=user)
            account.avatar_link = url
            account.save()

def update_user_social_data(strategy, *args, **kwargs):
    response = kwargs['response']
    backend = kwargs['backend']
    user = kwargs['user']

    if response['picture']:
        url = response['picture']
        account = Account()
        account.user = user
        account.avatar_link = url
        account.save()