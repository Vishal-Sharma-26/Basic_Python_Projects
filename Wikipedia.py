import wikipedia

def search_wikipedia(query):
    try:
        # Use the summary function to get a brief summary of the page
        result = wikipedia.summary(query, sentences=5)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        # If the query is ambiguous, display options to the user
        options = e.options[:5]  # Display first 5 options
        return f"Your search term is ambiguous. Did you mean one of these? {', '.join(options)}"
    except wikipedia.exceptions.PageError:
        return "Sorry, no matching page found on Wikipedia."

def main():
    print("Welcome to Wikipedia Search!")
    while True:
        query = input("Enter what you want to search for (or 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Exiting...")
            break
        else:
            result = search_wikipedia(query)
            print(result)
            print()  # Add a newline for better readability

if __name__ == "__main__":
    main()
