import time
import wjx


def main():
    t = 0
    while t <= 30:
        try:
            wjx._run()
        except:
            continue
        t += 1
        print('next...')
        time.sleep(1)
        


if __name__ == "__main__":
    main()
