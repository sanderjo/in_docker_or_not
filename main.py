#!/usr/bin/env python3

def check_docker():
    # Trick 1: if in docker, /proc/1/cgroup contains docker
    DOCKER = False
    try:
        with open("/proc/1/cgroup", "rt") as ifh:
            DOCKER = ":/docker/" in ifh.read()
    except:
        pass


    # Trick 2: if in docker and privileged docker, then /proc/sys/vm/swappiness is writable
    DOCKER_PRIVILEGED = False
    if DOCKER:
        try:
            f = open("/proc/sys/vm/swappiness", "a")
            f.close()
            print("writable!")
            DOCKER_PRIVILEGED = True
        except:
            DOCKER_PRIVILEGED = False
            print("not writable")
            # sys.exit(0)

    return DOCKER, DOCKER_PRIVILEGED

if __name__ == '__main__':

    print(check_docker())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
