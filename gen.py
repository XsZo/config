import yaml

# filter

listFilter = [
    'direct', 'block',
    'global', 'system', 'game',
    'region', 'r-cn', 'r-jp', 'r-tw', 'r-us'
]

for label in listFilter:
    with open('src/filter/' + label + '.yml', 'tr') as file:
        src = yaml.safe_load(file)

    flagDomain = 'domain' in src
    if flagDomain:
        src['domain'].sort()
    flagIp = 'ip' in src
    if flagIp:
        src['ip'].sort()
    flagIp6 = 'ip6' in src
    if flagIp6:
        src['ip6'].sort()
    flagPort = 'port' in src
    if flagPort:
        src['port'].sort()

    # generate clash conf

    fileDir = 'filter/c/'
    fileExt = '.yml'
    fileStart = 'payload:\n'
    fileEnd = ''
    lineStart = '  - '
    lineEnd = '\n'

    # domain list
    if flagDomain:
        with open(fileDir + label + fileExt, 'tw') as file:
            file.write(fileStart)
            for line in src['domain']:
                if line[0] == '_':
                    file.write(lineStart + line[1:] + lineEnd)
                else:
                    file.write(lineStart + '+.' + line + lineEnd)
            file.write(fileEnd)

    # ip list
    if flagIp or flagIp6:
        with open(fileDir + label + '.ip' + fileExt, 'tw') as file:
            file.write(fileStart)
            if flagIp:
                for line in src['ip']:
                    file.write(lineStart + line + lineEnd)
            if flagIp6:
                for line in src['ip6']:
                    file.write(lineStart + line + lineEnd)
            file.write(fileEnd)

    # classical list
    if flagPort:
        with open(fileDir + label + '.ms' + fileExt, 'tw') as file:
            file.write(fileStart)
            for line in src['port']:
                file.write(lineStart + 'DST-PORT,' + line + lineEnd)
            file.write(fileEnd)

    # generate quantumult conf

    fileDir = 'filter/q/'
    fileExt = '.txt'
    fileStart = ''
    fileEnd = ''
    lineStart = ''
    lineEnd = ',proxy\n'

    with open(fileDir + label + fileExt, 'tw') as file:
        if flagDomain:
            for line in src['domain']:
                if line[0] == '_':
                    file.write(lineStart + 'host,' + line[1:] + lineEnd)
                else:
                    file.write(lineStart + 'host-suffix,' + line + lineEnd)
        if flagIp:
            for line in src['ip']:
                file.write(lineStart + 'ip-cidr,' + line + lineEnd)
        if flagIp6:
            for line in src['ip6']:
                file.write(lineStart + 'ip6-cidr,' + line + lineEnd)

    # generate surge conf

    fileDir = 'filter/s/'
    fileExt = '.txt'
    fileStart = ''
    fileEnd = ''
    lineStart = ''
    lineEnd = '\n'

    if flagDomain:
        with open(fileDir + label + fileExt, 'tw') as file:
            file.write(fileStart)
            for line in src['domain']:
                if line[0] == '_':
                    file.write(lineStart + 'DOMAIN,' + line[1:] + lineEnd)
                else:
                    file.write(lineStart + 'DOMAIN-SUFFIX,' + line + lineEnd)

    if flagIp or flagIp6:
        with open(fileDir + label + '.ip' + fileExt, 'tw') as file:
            file.write(fileStart)
            if flagIp:
                for line in src['ip']:
                    file.write(lineStart + 'IP-CIDR,' + line + lineEnd)
            if flagIp6:
                for line in src['ip6']:
                    file.write(lineStart + 'IP-CIDR6,' + line + lineEnd)
            file.write(fileEnd)

    if flagPort:
        with open(fileDir + label + '.ms' + fileExt, 'tw') as file:
            file.write(fileStart)
            for line in src['port']:
                file.write(lineStart + 'DEST-PORT,' + line + lineEnd)
            file.write(fileEnd)
