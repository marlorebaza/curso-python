from flask import Flask, render_template, request, flash, redirect
from google.cloud import datastore

app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True

@app.route('/delete_all_contacts', methods = ['GET'])
def delete_all_contacts():
    datastore_client = datastore.Client()
    keys = list(map(lambda e: e.key, datastore_client.query(kind='Contacto').fetch()))
    datastore_client.delete_multi(keys)
    return redirect('/contacts')

@app.route('/contacts', methods = ['GET'])
def list_contacts():
    datastore_client = datastore.Client()
    contacts = datastore_client.query(kind='Contacto').fetch()
    return render_template('contact_book.html', contacts=contacts)

@app.route('/add_contact', methods = ['POST', 'GET'])
def add_contact():
    
    if request.form:
        
        # FUENTE: https://cloud.google.com/datastore/docs/reference/libraries#using_the_client_library
        
        # Inicializamos el cliente del datastore
        datastore_client = datastore.Client()
        
        # Indicamos el tipo definido para la entidad
        kind = 'Contacto'
        
        # Indicamos el id para la nueva entidad que vamos a crear
        id = 'contactCustomId'
        
        # Podemos indicar la llave
        #key = datastore_client.key(kind, id)
        # ... O no hacerlo y se autogenerará una
        key = datastore_client.key(kind)
        
        # Agregamos los valores de las propiedades de la entidad a crear
        contact = datastore.Entity(key)
        contact['name'] = request.form.get('name')
        contact['phone'] = request.form.get('phone')
        contact['email'] = request.form.get('email')
        
        # Guardamos la entidad
        datastore_client.put(contact)
        
        flash('Contacto añadido!')
        return redirect('/contacts')
        
    return render_template('contact.html')


@app.route('/contacts/<uid>', methods = ['GET'])
def contact_details(uid):
    datastore_client = datastore.Client()
    key = datastore_client.key('Contacto', int(uid))
    contact = datastore_client.get(key)
    if not contact:
        return redirect('/', code=301)
    return render_template('contact.html', contact=contact)

@app.route('/delete_contact', methods = ['POST'])
def delete_contact():
    uid = request.form.get('uid')
    print(uid)
    datastore_client = datastore.Client()
    key = datastore_client.key('Contacto', int(uid))
    datastore_client.delete(key)
    flash('Contacto eliminado!')
    return redirect('/contacts')

@app.route('/put_contact', methods = ['POST'])
def put_contact():
    datastore_client = datastore.Client()
    key = datastore_client.key('Contacto', int(request.form.get('uid')))
    contact = datastore.Entity(key)
    contact['name'] = request.form.get('name')
    contact['phone'] = request.form.get('phone')
    contact['email'] = request.form.get('email')
    datastore_client.put(contact)
    #return redirect(f'/contacts/{uid}')
    flash('Contacto actualizado!')
    return redirect('/contacts')

if __name__ == '__main__':
    # Levantará un servidor web en localhost
    app.run()
