def paginate(func):
    def func_wrapper(*args, **kwargs):
        if kwargs.get("follow"):
            if kwargs.get("maximum"):
                m = kwargs.get("maximum")
            else:
                m = 20
            # Start at user defined offset
            if kwargs.get("offset"):
                offset = kwargs.get("offset")
            else:
                offset = 0
            # Fetch pages until we hit an empty list
            while True:
                r = func(offset=offset, *args, **kwargs)
                print(r)
                if not r:
                    break
                if not r.get("result").get("data").get("list"):
                    break
                offset += m
        else:
            return func(*args, **kwargs)

    return func_wrapper