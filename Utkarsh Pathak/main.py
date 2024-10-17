from util.DBconnutil import DbConnUtil
import datetime


def display_pet_details():
    try:
        # Get the database connection
        conn = DbConnUtil.getConnection()
        if conn is None:
            print("Could not establish a connection to the database.")
            return

        cursor = conn.cursor()  # Create a cursor from the connection

        # SQL query to fetch pet details from the "pets" table
        query = "SELECT Name, Age, Breed FROM pet"
        cursor.execute(query)

        # Fetching all rows from the executed query
        pet_details = cursor.fetchall()

        # Checking if there are available pets
        if not pet_details:
            print("No pets available in the database.")
        else:
            print("List of Pet Details:")
            for pet in pet_details:
                pet_dict = {
                    "Name": pet[0],
                    "Age": pet[1],
                    "Breed": pet[2]
                }
                print(pet_dict)  # Display each pet's details as a dictionary

    except Exception as e:
        print("Error while connecting to the database or retrieving pet details:", e)

    finally:
        # Close the cursor and connection to release resources
        try:
            cursor.close()
            conn.close()
        except Exception as close_e:
            print("Error while closing the connection:", close_e)


def display_adoption_events():
    try:
        # Get the database connection
        conn = DbConnUtil.getConnection()
        if conn is None:
            print("Could not establish a connection to the database.")
            return

        cursor = conn.cursor()  # Create a cursor from the connection

        # SQL query to fetch details of upcoming adoption events
        query = "SELECT event_id, event_name, event_date FROM adoption_events"
        cursor.execute(query)

        # Fetching all rows from the executed query
        event_details = cursor.fetchall()

        # Checking if there are available events
        if not event_details:
            print("No upcoming adoption events found.")
        else:
            print("List of Upcoming Adoption Events:")
            for event in event_details:
                event_dict = {
                    "Event ID": event[0],
                    "Event Name": event[1],
                    "Event Date": event[2]
                }
                print(event_dict)  # Display each event's details as a dictionary

    except Exception as e:
        print("Error while connecting to the database or retrieving event details:", e)

    finally:
        # Close the cursor and connection to release resources
        try:
            cursor.close()
            conn.close()
        except Exception as close_e:
            print("Error while closing the connection:", close_e)


def register_for_event(event_id, participant_name):
    try:
        # Get the database connection
        conn = DbConnUtil.getConnection()
        if conn is None:
            print("Could not establish a connection to the database.")
            return

        cursor = conn.cursor()  # Create a cursor from the connection

        # SQL query to insert the participant into the participants table
        query = """
            INSERT INTO participants (event_id, participant_name)
            VALUES (?, ?)
        """

        # Execute the query with the event ID and participant name
        cursor.execute(query, (event_id, participant_name))

        # Commit the transaction to save the changes
        conn.commit()

        # Confirmation message
        print(f"Successfully registered {participant_name} for event ID {event_id}.")

    except Exception as e:
        print("Error while registering for the event:", e)

    finally:
        # Close the cursor and connection to release resources
        try:
            cursor.close()
            conn.close()
        except Exception as close_e:
            print("Error while closing the connection:", close_e)


if __name__ == "__main__":
    while True:
        print("\nWelcome to PetPals!!")
        print("1. List Available Pets")
        print("2. Donate")
        print("3. View Adoption Events")
        print("4. Register for an Adoption Event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_pet_details()

        elif choice == '2':
            # Donation logic here (already implemented)
            pass

        elif choice == '3':
            display_adoption_events()

        elif choice == '4':
            try:
                # Prompt user for event registration details
                event_id = int(input("Enter the Event ID you wish to register for: "))
                participant_name = input("Enter your name: ")
                
                # Call the function to register the participant
                register_for_event(event_id, participant_name)
            except ValueError:
                print("Invalid input. Please enter a valid event ID.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
