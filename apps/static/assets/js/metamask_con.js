console.log("connected")
if (typeof window.ethereum !== 'undefined') {
  console.log('MetaMask is installed!');
}
else {
  console.log('You should install metamask!');

}
const ethereumButton = document.querySelector('.enableEthereumButton');
const showAccount = document.querySelector('.showAccount');

ethereumButton.addEventListener('click',async () => {
  console.log('account')
  ac=await getAccount();
  console.log(ac)
  showAccount.value=ac
});

async function getAccount() {
  const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
  const account = accounts[0];
  console.log(account)
  return account;
  
}
