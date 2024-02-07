token = serializer.dumps(user.id, salt='password-reset')
reset_link = f'https://yourdomain.com/reset-password/{token}'