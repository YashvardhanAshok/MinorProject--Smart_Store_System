<?php
// Connect to the MySQL database
$serverid = "localhost";
$PhPid = "BROWSER1";
$password = "~]TmYCf[AEEV";
$database = "MAIN_DATA_BASE_FOR_MOVIE_CLUB";



// Create a connection
$conn = new mysqli($serverid, $PhPid, $password, $database);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the HTTP POST request was made
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fName = isset($_POST["fName"]) ? $_POST["fName"] : '';
    $lName = isset($_POST["lName"]) ? $_POST["lName"] : '';
    $email = isset($_POST["email"]) ? $_POST["email"] : '';
    $password = isset($_POST["password"]) ? $_POST["password"] : '';

    // Check if the email already exists
    $checkQuery = "SELECT COUNT(*) AS count FROM user_data WHERE email = ?";
    if ($stmt = $conn->prepare($checkQuery)) {
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $result = $stmt->get_result();
        $row = $result->fetch_assoc();
        $emailCount = $row['count'];
        $stmt->close();

        if ($emailCount > 0) {
            echo "Email is already in use.";
        } else {
            // Email is not in use, so insert the data
            $insertQuery = "INSERT INTO user_data (fName, lName, email, password) VALUES (?, ?, ?, ?)";
            if ($stmt = $conn->prepare($insertQuery)) {
                $stmt->bind_param("ssss", $fName, $lName, $email, $password);
                if ($stmt->execute()) {
                    echo "Data inserted successfully!";
                } else {
                    echo "Error: " . $stmt->error;
                }
                $stmt->close();
            } else {
                echo "Error preparing the SQL statement: " . $conn->error;
            }
        }
    } else {
        echo "Error preparing the SQL statement: " . $conn->error;
    }
}

// Close the database connection
$conn->close();
?>
