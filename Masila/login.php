<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Login</h1>
    </header>

    <nav>
        <ul>
            <li><a href="index.php">Home</a></li>
        </ul>
    </nav>
    <main>
        <section>
            <h2>Member Login</h2>
            <form action="process_login.php" method="post">
                 <!-- Login form fields -->
                 <label for="email">Email/Phone:</label>
                 <input type="text"name="email" required><br>

                 <label for="password">Password:</label>
                 <input type="password" name="password" id="password">
                 <input type="checkbox"id="showPassword">Show Password <br>

                 <input type="submit" value="Login">
            </form>
        </section>
    </main>

    <footer>
        <p>&copy;<?php echo date("Y");?>     Aic Mithetheni</p>
    </footer>

    <script>
        const showPass  =document.getElementById('showPassword')
        const passInput =document.getElementById('password')

        showPass.addEventListener('change',function(){
            if(showPass.checked){
                passInput.type = 'text';
            }else{
                passInput.type = 'password'
            }
        })
    </script>
</body>
</html>