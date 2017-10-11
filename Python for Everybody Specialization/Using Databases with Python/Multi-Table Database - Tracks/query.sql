SELECT Track.title as Track, Artist.name as Artist, Album.title as Album, Genre.name as Genre
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name, Track.title LIMIT 3