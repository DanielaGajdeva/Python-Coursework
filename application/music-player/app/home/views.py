from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import home
from forms import AlbumForm, SongForm
from .. import db
from ..models import Album, Song, User

@home.route('/')
def homepage():
    return render_template('/index.html', title="Welcome")

@home.route('/albums', methods=['GET', 'POST'])
@login_required
def albums():
    
    albums = Album.query.filter_by(user_id = current_user.id).all()
    return render_template('/home/albums.html',
                           albums=albums, title="All Albums")


@home.route('/albumdetails/<int:album_id>')
@login_required
def albumdetails(album_id):
    album = Album.query.get_or_404(album_id)
    songs = Song.query.filter_by(album_id=album_id).all()
    return render_template('/home/albumdetails.html', album=album, songs=songs, title="Album Details")


@home.route('/createalbum', methods=['GET', 'POST'])
@login_required
def createalbum():
    user = User.query.get(current_user.id)
    form = AlbumForm()
    if form.validate_on_submit():
        album = Album(name=form.name.data,
                        picturelink=form.picturelink.data,
                        user_id=user.id, 
                        songs=[])
        
        user.albums.append(album)
        db.session.add(album) 
        db.session.commit()

        return redirect('albums')

    return render_template('/home/createalbum.html', action="Add",
                            form=form, title="Add album")

@home.route('/deletealbum/<int:album_id>', methods=['GET', 'POST'])
@login_required
def delete_album(album_id):
    songs = Song.query.filter_by(album_id=album_id).all()
    for s in songs:
        db.session.delete(s)
        db.session.commit()
        
    album = Album.query.get(album_id)
    db.session.delete(album)
    db.session.commit()

    return redirect('/albums')

@home.route('/song/<int:song_id>')
@login_required
def song(song_id):
    song = Song.query.get(song_id)
    return render_template('/home/song.html', song=song, title="Song")
    
@home.route('/home/createsong/<int:album_id>', methods=['GET', 'POST'])
@login_required
def createsong(album_id):
    album = Album.query.get(album_id)
    form = SongForm()
    if form.validate_on_submit():
        song = Song(name=form.name.data,
                        link=form.link.data,
                        album_id=album.id)
        
        album.songs.append(song)
        db.session.add(song) 
        db.session.commit()

        return redirect('/albums')

    return render_template('/home/createsong.html', action="Add",
                           form=form, title="Add song")


@home.route('/deletesong/<int:song_id>', methods=['GET', 'POST'])
@login_required
def delete_song(song_id):
    song = Song.query.get_or_404(song_id)
    db.session.delete(song)
    db.session.commit()

    return redirect('/albums')
