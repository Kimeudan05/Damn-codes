<?php

require_once 'db.php';

if($_SERVER["REQUEST_METHOD"]=="POST")
{
    $email  = $_POST['email'];
    $password  = $_POST['password'];


    $sql = "SELECT * FROM members WHERE email = '$email'";
    $result = $conn->query($sql);

    if($result->num_rows==1){
        $row= $result->fetch_assoc();
        if(password_verify($password,$row['password'])){
            // Successful login, redirect to member dashboard
            header("Location:member_dashboard.php");
        }else{
            echo("Invalid password");
        }
    }else{
        echo("Member not found");
    }
}
$conn->close();
?>