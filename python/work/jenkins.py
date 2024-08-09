# class Job():
#     def __init__(self, jenkins_url, jenkins_job, user, token, jenkins_server):
#
import time

from api4jenkins import Jenkins

if __name__ == '__main__':
    token = '1163a2390afe21ec865142aa1439cacfc5'
    jk_url = 'http://192.168.0.19:9902'
    serve = Jenkins(jk_url, auth=('heguiqiu', '1163a2390afe21ec865142aa1439cacfc5'))
    print(serve.version)
    item = serve.build_job('eucp-demo')
    while not item.get_build():
        print('wait build')
        time.sleep(1)
    build = item.get_build()
    while build.building:
        print('building...')
        time.sleep(1)
    print(build.building)
    print(build.result)