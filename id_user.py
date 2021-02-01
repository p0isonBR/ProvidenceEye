def UserID(message):

    if message.from_user.id == 1054600955:
        return '`Ola mestre supremo do universo`'
    else:
        return '''*Nome*: `{message.from_user.first_name}`
*Username*: `{message.from_user.username}`
*ChatID*: `{message.from_user.id}`'''