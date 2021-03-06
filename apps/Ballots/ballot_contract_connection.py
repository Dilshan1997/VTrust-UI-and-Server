contract_address='0x1817C9Fd284399C5D96bba39cc73Ee3eFf03dAf0'

abi="""[
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "ballots_arr",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "ballot_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "owner_email",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ballot_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ballot_description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ballot_owner_name",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "ballot_owner_address",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "open_date",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "closing_date",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "ballot_type",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "proposals_count",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "full_vote_count",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "o_email",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "b_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "b_description",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "b_owner_name",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "b_owner_address",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "start_d",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "end_d",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "b_type",
				"type": "string"
			}
		],
		"name": "createBallot",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "p_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "prop_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "prop_details",
				"type": "string"
			}
		],
		"name": "createProposal",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "bid",
				"type": "uint256"
			}
		],
		"name": "getBallotDetails",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "ballot_id",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "owner_email",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "ballot_name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "ballot_description",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "ballot_owner_name",
						"type": "string"
					},
					{
						"internalType": "address",
						"name": "ballot_owner_address",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "open_date",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "closing_date",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "ballot_type",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "proposals_count",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "full_vote_count",
						"type": "uint256"
					},
					{
						"internalType": "address[]",
						"name": "followers",
						"type": "address[]"
					}
				],
				"internalType": "struct Ballot.BallotDetails",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBallotId",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "getDashboardData",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "getFollowingBallots",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "admin_address",
				"type": "address"
			}
		],
		"name": "getPrivateIds",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "ballot_id",
				"type": "uint256"
			}
		],
		"name": "getPrivateVotersData",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "map_id",
				"type": "string"
			}
		],
		"name": "getProposalDetails",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "proposal_id",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "prop_name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "prop_details",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "vote_count",
						"type": "uint256"
					}
				],
				"internalType": "struct Ballot.proposals",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "p_id",
				"type": "string"
			}
		],
		"name": "getProposalResult",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "b_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "p_id",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "voting_addr",
				"type": "address"
			}
		],
		"name": "privateBallotVoting",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "proposals_arr",
		"outputs": [
			{
				"internalType": "string",
				"name": "proposal_id",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "prop_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "prop_details",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "vote_count",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "admin_address",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "ballot_id",
				"type": "uint256"
			}
		],
		"name": "savePrivateBallotIds",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "ballot_id",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "voter_address",
				"type": "address"
			}
		],
		"name": "savePrivateVotersData",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "bid",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "setFollwers",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "b_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "p_id",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_addr",
				"type": "address"
			}
		],
		"name": "voting",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "b_id",
				"type": "uint256"
			}
		],
		"name": "winningProposal",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
 """
 