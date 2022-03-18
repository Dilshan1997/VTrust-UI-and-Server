const tokenAddress = '0x3710A28F56e8460235f6ed7e027083adC8155e18';
const tokenSymbol = 'VT';
const tokenDecimals = 1;
const tokenImage = '';
console.log('VT token')

$("#sign_up").click(async function(){
  try {
    // wasAdded is a boolean. Like any RPC method, an error may be thrown.
    const wasAdded = await ethereum.request({
      method: 'wallet_watchAsset',
      params: {
        type: 'ERC20', // Initially only supports ERC20, but eventually more!
        options: {
          address: tokenAddress, // The address that the token is at.
          symbol: tokenSymbol, // A ticker symbol or shorthand, up to 5 chars.
          decimals: tokenDecimals, // The number of decimals in the token
          // image: tokenImage, // A string url of the token logo
        },
      },
    });
  
    if (wasAdded) {
      console.log('Thanks for your interest!');
    } else {
      console.log('Your loss!');
    }
  } catch (error) {
    console.log(error);
  }
})
