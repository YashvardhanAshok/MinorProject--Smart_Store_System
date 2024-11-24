<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'];
    $password = $_POST['password'];

    $serverid = "localhost";
    $PhPid = "BROWSER1";
    $password = "~]TmYCf[AEEV";
    $database = "MAIN_DATA_BASE_FOR_MOVIE_CLUB";
    
    
    
    // Create a connection
    $db = new mysqli($serverid, $PhPid, $password, $database);


    if ($db->connect_error) {
        die("Connection failed: " . $db->connect_error);
    }

    $stmt = $db->prepare("SELECT id FROM user_data WHERE email = ? AND password = ?");

    if (!$stmt) {
        die("Prepare failed: " . $db->error);
    }

    $stmt->bind_param("ss", $email, $password);

    if (!$stmt->execute()) {
        die("Execute failed: " . $stmt->error);
    }

    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $user_id = $row['id'];
        echo "Data_successfully" . $user_id;
    } else {
        echo "Try again";
    }

    $stmt->close();
    $db->close();
} else {
    echo "Invalid request";
}
?>
