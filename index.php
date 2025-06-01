<!DOCTYPE html>
<html>
<head>
    <title>Basketball Advisor</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .container { max-width: 500px; margin: 0 auto; }
        .result { margin-top: 20px; padding: 15px; background: #f5f5f5; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Basketball Weather Advisor</h1>
        <form method="post">
            <label>Outlook:</label><br>
            <select name="outlook" required>
                <option value="Sunny">Sunny</option>
                <option value="Overcast">Overcast</option>
                <option value="Rainy">Rainy</option>
            </select><br><br>
            
            <label>Temperature:</label><br>
            <select name="temp" required>
                <option value="Hot">Hot</option>
                <option value="Mild">Mild</option>
                <option value="Cool">Cool</option>
            </select><br><br>
            
            <label>Humidity:</label><br>
            <select name="humidity" required>
                <option value="High">High</option>
                <option value="Normal">Normal</option>
            </select><br><br>
            
            <label>Windy?</label><br>
            <select name="windy" required>
                <option value="False">No</option>
                <option value="True">Yes</option>
            </select><br><br>
            
            <input type="submit" value="Check Conditions">
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $outlook = escapeshellarg($_POST['outlook']);
            $temp = escapeshellarg($_POST['temp']);
            $humidity = escapeshellarg($_POST['humidity']);
            $windy = escapeshellarg($_POST['windy']);
            
            $command = "C:\\Python313\\python.exe predict.py $outlook $temp $humidity $windy 2>&1";
            $result = shell_exec($command);
            
            echo '<div class="result">';
            echo '<h3>Result:</h3>';
            echo '<p>' . htmlspecialchars($result) . '</p>';
            echo '</div>';
        }
        ?>
    </div>
</body>
</html>