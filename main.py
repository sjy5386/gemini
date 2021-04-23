import hashlib
import os


def search(dirname):
    arr = []
    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            arr.append(os.path.join(path, filename))
    return arr


def update(files):
    dic = {}
    for filename in files:
        f = open(filename, mode='rb')
        data = f.read()
        f.close()
        m = get_sha512(data)
        if m in dic.keys():
            dic[m].append(filename)
        else:
            dic[m] = [filename]
    return dic


def get_sha512(data):
    m = hashlib.sha512()
    m.update(data)
    return m.digest()


if __name__ == '__main__':
    dirname = input("Dirname: ")
    files = search(dirname)
    dic = update(files)
    for key in dic.keys():
        if len(dic[key]) > 1:
            print(dic[key])
