ret # Return the dataframe
df12 = pd.merge(df11, df7) # Merge two previous datasets: df11 and df7

numRevs, states = [], [] # Initialize two empty lists, one for number of reviews and the other for states
for i in genreList: # For each genre in the genre list (defined above)
    most_state = df12.loc[df12[i] == True, "State"].value_counts().head(2) # Get the state with the most number of reviews for that genre
    numRevs.append(most_state[0,1]) # Append the state to the list
    states.append(most_state.index[0,1]) # Append the number of reviews to the list




ret = pd.DataFrame({
            'Genre':genreList,
            'State':states,
            '# of Reviews':numRevs,
        }) # Convert the values to dataframe

ret # Return the dataframe
df12 = pd.merge(df11, df7) # Merge two previous datasets: df11 and df7

numRevs, states = [], [] # Initialize two empty lists, one for number of reviews and the other for states
for i in genreList: # For each genre in the genre list (defined above)
    most_state = df12.loc[df12[i] == True, "State"].value_counts().head(2) # Get the state with the most number of reviews for that genre
    numRevs.append(most_state[0:]) # Append the state to the list
    states.append(most_state.index[0:]) # Append the number of reviews to the list




ret = pd.DataFrame({
            'Genre':genreList,
            'State':states,
            '# of Reviews':numRevs,
        }) # Convert the values to dataframe

ret # Return the dataframe
df12 = pd.merge(df11, df7) # Merge two previous datasets: df11 and df7

numRevs, states = [], [] # Initialize two empty lists, one for number of reviews and the other for states
for i in genreList: # For each genre in the genre list (defined above)
    most_state = df12.loc[df12[i] == True, "State"].value_counts().head(2) # Get the state with the most number of reviews for that genre
    numRevs.append(most_state[0:]) # Append the state to the list
    states.append(most_state.index[0:]) # Append the number of reviews to the list




ret = pd.DataFrame({
            'Genre':genreList,
            'State':states,
            '# of Reviews':numRevs,
        }) # Convert the values to dataframe

ret['Action'] # Return the dataframe
df12 = pd.merge(df11, df7) # Merge two previous datasets: df11 and df7

numRevs, states = [], [] # Initialize two empty lists, one for number of reviews and the other for states
for i in genreList: # For each genre in the genre list (defined above)
    most_state = df12.loc[df12[i] == True, "State"].value_counts().head(1) # Get the state with the most number of reviews for that genre
    numRevs.append(most_state[0]) # Append the state to the list
    states.append(most_state.index[0]) # Append the number of reviews to the list




ret = pd.DataFrame({
            'Genre':genreList,
            'State':states,
            '# of Reviews':numRevs,
        }) # Convert the values to dataframe

ret # Return the dataframe
for i in genreList:
    print(df12.loc[df12[i] == True, "State"].value_counts())

for i in genreList:
    print(i, df12.loc[df12[i] == True, "State"].value_counts())

for i in genreList:
    print(i, df12.loc[df12[i] == True, "State"].value_counts()).head(2)

for i in genreList:
    print(i, df12.loc[df12[i] == True, "State"].value_counts().head(2))

df12 = pd.merge(df11, df7) # Merge two previous datasets: df11 and df7

numRevs, states = [], [] # Initialize two empty lists, one for number of reviews and the other for states
for i in genreList: # For each genre in the genre list (defined above)
    most_state = df12.loc[df12[i] == True, "State"].value_counts().head(1) # Get the state with the most number of reviews for that genre
    numRevs.append(most_state[0]) # Append the state to the list
    states.append(most_state.index[0]) # Append the number of reviews to the list


ret = pd.DataFrame({
            'Genre':genreList,
            'State':states,
            '# of Reviews':numRevs,
        }) # Convert the values to dataframe

ret # Return the dataframe

## ---(Mon Apr  8 14:13:48 2019)---
import numpy
import pandas

files = open('Stocks/')