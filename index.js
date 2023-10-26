const Discord = require('discord.js');
var axios = require('axios');
var fetch = require('node-fetch');
var clientid = 'xxxx';
//const fetch = require('node-fetch');
//const bent = require('bent')
//const getJSON = bent('json')
const client = new Discord.Client();

client.once('ready', () => {
	console.log('Ready!');
});

client.login('x.x.x');
client.on('message', message => {
    console.log(message.content);
    
    
    if (message.content === '!ping') {
        // send back "Pong." to the channel the message was sent in
        message.channel.send('Pong.'); 
    }
   // const querystring = require('querystring');
   
    
    var prefix = "!";
    if (!message.content.startsWith(prefix) || message.author.bot) return;
    const args = message.content.slice(prefix.length).split(' ');
    const username = args.shift().toLowerCase();
    const querystring = require('querystring');

    if (message.content === 'live') {
      CheckOnlineStatus(prefix, args, message, querystring) 
    }

    if (message.content === '!who') {
      Check(message);
  
    }
});
async function CheckOnlineStatus(prefix, username, message, querystring) {
  
  if (prefix === 'live') {
    if (!username.length) {
      return message.channel.send('You need to supply a search term!');
    }
    const query = querystring.stringify({ term: args.join(' ') });
    const picked =  fetch(`https://api.twitch.tv/helix/streams?user_id=${query}`,[Headers={clientid}]).then(response => response.json());
  
    if (!picked.length) { 
      return message.channel.send(`No results found for **${username.join(' ')}**.`);
    }
    message.channel.send(picked);}
  }


  async function Check(message) {
    //let obj = await getJSON('https://api.twitch.tv/helix/streams?user_login=xxx')
      //const live = await fetch('https://api.twitch.tv/helix/streams?user_login=xx', {headers: {'Client_ID': 'xx'}}).then(response => response.json());
      
      const picked = fetch(`https://api.twitch.tv/helix/streams?user_id=xx`,[Headers={clientid}]).then(response => response.json());
      // status code
      //stream.status // 200 
      //stream.statusCode // 200
      // optionally decode
      //const obj = await stream.json();
      //if (!live.length) { 
      //  return message.channel.send(`No results found for **${args.join(' ')}**.`);
      //}
      return message.channel.send(picked);  
    }
    // Twitch functions}




  //const $ = require('JSON');
  //$.getJSON('https://api.twitch.tv/helix/streams/xxx?callback=?', function(data) {
  //console.log(data);
 // message.channel.send(data);

   // var whoPicked = message.content.split(" ");
    //if(whoPicked[0] === '!live'){
      //var picked = whoPicked[1]; 
    //  if (!whoPicked[1].length == 'NULL') {
      //  return message.channel.send('You need to supply a username!');
     // }
      
      //picked = querystring.stringify({ term: picked.join(' ') });
      //const live = await fetch(`https://api.twitch.tv/kraken/streams/${picked}`).then(response => response.json());
      //return message.channel.send(live);
      //message.channel.send("testing2");
    
   
  //}
  

 