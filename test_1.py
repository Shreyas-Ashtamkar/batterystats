# just for showing passed
from .batterystats import Battery

def test_instance():
    assert isinstance(Battery(), Battery)

def test_datetime():
    assert isinstance(Battery().date, str)
    assert isinstance(Battery().time, str)


if __name__ == '__main__':
    try:
        test_instance()
        test_datetime()
        print("All test ran successfully")
    except Exception as e:
        print(e)

