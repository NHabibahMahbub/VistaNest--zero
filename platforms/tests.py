<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VistaNest - Property Details</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">

    <style>
        .bordered-image {
            max-width: 100%;
            height: auto;
            border: 3px solid black;
            border-radius: 15px;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
        }
    </style>
</head>

<body>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
        <a class="navbar-brand" href="#">VistaNest - Real Estate Platform</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
    </nav>

    <div class="container mt-5 pt-4">
        <!-- Property Details Section -->
        <div class="row mt-4">
            <div class="col-md-6">
                <h1 style="font-family: 'Montserrat';">{{ platform.title }}</h1>
                <p><strong>Owner's Contact Number:</strong> {{ platform.owner_contact_number }}</p>
                <p><strong>Property Type:</strong> {{ platform.property_type }}</p>
                <p><strong>Property Description:</strong> {{ platform.description }}</p>
                <p><strong>Price: BDT</strong> {{ platform.price }}</p>
                <p><strong>Size:</strong> {{ platform.size_sqft }} sqft</p>
                <p><strong>Year Built:</strong> {{ platform.year_built }}</p>
                <p><strong>Location:</strong> {{ platform.location }}</p>
                <p><strong>City:</strong> {{ platform.city }}</p>
                <p><strong>Country:</strong> {{ platform.country }}</p>
                <p><strong>Listed Date:</strong> {{ platform.listed_date }}</p>
            </div>

            <div class="col-md-6">
                <img src="{{ platform.image.url }}" alt="Property Image" class="bordered-image">
            </div>
        </div>

        <!-- Bids Details Section -->
        <h2 class="mt-5" style="font-family: 'Montserrat';"><b>Bids Details</b></h2>
        <div id="bids" class="mb-4">
            {% for bid in bids %}
                <p>User: {{ bid.user.username }}, Amount: BDT {{ bid.amount }}</p>
            {% empty %}
                <p>No bids available for this property.</p>
            {% endfor %}
        </div>

        <!-- Navigation Links -->
        <a href="{% url 'home' %}" class="btn btn-primary">Back to Home</a>
        <a href="{% url 'search' %}" class="btn btn-secondary ml-2">Back to Search</a>

        <!-- Add to Favorites Link -->
        <br><br>
        {% if user.is_authenticated %}
            {% if platform in user.favorite_set.all %}
                <a href="{% url 'remove_from_favorites' platform.id %}" class="btn btn-outline-danger mt-2">Remove from Favorites</a>
            {% else %}
                <a href="{% url 'add_to_favorites' platform.id %}" class="btn btn-outline-success mt-2">Add to Favorites</a>
            {% endif %}
        {% else %}
            <p>Please <a href="{% url 'login' %}">login</a> to add to favorites.</p>
        {% endif %}
    </div>

    <!-- Bootstrap and jQuery Scripts -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa8z7peE2fh7k7q2MZXKfXj7N" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy9V7J5aVnDaDXFnKkvXHQjhlCZsmf5L8u6w6R6" crossorigin="anonymous"></script>
</body>
</html>
