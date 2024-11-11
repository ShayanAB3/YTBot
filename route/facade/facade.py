def decorator(func):
    async def wrapper(ctx, *args, **kwargs):
        return await func(ctx, *args, **kwargs)
    return wrapper