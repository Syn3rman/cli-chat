var io = require('socket.io-client');
var readlineSync = require('readline-sync');

socket = io.connect('http://localhost:3000');

socket.on('connect', async ()=>{
    console.log('Sending message');
    let t=0;
    while(t<5){
        var msg = readlineSync.question('Message: ');
        socket.emit('message', msg)
    t+=1
    }
});
// socket.emit()