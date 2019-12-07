SELECT user_profile.country ,corr(user_profile.age,artists.plays) as canciones FROM user_profile JOIN artists on artists.user_mboxsha1 = user_profile.user_mboxsha1 and artists.artist_name = 'metallica' 
    GROUP BY user_profile.country
    ORDER BY canciones DESC;
