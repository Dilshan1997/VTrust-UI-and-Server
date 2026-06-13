# 🗳️ VTrust: A Decentralized Blockchain-Empowered Voting Ecosystem

VTrust is a secure, decentralized, and mobile-responsive web-based voting ecosystem engineered to mitigate the systemic vulnerabilities of trust, architectural centralization, and administrative manipulation inherent in traditional voting systems.

By implementing Web 3.0 technologies, VTrust eliminates single points of failure, ensuring that all cast ballots are cryptographically immutable, auditable, and completely free from third-party intervention.

## ✨ Platform Overview

The platform utilizes a hybrid execution architecture:

- **On-chain (Ethereum + Solidity):**
  - Ballot execution
  - Credential validation
  - Immutable storage

- **Off-chain (Django + MySQL):**
  - Session management
  - Telemetry
  - Cached data

## 🛠️ System Architecture



## 🔬 Feature Implementation

### 🔐 1. Hybrid Parallel 2FA Authentication

- Combines:
  - Local database verification
  - Blockchain smart contract validation
- Uses MetaMask wallet identity
- Dual hashing:
  - Django hashing
  - Solidity `keccak256`

### 📊 2. Dynamic Ballot Engine

- Dynamic UI generation without page reload
- Converts timestamps to Unix Epoch
- Deterministic ID structure:

### 🌐 3. Trustless Public Polling

- One vote per wallet (anti-Sybil protection)
- Real-time analytics using AJAX + Chart.js
- Auto result finalization after deadline

### 🔒 4. Private Ballot System

- Wallet whitelist stored on-chain
- Email-based access control
- Smart contract validation via `msg.sender`

### 🪙 5. VT Token (ERC-20)

- Built on ERC-20 standard
- Used for:
- Ballot creation fees
- Monetization model
- Automatic token distribution during registration

## 📈 Feature Validation Matrix

| Feature | Status |
|--------|--------|
| Web3 Authentication | ✅ Validated |
| Dynamic Ballots | ✅ Validated |
| Public Polling | ✅ Validated |
| Private Voting | ✅ Validated |
| Analytics Dashboard | ✅ Validated |
| ERC-20 Token | 💎 Core Stable |

## 🖼️ UI & System Diagrams

### Use Case Diagram
![Use Case Diagram](assets/docs/use_case_diagram.png)

### Activity Diagram
![Activity Diagram](assets/docs/activity_diagram.png)

### Dashboard UI
![Dashboard UI](assets/screenshots/dashboard.png)

### Ballot Wizard UI
![Ballot Wizard](assets/screenshots/ballot_wizard.png)

## 🎛️ Technology Stack

### ⛓️ Blockchain
- Solidity (v0.8.x)
- OpenZeppelin Contracts
- Ganache
- Remix IDE

### ⚙️ Backend
- Python 3.8+
- Django Framework
- MySQL Server
- MailHog

### 🎨 Frontend
- Bootstrap 4/5
- JavaScript (ES6)
- jQuery
- Parsley.js
- Chart.js

## 🚀 Installation Guide

### ✅ Prerequisites

- Python 3.8+
- Node.js (LTS)
- MySQL Server
- MetaMask Extension

### 🔹 Phase 1: Blockchain Setup

1. Start Ganache
2. Connect MetaMask to Ganache
3. Import accounts
4. Compile contracts in Remix
5. Deploy contracts
6. Save:
 - Contract addresses
 - ABI files

### 🔹 Phase 2: Backend Setup

```bash
git clone https://github.com/placeholder-username/vtrust-voting-system.git
cd vtrust-voting-system

python -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```
## 🔹 Environment Configuration (.env)

Create a `.env` file in your project root:

```env
DEBUG=True
SECRET_KEY=your_secret_key_here

DB_NAME=vtrust_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306

BLOCKCHAIN_NODE_URL=http://127.0.0.1:7545

AUTH_CONTRACT_ADDRESS=0xYourAuthContractAddress
BALLOT_CONTRACT_ADDRESS=0xYourBallotContractAddress
```

## 🔹 Backend Setup Commands

```bash
git clone https://github.com/placeholder-username/vtrust-voting-system.git
cd vtrust-voting-system

python -m venv venv
source venv/bin/activate   # Windows: .\venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```

## 🔹 Database & Server Commands

```bash
python manage.py makemigrations
python manage.py migrate

# Start MailHog (depends on installation)
mailhog

# Run Django server
python manage.py runserver
```

## 🔹 Access URL
http://127.0.0.1:8000
