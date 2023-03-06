from sqlalchemy import and_

from src import db, app
from src.database import models

with app.app_context():
    films = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()
    harry_potter_and_deadly_hallows_part1 = db.session.query(models.Film).filter(
        models.Film.title == 'Harry Potter and the Deathly Hallows part 1'
    ).first()
    harry_potter_and_deadly_hallows_part2 = db.session.query(models.Film).filter_by(title='Harry Potter and the Deathly Hallows part 2'
    ).first()
    deathly_hallows = db.session.query(models.Film).filter(
        models.Film.title.ilike('%deathly hallows%')
    ).all()
    print(deathly_hallows)
    films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
    print(films_with_actors)