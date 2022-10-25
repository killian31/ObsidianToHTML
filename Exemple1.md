Status : en cours
Topics : #Blockchain 
Links : [[Project BBD]] [[System Architecture]]

-------------

# Summary
| Consensus algorithm | Platforms | Description | Requires cryptocurrency | Benefits | Drawbacks |
| :--- | :--- | ---: | ---: | ---: | ---: |
| [[#Proof of Work]] (PoW) | Bitcoin | A node (miner) use energy to solve a problem and add a block. User receive crypto for it. | Yes | Most secure consensus algorithm | Needs a lot of computational power. Consume a lot of energy. Risk of centralisation |
| [[#Proof of Stake]] (PoS) | Ethereum, Cardano | | | Better decentralisation.| The richest are likely to become richer.|

> "Due to the high network delay in the peer-to-peer network, the order of transactions observed by each node may not be exactly the same. Therefore, the blockchain system needs to design a mechanism to agree on the order of transactions that occur within a similar period of time. This algorithm for agreeing on the order of transactions within a time window is called a "consensus mechanism." 
> 
>  -- [Qianwen Wang _et al_ 2020 _J. Phys.: Conf. Ser._ **1437** 012007](https://iopscience.iop.org/article/10.1088/1742-6596/1437/1/012007)


# Proof of Work

- Some people (nodes) are competing to solve a problem mathematical problem
- The first one to solve it have the right to add the bloc to the blockchain and earn crypto for it (that's the mining process)
- The more energy spent, the greater the reward 

# Proof of Stake 

- Needs less energy than [[#Proof of Work]]
- Validators need to have at stake some crypto that they can't use 
- Validators are chosen randomly, gathered randomly in groups 
- Each time a bloc is added, a certain amount of groups need to validate it.
- Reward for adding or attesting a bloc is valid
- A validator cheating will lose part of his stake 

# Delegated Proof of Stake (DPoS)

- Performance improve but less decentralised
- Voters vote to elect delegates who will validate blocks on voters' behalf

# Proof of Authority (PoA)

- Blocks approved by validators
- Fully automated
- To become a validator, a network user must earn the right by accumulating a sufficiently positive reputation
- Validators are motivated to uphold the transaction process, as failing to do so would result in a negative reputation being attached to their identities

To be established as validator, the following conditions must be met:
1. Identity is verified on the blockchain
2. It has to be difficult to earn this title in order for the community to value this position (for example a validator has to obtain a public notary license)
3. Checks and procedures for establishing authority must be completely uniform

Scalable but high risk of centralisation (=> not likely to see it on a public blockchain)  
