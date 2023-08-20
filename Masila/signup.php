<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <header>
        <h1>Sign Up</h1>
    </header>
    <nav>
        <ul>
            <li><a href="index.php">Home</a></li>
        </ul>
    </nav>
    <main>
        <section>
            <h2>Member Sign Up</h2>
            <form action="process_signup.php" method="post">
                <label for="fname">First Name:</label>
                <input type="text" name="fname" required><br>
                
                <label for="lname">Last Name:</label>
                <input type="text" name="lname" required><br>
                
                <label for="email">Email:</label>
                <input type="email" name="email" required><br>
                
                <label for="phone">Phone:</label>
                <input type="tel" name="phone" required><br>
                
                <label for="gender">Gender:</label>
                <select name="gender" required>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                </select><br>
                
                <label for="password">Password:</label>
                <input type="password" name="password" id="password" required>
                <input type="checkbox" id="showPassword"> Show Password<br>
                
                <label for="confirm_password">Confirm Password:</label>
                <input type="password" name="confirm_password" id="confirmPassword" required><br>
                
                <label for="category">Category:</label>
                <select name="category" required>
                    <option value="praise">Praise</option>
                    <option value="sunday_school">Sunday School</option>
                    <option value="kama">KAMA</option>
                    <option value="mothers_union">Mothers Union</option>
                </select><br>
                
                <input type="submit" value="Sign Up">
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; <?php echo date("Y"); ?> Church Name</p>
    </footer>
    <script>
        const showPasswordCheckbox = document.getElementById('showPassword');
        const passwordInput = document.getElementById('password');
        const confirmPasswordInput = document.getElementById('confirmPassword');

        showPasswordCheckbox.addEventListener('change', function () {
            if (showPasswordCheckbox.checked) {
                passwordInput.type = 'text';
                confirmPasswordInput.type = 'text';
            } else {
                passwordInput.type = 'password';
                confirmPasswordInput.type = 'password';
            }
        });
    </script>
</body>
</html>
