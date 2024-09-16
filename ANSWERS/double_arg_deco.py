from functools import wraps


def double_arg(old_func):

    @wraps(old_func)
    def _(*args, **kwargs):
        args = list(args)
        arg_info = [*old_func.__annotations__.items()]
        for i, (arg, info) in enumerate(zip(args, arg_info)):
            if info[1] in (int, float):
                args[i] *= 2
        return old_func(*args, **kwargs)

    return _

@double_arg
def f1(a: str, b: int) -> str:
    return a * b


@double_arg
def f2(a: float, b: float) -> float:
    return a * b


print(f1("Python", 5))
print(f1("typing!", 2))
print(f2(1.2, 1.2))
print(f2(1.0, 5.0))
print(f2(3.6, 8.932))

