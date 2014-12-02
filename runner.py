__author__ = 'sid'

from multiprocessing import Pool, Process, Queue

import click

import crawler_category
from crawler_category import *
import crawler_app
from crawler_app import *


def run_cat(cat_name, cat_url):
    os.makedirs(DATA_DIR + '/' + cat_name, 0o777, True)
    done = 0
    while done == 0:
        try:
            getAppsInCategory(cat_name, cat_url, True)
            done = 1
            print(cat_name, 'Done!!!')
        except:
            pass


def run_all_cats():
    f = open(DATA_DIR + '/' + DATA_APP_CAT_FILE)
    for line in f:
        url = line.partition(',')[0]
        print(url)
        m = re.search('ios-(\w|-)+', url)
        cat = m.group(0)
        print(cat)
        run_cat(cat, url)


def get_cat_apps(q, i):
    app_url_file = q.get()

    done = 0
    while done == 0:
        try:
            app_count = 0
            print('processing', app_url_file)
            f = open(app_url_file)
            for line in f:
                print('worker:', i)
                app_detail = getAppDetails(line)
                pickle_app(app_detail)
                app_count += 1
                if app_count % 10 == 0:
                    time.sleep(0.5)
            f.close()
            done = 1
        except:
            pass

    print(app_count, 'apps in name')
    return app_count


def run_all_apps():
    total_apps = 0
    q = Queue()
    print('get all apps')
    for name in os.listdir('./' + DATA_DIR):
        name = './' + DATA_DIR + '/' + name
        if os.path.isdir(name):
            app_url_file = name + '/' + DATA_APP_URL_FILE
            if os.path.exists(app_url_file):
                q.put(app_url_file)

    for num in range(2):
        Process(target=get_cat_apps, args=(q, num)).start()

    # with Pool(processes=4) as pool:
    #     result = pool.apply_async(get_cat_apps, (q,))
    #     print('main_process')
    #     pool.close()
    #     pool.join()
        #total_apps += result

    print('Dump', total_apps, 'apps from appstore')


@click.group()
def cli():
    return


@cli.command()
@click.option('--cat', is_flag=True, help='get all categories and urls')
@click.option('--url', is_flag=True, help='get all app urls')
@click.option('--app', is_flag=True, help='get all app data')
def crawler(cat, url, app):
    if cat:
        getAllCategories(True)
    elif url:
        run_all_cats()
    elif app:
        run_all_apps()


def main():
    cli()


if __name__ == '__main__':
    main()

