<?php

require_once 'db.php';

if($_SERVER["REQUEST_METHOD"]=="POST"){
    // GET FORM DATA
    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $gender = $_POST['gender'];
    $password = password_hash($_POST['password'],PASSWORD_DEFAULT);
    $category = $_POST['category'];

      // Insert member data into database
    $sql = "INSERT INTO members(fname,lname,email,phone,gender,password,category) VALUES ('$fname','$lname','$email','$phone','$gender','$password','$category')";
    
    if($conn->query($sql)== TRUE){
        // Redirect to success page or login
        header("Location: login.php");
    }else{
        echo("Error: " .$sql."<br>" .$conn->error);
    }
   $conn->close();
}
?>