const exp = require('express');
const { exec } = require('child_process');
const app = exp();

app.use(exp.json());

app.get('/calculate/:method/:value', (req, res) => {
    const method = req.params.method;
    const value = req.params.value;

    const pythonScript = `python calculator.py ${method} ${value}`;

    exec(pythonScript, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing the Python script: ${error}`);
            return;
        }

        console.log(`Python script output: ${stdout}`);
        if (stderr) {
            console.error(`Python script error: ${stderr}`);
        }

        res.send({ message: `Result for ${method}(${value})`, payload: stdout });
    });
});

app.listen(4000, () => {
    console.log("server running on port 4000...");
});
