const express = require('express')
const app = express()
const port = 3000
const rpio = require('rpio');

let variable = false
app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static('./resources'));

var options = {
    gpiomem: true,          /* Use /dev/gpiomem */
    mapping: 'physical',    /* Use the P1-P40 numbering scheme */
    mock: undefined,        /* Emulate specific hardware in mock mode */
    close_on_exit: true,    /* On node process exit automatically close rpio */
}

rpio.init([options])
rpio.open(11, rpio.OUTPUT, rpio.LOW);

app.get('/', (req, res) =>
    res.render('index',
        {
            variable: variable
        }))

app.post('/change', (req, res) => {
    variable = !req.body.variable
    if (variable){
        rpio.open(11, rpio.OUTPUT, rpio.HIGH);
    }
    else
    {
        rpio.open(11, rpio.OUTPUT, rpio.LOW);
    }
    res.send({ variable })
})
app.listen(port, () => console.log(`Example app listening on port ${port}!`))