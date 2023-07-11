# Deploying a smart contract using Brownie

Brownie is a framework commonly used for developing and testing smart contracts for the Ethereum Virtual Machine. It supports both Solidity and Vyper as smart contract languages, but we’ll use Solidity in this project.

Brownie is relatively comfortable for people who prefer Python over Truffle or Hardhat, which are JavaScript-based frameworks.

Before we get started with the project, we must have the following things:

An Ethereum wallet such as MetaMask.
Some Ether on the Goerli testnet (which can be requested on their faucet).
A Web3 backend and IaaS provider such as an Infura account.
In the first part of the project, we’ll create a smart contract and deploy it on a local blockchain. We will write Python scripts that will interact with it. Later on, we’ll deploy the same contract on the Goerli test network where other people can access our contract and try it out.
