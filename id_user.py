def UserID(message):

    return f'*Nome*: `{message.from_user.first_name}`\n*Username*: `{message.from_user.username}`\n*ChatID*: `{message.from_user.id}`'
