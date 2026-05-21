def error():
    user = int(input("Enter a error number:"))

    match user:
        case 404:
            print("Page not found")
        case 400:
            print("Bad request")
        case 301:
            print("Moved permanently")
        case 401:
            print("Unathorized")
        case 403:
            print("Forbidden")
        case 500:
            print("Internal error")
        case 503:
            print("Service unavailable")
        case 204:
            print("No content")
        case 229:
            print("im a div")
        case 304:
            print("Not modified")
        case 429:
            print("Too many requests")

error()
        
