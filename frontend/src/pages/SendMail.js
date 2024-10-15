import React, { useState } from 'react';
import { TextField, Button, Box, Typography } from '@mui/material';

const EmailForm = () => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [statusMessage, setStatusMessage] = useState('');

  const sendEmail = async (e) => {
    e.preventDefault();
    try {
      // Send POST request to the server
      const report = JSON.parse(localStorage.getItem('report'));
      const data = {
        email,
        username,
        ...report
      }
      const response = await fetch('http://127.0.0.1:8000/api/send-mail/', {
        method : "POST",
        body : JSON.stringify(data),
        headers : {
            "content-type" : "application/json"
        }
      });

      if (response.status === 200) {
        setStatusMessage('Email successfully sent!');
      }
      alert("email sended")
    } catch (error) {
      console.error('Error sending email', error);
      setStatusMessage('Failed to send email. Please try again.');
      alert("something vent wrong")
    }
  };

  return (
    <Box
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
      height="100vh"
    >
      <Box
        component="form"
        onSubmit={sendEmail}
        sx={{
          display: 'flex',
          flexDirection: 'column',
          gap: 2,
          width: '300px',
        }}
      >
        <Typography variant="h4" textAlign="center" gutterBottom>
          Send Email
        </Typography>
        <TextField
          label="Email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          fullWidth
          required
        />
        <TextField
          label="Username"
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          fullWidth
          required
        />
        <Button variant="contained" color="primary" type="submit" fullWidth onClick={sendEmail}>
          Send Mail
        </Button>
        <Typography variant="body2" color="textSecondary" textAlign="center">
          {statusMessage}
        </Typography>
      </Box>
    </Box>
  );
};

export default EmailForm;
