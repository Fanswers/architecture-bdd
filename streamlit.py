import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

st.set_page_config(page_title="Spotify top 50 / Concerts France", page_icon="🎼", layout="wide")

adresse_ip = "http://192.168.1.35:5000/"

with st.sidebar.form(key = "form1"):
    home_button = st.form_submit_button("Home")
    if home_button:
        st.experimental_rerun()

with st.sidebar.form(key = "form2"):
    # Get data
    file_data = requests.get(f"{adresse_ip}").json()
    i = 0
    for doc in file_data:
        count_concerts = 0
        if "followers" in doc.keys():
            for elem in doc["followers"]:
                file_data[i][elem] = file_data[i]["followers"][elem]
            del file_data[i]["followers"]
        if "concerts" in doc.keys():
            for elem in doc["concerts"]:
                count_concerts += 1
            file_data[i]["count_concerts"] = count_concerts
            del file_data[i]["concerts"]
        i += 1
    list_id = [elem["_id"] for elem in file_data]
    list_id.insert(0,"")
    artiste = st.selectbox('Artiste recherché:', list_id)
    submit2 = st.form_submit_button(label = "Submit")

if artiste == "":
    st.markdown("<h2 style='text-align: center; color: black;'>Dataframe des artistes qui ont prévu des concerts en france</h2>", unsafe_allow_html=True)
    st.dataframe(file_data)

    df = pd.json_normalize(file_data)
    df_only_date = df.drop(['_id', 'popularity', 'spotify_id', 'count_concerts'], axis=1)
    max_date = max(df_only_date.columns)
    # Graph top 10 followers
    df_graph = df.sort_values(by=[max_date], ascending=False).head(10)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_graph["_id"],
        y=df_graph[max_date],
        name=max_date,
        marker_color='lightsalmon'
    ))
    fig.update_layout(barmode='group', xaxis_tickangle=-45, title="")
    st.markdown(
        "<h2 style='text-align: center; color: black;'></h2>",
        unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: center; color: black;'>Les 10 artistes les plus suivis qui ont fait/prévu des concerts en France</h4>",
        unsafe_allow_html=True)
    st.plotly_chart(fig)

    st.markdown(
        "<h2 style='text-align: center; color: black;'></h2>",
        unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: center; color: black;'>Les 10 artistes qui ont fait/prévu le plus de concerts en France</h4>",
        unsafe_allow_html=True)

    df_graph = df.sort_values(by=["count_concerts"], ascending=False).head(10)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_graph["_id"],
        y=df_graph["count_concerts"],
        name=max_date,
        marker_color='blue'
    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(barmode='group', xaxis_tickangle=-45, title="")
    st.plotly_chart(fig)

    st.subheader("Ajouter un artiste")
    with st.form(key="form_add"):
        artist_name = st.text_input(label="Nom de l'artiste:")
        submit_add = st.form_submit_button(label="Submit")
        if submit_add:
            requests.post(f"{adresse_ip}", json={"_id": artist_name})
            st.experimental_rerun()
    st.subheader("Supprimer un artiste")
    with st.form(key="form_delete"):
        artist_name = st.text_input(label="Nom de l'artiste:")
        submit_delete = st.form_submit_button(label="Submit")
        if submit_delete:
            requests.delete(f"{adresse_ip}", json={"_id": artist_name})
            st.experimental_rerun()
else:
    file_data_id = requests.get(f"{adresse_ip}{artiste}").json()
    i = 0
    for doc in file_data_id:
        count_concerts = 0
        if "followers" in doc.keys():
            for elem in doc["followers"]:
                file_data_id[i][elem] = file_data_id[i]["followers"][elem]
            del file_data_id[i]["followers"]
        if "concerts" in doc.keys():
            for elem in doc["concerts"]:
                count_concerts += 1
            file_data_id[i]["count_concerts"] = count_concerts
            del file_data_id[i]["concerts"]
        i += 1
    st.markdown(f"<h1 style='text-align: center; color: black;'>{artiste}</h1>", unsafe_allow_html=True)
    st.dataframe(file_data_id)
    if "popularity" in file_data_id[0].keys():
        st.markdown(f"<h2 style='text-align: center; color: black;'>Evolution des followers de {artiste}</h2>", unsafe_allow_html=True)
        df = pd.json_normalize(file_data_id)
        if "spotify_id" in file_data_id[0].keys():
            df_melted = pd.melt(df, id_vars=["_id", "spotify_id", "popularity", "count_concerts"], var_name="date", value_name="followers")
        else:
            df_melted = pd.melt(df, id_vars=["_id", "popularity", "count_concerts"], var_name="date",
                                value_name="followers")

        fig = plt.figure(figsize=(10, 4))
        plt.ticklabel_format(style='plain', axis='y')
        plt.xticks(rotation=45)
        sns.lineplot(x="date", y="followers", data=df_melted)
        st.pyplot(fig)

    else:
        st.markdown(f"<h2 style='text-align: center; color: black;'></h2>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: black;'>{artiste} n'a pas été trouvé sur spotify</h2>",
                    unsafe_allow_html=True)

    file_data_id_concerts = requests.get(f"{adresse_ip}{artiste}").json()
    i = 0
    for doc in file_data_id_concerts:
        count_concerts = 0
        if "followers" in doc.keys():
            del file_data_id_concerts[i]["followers"]
        if "_id" in doc.keys():
            del file_data_id_concerts[i]["_id"]
        if "popularity" in doc.keys():
            del file_data_id_concerts[i]["popularity"]
        if "spotify_id" in doc.keys():
            del file_data_id_concerts[i]["spotify_id"]
        if "concerts" in doc.keys():
            for elem in doc["concerts"]:
                count_concerts += 1
                file_data_id_concerts[i][elem] = file_data_id_concerts[i]["concerts"][elem]
            del file_data_id_concerts[i]["concerts"]
        i += 1
    today = datetime.date.today()
    passed_concert = []
    next_concert = []
    for key in file_data_id_concerts[0]:
        if datetime.datetime.strptime(key, '%Y-%m-%dT%H:%M:%S').date() > today:
            next_concert.append(key)
        else:
            passed_concert.append(key)
    col_passed, blank, col_next = st.columns([2, 2, 2])
    with col_passed:
        st.markdown(f"<h3 color: black;'>Concerts passés</h3>", unsafe_allow_html=True)
        for elem in passed_concert:
            st.write(elem)
    with col_next:
        st.markdown(f"<h3 color: black;'>Concerts à venir</h3>", unsafe_allow_html=True)
        for elem in next_concert:
            st.write(elem)
    st.subheader("Modifier un artiste")
    with st.form(key="form_updaye"):
        artist_name = st.text_input(label="Nom de l'artiste:")
        new_artist_name = st.text_input(label="Nouveau nom de l'artiste:")
        artist_spotify_id = st.text_input(label="Spotify id:")
        popularity = st.number_input(label="Popularity:", min_value=0, max_value=100, value=0, step=1)
        submit_update = st.form_submit_button(label="Submit")
        if submit_update:
            requests.put(f"{adresse_ip}", json={"_id": artist_name, "new_id": new_artist_name, "spotify_id": artist_spotify_id, "popularity": int(popularity)})
            st.experimental_rerun()
