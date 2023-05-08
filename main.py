import streamlit as st
import pymongo 

# Define the correct login credentials
CORRECT_USERNAME = "streamlit"
CORRECT_PASSWORD = "password123"

# Create a function to check if the login credentials are correct
def authenticate(username, password):
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        return True
    else:
        return False
    
def dataConnectivity():
    conn_str = "mongodb://project3343:rsproject@ac-gjl3aea-shard-00-00.sop0wqm.mongodb.net:27017,ac-gjl3aea-shard-00-01.sop0wqm.mongodb.net:27017,ac-gjl3aea-shard-00-02.sop0wqm.mongodb.net:27017/?ssl=true&replicaSet=atlas-xr3bsz-shard-0&authSource=admin&retryWrites=true&w=majority"
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    print("Whole stuff running Again!")
    try:
        print(client.server_info())
    except Exception:
        print("Unable to connect to the server.")
    db = client.resumeDB
    jd = db.jd
    print(db.list_collection_names())
    return jd



def jd():
    st.success('Login successful!')
# create an empty list to store tasks
    tasks = []
    st.header("JD panel")
# create a single text input for all tasks and split them by newline
    tasks_input = st.text_area("Enter the Job description")

# split tasks by newline and append them to the tasks list
    tasks = tasks_input.split("\n")

# create a button to add tasks to the list
    if st.button("Add the list of job descriptions"):
        jd = dataConnectivity()
        jdNumber = jd.count_documents({})
        for task in tasks:
            jdNumber = jdNumber + 1
            name = f"JD {jdNumber}"
            jd.insert_one({"name":name,"desc": task})
            st.write(f"- {task}")

# create a button to remove tasks from the list
    if st.button("Remove JD"):
        jdCollection = dataConnectivity()
        jdCollection.delete_many({})
        st.write("JD removal successful")

# create a button to show all tasks in the list
    if st.button("Show JD list"):
        jdCollection = dataConnectivity()
        if jdCollection.count_documents({}) != 0:
            jd = jdCollection.find({})
            for i, task in enumerate(jd, start=1):
                st.write(f"JD {i}: {task['desc']}")
        else:
            st.write("No job descriptions added yet.")


# Define the Streamlit app
def app():
    # Set page title
    st.set_page_config(page_title='Authentication Example')
    
    if "option" not in st.session_state:
        st.session_state["option"] = None

    if "logged" not in st.session_state:
        st.session_state["logged"] = None

    # Add a title
    container = st.empty()
    
    if st.session_state["logged"] == None:
        with container.container():
            st.title('The New Login')
    
            # Add form inputs for username and password
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')
    
            # Add a button to submit the login credentials
            submitted = st.button('Submit')
    
            # Check if the login credentials are correct and print "Hello, World!" if they are
            if submitted:
                if authenticate(username, password):
                    st.session_state["logged"] = True
                    st.session_state["option"] = True
                    container.empty()
                else:
                    st.error('Invalid username or password')
    if st.session_state["option"] is not None:
        jd()

if __name__ == '__main__':
    app()
