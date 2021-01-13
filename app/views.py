from flask import render_template, Blueprint, request, url_for
from os import listdir
from os.path import isfile, isdir, join

main_blueprint = Blueprint('main', __name__, static_folder='static', static_url_path='/static')


@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/config')
def config():
    return render_template('config.html')

@main_blueprint.route('/filesystem/')
@main_blueprint.route('/filesystem/<safe_path>') ## 2020.11.20.11.11.11
def filesystem(safe_path=''):
    base_path = '/home/radar/rapp/app/static/images/fotos'
    up_safe_path = '.'.join(safe_path.split('.')[:-1])
    path = '/'.join(safe_path.split('.'))
    full_path = base_path + path 

    base_web_path = '/images/fotos'
    full_web_path = base_web_path + path 

    #files = [ join(full_path , f) for f in listdir(full_path) if isfile(join(full_path, f)) ]
    files = [ url_for('static', filename=full_web_path+'/'+f) for f in listdir(full_path) if isfile(join(full_path, f)) ]
    #files = [ join(full_path , f) for f in listdir(full_path) if isfile(join(full_path, f)) ]
    dirs = [ join(full_path , d) for d in listdir(full_path) if isdir(join(full_path, d)) ]
    return render_template('filesystem.html', 
                           dirs=dirs, 
                           files=files, 
                           base_path=base_path, 
                           up_safe_path=up_safe_path)


@main_blueprint.route('/carrusel/<safe_path>')
def carrusel(safe_path=''):
    base_path = '/home/radar/rapp/app/static/images/fotos'
    base_web_path = '/images/fotos'
    up_safe_path = '.'.join(safe_path.split('.')[:-1])
    path = '/'.join(safe_path.split('.'))
    full_path = base_path + path
    full_web_path = base_web_path + path 
    z_safe_path = safe_path+'.z'

    pics = [ url_for('static', filename=full_web_path+'/'+f) for f in listdir(full_path) if isfile(join(full_path, f)) ]
    return render_template('carrusel.html', pics=pics, up_safe_path=up_safe_path, z_safe_path=z_safe_path)


@main_blueprint.route('/plate', methods=['GET', 'POST'])
def plate():
    print(request.data)
    return 'PLATE'
