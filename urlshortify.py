from shortener import URLShortener

def main():
    shortener = URLShortener()

    while True:
        long_url = input("Enter a long URL (or 'exit' to quit): ")
        
        if long_url.lower() == 'exit':
            break

        short_url = shortener.shorten_url(long_url)
        print(f"Shortened URL: {short_url}")

    print("Exiting URLShortify.")

if __name__ == "__main__":
    main()
