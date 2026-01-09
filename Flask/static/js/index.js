 const form = document.getElementById('calculatorForm');
            const resultContainer = document.getElementById('resultContainer');
            const resultValue = document.getElementById('resultValue');
            const errorMessage = document.getElementById('errorMessage');

            form.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const num1 = parseFloat(document.getElementById('num1').value);
                const num2 = parseFloat(document.getElementById('num2').value);
                const operation = document.querySelector('input[name="operation"]:checked').value;

                try {
                    const response = await fetch('/api/calculator', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            num1: num1,
                            num2: num2,
                            operation: operation
                        })
                    });

                    const data = await response.json();

                    if (data.error) {
                        errorMessage.textContent = data.error;
                        errorMessage.classList.add('show');
                        resultContainer.classList.remove('show');
                    } else {
                        resultValue.textContent = data.result;
                        resultContainer.classList.add('show');
                        errorMessage.classList.remove('show');
                    }
                } catch (error) {
                    errorMessage.textContent = 'An error occurred. Please try again.';
                    errorMessage.classList.add('show');
                    resultContainer.classList.remove('show');
                }
            });