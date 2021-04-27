from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem

# Import app and db from events_app package so that we can run app
from grocery_app import app, db
from grocery_app.forms import GroceryStoreForm, GroceryItemForm

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)

@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    #Creates a GroceryStoreForm
    form= GroceryStoreForm()

    if form.validate_on_submit():
        new_GroceryStore = GroceryStore(
            title=form.title.data,
            address=form.address.data,
        )
        db.session.add(new_GroceryStore)
        db.session.commit()

        flash('New GroceryStore was created successfully!')
        return redirect(url_for('main_store_detail'))
    
    return render_template('new_store.html')

@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    #Creates a Newitem form
    form = GroceryItemForm()
      
    if form.validate_on_submit():
        new_GroceryItem = GroceryItem(
            name=form.name.data,
            price=form.price.data,
            category=form.category.data,
            photo_url=form.photo_url.data,
            store=form.store.data,
        )
        db.session.add(new_GroceryItem)
        db.session.commit()

        flash('New GroceryItem was created successfully')
        return redirect(url_for('main_item_detail'))
    
    return render_template('new_item.html')

@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    store = GroceryStore.query.get(store_id)
    #Creates a GroceryStoreForm 
    store = GroceryStore.query.get(store_id)
    form = GroceryStoreForm(obj=store)
    
    if form.validate_on_submit():
        new_GroceryStore = GroceryStore(
            title=form.title.data,
            address=form.address.data,
        )
        db.session.add(new_GroceryStore)
        db.sesssion.commit()

        flash('New GroceryStore was created')
        return redirect(url_for('main.store_detail', store_id=new_GroceryStore.id))


    store = GroceryStore.query.get(store_id)
    return render_template('store_detail.html', store=store, form=form)

@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    form = GroceryItemForm(obj=item)

    if form.validate_on_submit():
        new_GroceryItem = GroceryItem(
            name=form.name.data,
            price=form.price.data,
            category=form.category.data,
            photo_url=form.photo_url.data,
            store=form.store.data,     
        )
        db.session.add(new_GroceryItem)
        db.session.commit()
    
        flash('New GroceryItem was created successfully')
        return redirect(url_for('main.item_detail', item_id=new_GroceryItem.id))

    
    item = GroceryItem.query.get(item_id)
    return render_template('item_detail.html', item=item)
