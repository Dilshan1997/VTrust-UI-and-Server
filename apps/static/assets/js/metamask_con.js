console.log("connected")
if (typeof window.ethereum !== 'undefined') {
  console.log('MetaMask is installed!');
}
else {
  console.log('You should install metamask!');

}
const ethereumButton = document.querySelector('.enableEthereumButton');
const showAccount = document.querySelector('.showAccount');

ethereumButton.addEventListener('click', () => {
  console.log('account')
  getAccount();
});

async function getAccount() {
  const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
  const account = accounts[0];
  showAccount.value = account.toUpperCase();
}
