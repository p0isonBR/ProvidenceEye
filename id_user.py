def UserID(message):

    if message.from_user.id == 1054600955:
        return '`Ola mestre supremo do universo`'
    else:
        return f'*Nome*: `{message.from_user.first_name}`\n*Username*: `{message.from_user.username}`\n*ChatID*: `{message.from_user.id}`'