#!/usr/bin/node 

const fs =  require('fs')

const file_path = process.argv[2]

const string = process.argv[3]

fs.writeFile(file_path, string, 'utf8', (err) => {
	if (err){
		console.error(err);
		return;
	}
});

