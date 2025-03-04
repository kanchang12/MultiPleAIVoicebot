from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Form
HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Start Outbound Call</title>
</head>
<body>
    <h1>Start Outbound Call</h1>
    <form id="callForm">
        <label for="phoneNumber">Enter Phone Number:</label>
        <input type="text" id="phoneNumber" name="phoneNumber" placeholder="+1234567890" required>
        <button type="submit">Start Call</button>
    </form>

    <script>
        document.getElementById('callForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent form submission
            const phoneNumber = document.getElementById('phoneNumber').value;

            // Send the phone number to your Make.com webhook
            fetch('https://hook.make.com/YOUR_MAKE_WEBHOOK_URL', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ phoneNumber: phoneNumber }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                alert('Call initiated!');
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('Failed to initiate call.');
            });
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    app.run(debug=True)
