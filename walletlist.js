const fs = require('fs');

// Read data from file.txt
fs.readFile('walletlist.txt', 'utf8', (err, data) => {
  if (err) throw err;

  // Convert data to array and remove duplicates
  
  const dataLowerCase = data.toLowerCase();
  
  const dataArray = dataLowerCase.trim().split('\n');
  const uniqueDataArray = [...new Set(dataArray)];

  // Write filtered data to list.txt
  fs.writeFile('walletlist_result.txt', uniqueDataArray.join('\n'), err => {
    if (err) throw err;
    console.log('Data written to list.txt');
  });
});