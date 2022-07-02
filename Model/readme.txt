Run in the following order:

1. Scrape_1 
2. Scrape_2
- Step 1&2 are estimated to take a few hours together - 
3. Data_Processing - Uses INJ_Mapping_Finalized.csv as one of the input. All of the injuries were manually labeled.
4. LR,RF,NB,XG - Outputs several .joblib sklearn models to be used for the voting classifier in file #5.
5. voting_classifier.


No APIs/Keys are required. All of the sources are publicly available.
TransferMrkt data policy - https://www.transfermarkt.co.uk/intern/datenpflegeGuide
Fbref data policy - https://www.sports-reference.com/data_use.html
