SELECT user_profile.country , sum(artists.plays) as canciones FROM user_profile JOIN artists on artists.user_mboxsha1 = user_profile.user_mboxsha1 and artists.artist_name = 'metallica' 
    GROUP BY user_profile.country
    ORDER BY canciones DESC;

SELECT user_profile.gender , sum(artists.plays) as canciones FROM user_profile JOIN artists on artists.user_mboxsha1 = user_profile.user_mboxsha1 and artists.artist_name = 'metallica' 
    GROUP BY user_profile.gender
    ORDER BY canciones DESC;

SELECT user_profile.age , sum(artists.plays) as canciones FROM user_profile JOIN artists on artists.user_mboxsha1 = user_profile.user_mboxsha1 and artists.artist_name = 'metallica' 
    GROUP BY user_profile.age
    ORDER BY canciones DESC;