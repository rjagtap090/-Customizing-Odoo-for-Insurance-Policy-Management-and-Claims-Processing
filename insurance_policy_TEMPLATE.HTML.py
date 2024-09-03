<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
</head>
<body>
    <h1>Insurance Policy: {{ policy.name }}</h1>
    <p>Type: {{ policy.policy_type }}</p>
    <p>Customer: {{ policy.customer_id.name }}</p>
    <p>Start Date: {{ policy.start_date }}</p>
    <p>End Date: {{ policy.end_date }}</p>
    <p>Premium: ${{ policy.premium_amount }}</p>
</body>
<script src="/static/js/script.js"></script>
</html>


