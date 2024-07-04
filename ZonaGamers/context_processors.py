def user_context_processor(request):
    print(f'User:  {request.user.username}')
    return {
        'username': request.user.username,
        'is_authenticated': request.user.is_authenticated
    }