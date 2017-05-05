
1. Find the user with the email cats@gmail.com.
    User.query.filter(User.email == 'cats@gmail.com').all()
    User.query.filter(email = 'cats@gmail.com').all()
    db.session.query(User).filter(User.email == 'cats@gmail.com').all()

2. Find any movies with the exact title “Cape Fear.”
    Movie.query.filter(Movie.title == 'Cape Fear').all()
    db.session.query(Movie).filter(Movie.title == 'Cape Fear').all()

3. Find all users with the zipcode 90703.
    User.query.filter(User.zipcode == '90703').all()
    db.session.query(User).filter(User.zipcode == '90703').all()

4. Find all ratings of with the score of 5.
    Rating.query.filter(Rating.score == '5').all()
    db.session.query(Rating).filter(Rating.score == '5').all()

5. Find the rating for the movie whose id is 7, from the user whose id is 6.
    Rating.query.filter(Rating.movie_id == '7', Rating.user_id == '6').all()
    db.session.query(Rating).filter(Rating.movie_id == '7', Rating.user_id == '6').all()

6. Find all ratings that are larger than 3.
    Rating.query.filter(Rating.score > '3').all()
    db.session.query(Rating).filter(Rating.score > '3').all()

