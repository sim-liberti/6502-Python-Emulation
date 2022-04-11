from rich import print
import time
import inspect

def EXPECT_EQ(value_1, value_2):
    start = time.time()
    if value_1 == value_2:
        print("[green][ RUN     ][/green]", end="")
        print(f" {inspect.stack()[1].function}")
        print("[green][      OK ][/green]", end="")
        print(f" {inspect.stack()[1].function}", end="")
        end = time.time()
        print(f" ({round(end-start, 2)}ms)")
    else:
        print("[red][ RUN     ][/red]", end="")
        print(f" {inspect.stack()[1].function}")
        print("[red][  FAILED ][/red]", end="")
        print(f" {inspect.stack()[1].function}", end="")
        end = time.time()
        print(f" ({round(end-start, 2)}ms)")

def EXPECT_FALSE(value):
    start = time.time()
    if value == 0:
        print("[green][ RUN     ][/green]", end="")
        print(f" {inspect.stack()[1].function}")
        print("[green][      OK ][/green]", end="")
        print(f" {inspect.stack()[1].function}", end="")
        end = time.time()
        print(f" ({round(end-start, 2)}ms)")
    else:
        print("[red][ RUN     ][/red]", end="")
        print(f" {inspect.stack()[1].function}")
        print("[red][  FAILED ][/red]", end="")
        print(f" {inspect.stack()[1].function}", end="")
        end = time.time()
        print(f" ({round(end-start, 2)}ms)")

def EXPECT_TRUE(value):
    start = time.time()
    if value == 1:
        print("[green][ RUN     ][/green]", end="")
        print(f" {inspect.stack()[1].function}")
        print("[green][      OK ][/green]", end="")
        print(f" {inspect.stack()[1].function}", end="")
        end = time.time()
        print(f" ({round(end-start, 2)}ms)")
    else:
        print("[red][ RUN     ][/red]", end="")
        print(f" {inspect.stack()[1].function}")
        print("[red][  FAILED ][/red]", end="")
        print(f" {inspect.stack()[1].function}", end="")
        end = time.time()
        print(f" ({round(end-start, 2)}ms)")