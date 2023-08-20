<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Church Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to our Church</h1>
    </header>
    <nav>
        <ul>
            <li><a href="index.php">Home</a></li>
            <li><a href="signup.php">Sign Up</a></li>
            <li><a href="login.php">Login</a></li>
        </ul>
    </nav>
    <main>
        <section>
            <h2>Latest Notices</h2>
            <!-- Display notices here -->
        </section>
        <footer>
            <p>&copy;<?php echo date('Y')?>Mithetheni Aic</p>
        </footer>
    </main>
</body>
</html>