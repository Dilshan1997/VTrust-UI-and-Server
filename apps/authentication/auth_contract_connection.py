contract_address='0x914d29eCe58617B7925d516654b8E93d445d82E5'

abi="""[
	{
		"constant": false,
		"inputs": [
			{
				"name": "_newname",
				"type": "string"
			},
			{
				"name": "_newemail",
				"type": "string"
			},
			{
				"name": "_oldpassword",
				"type": "string"
			},
			{
				"name": "_newpassword",
				"type": "string"
			}
		],
		"name": "changeUserData",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			},
			{
				"name": "_name",
				"type": "string"
			},
			{
				"name": "_password",
				"type": "string"
			}
		],
		"name": "loginUser",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "logoutUser",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			},
			{
				"name": "_name",
				"type": "string"
			},
			{
				"name": "_email",
				"type": "string"
			},
			{
				"name": "_password",
				"type": "string"
			}
		],
		"name": "registerUser",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_name",
				"type": "string"
			},
			{
				"indexed": false,
				"name": "_password",
				"type": "string"
			}
		],
		"name": "LogInUser",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"name": "_id",
				"type": "uint256"
			},
			{
				"indexed": false,
				"name": "_name",
				"type": "string"
			},
			{
				"indexed": false,
				"name": "_email",
				"type": "string"
			},
			{
				"indexed": false,
				"name": "_password",
				"type": "string"
			}
		],
		"name": "RegNewUser",
		"type": "event"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "checkIsUserLogged",
		"outputs": [
			{
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "get_address",
		"outputs": [
			{
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getUserBalance",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getUserData",
		"outputs": [
			{
				"name": "id",
				"type": "uint256"
			},
			{
				"name": "email",
				"type": "string"
			},
			{
				"name": "",
				"type": "address"
			},
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"name": "User_arr",
		"outputs": [
			{
				"name": "id",
				"type": "uint256"
			},
			{
				"name": "UserAddress",
				"type": "address"
			},
			{
				"name": "name",
				"type": "string"
			},
			{
				"name": "email",
				"type": "string"
			},
			{
				"name": "password",
				"type": "string"
			},
			{
				"name": "isUserLoggedIn",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]
 """