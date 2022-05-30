# Movie-Quick
Movie-Quick is a movie recommendation website which is based on content-based filtering using cosine similarity and CountVectorizer algorithm. 
Here, the popularity feature is also included for better user experience.
I used TMDB dataset which I accessed from Kaggle to build the system. 
CountVectorizer creates a matrix in which each unique word is represented by a column of the matrix, and each text sample from the document is a row in the matrix.
Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.
I have also used bag of words method where all the words are collected and its frequency of occurence has been noted.

Check out the website: https://movie-quick.herokuapp.com/

# Note
I was unable to upload some dataset due to exceeding size limit. Hence, I have uploaded the datasets in drive, whose link is given below.
For accessing the dataset- https://drive.google.com/file/d/1Zm2HQBD-mJ8EVGEOvz0SwIKz5H8qjha0/view?usp=sharing

# Cosine Similarity
<!-- ![70401457-a7530680-1a55-11ea-9158-97d4e8515ca4](https://user-images.githubusercontent.com/76248901/170921129-3757 -->
Cosine similarity is measured by the cosine of the angle between two vectors. It is often used to measure document similarity in text analysis. 
It is often used for high dimensional data. It is also to note that the distance here is inversely proportional to similarity.
![70401457-a7530680-1a55-11ea-9158-97d4e8515ca4](https://user-images.githubusercontent.com/76248901/170921129-3757584f-e377-4083-8ed0-552bc4fda6c3.png)

# Flowchart
![Screenshot (86)](https://user-images.githubusercontent.com/76248901/170921352-bb4dcb22-a99b-42bd-abf1-8f6027359a25.png)

# Working
Searching or selecting the movie from the selectbox will show you the top movies which are similar to the selected movie and also has a rating above a certain value.
On clicking on the 'Click' will lead you to the TMDB page containing all the details of the movie.
There is also a 'Popular Picks' section that allows the user to not miss on personal favorites of other user.
