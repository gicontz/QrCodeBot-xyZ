import os;

ScholarsDict = {
    # 'DiscordID' : ['DiscordName', 'RoninWalletAddress', 'RoninPrivateKey']

    # The RoninWalletAddress should start with 0x instead of ronin:
    # The RoninPrivateKey should be parsed without the 0x
    
    # The following are placeholders...
    '698092015237201990' : ['ghilo17 | Axie Pixel - Alpha', '0x3e108a8776613656ffafce31da3dc88c3538f016','2941c3d3756ff6a881472d9fcf4f1e0afd17cb0516bdc037a8f65c9be253b7b1'],
    '413325738477879296' : ['Josh | Axie Pixel - Alpha', '0x5cf87ecafb97ef82ff26563879ef364d11a5bb6c','2cb8d0b3fa4e83a95b5669855898b34bece877bf309869ac2d5efe01c7581982'],
    '740475450400440341' : ['Kyle | Axie Pixel - Gamma', '0x23a7149ff395c0649ce739b8dc62b98a78e09c05','a5532b382378ebb5da6331a6a17b19930dbee699807edfab512e630f6c82f0a5'],
    '867909482573860875' : ['Grace | Axie Pixel - Delta', '0xfa54eda8f2213c579964983d3fdbbe6bb7ee2fd3','e8e95578cda29f730632ead52142db5f64ca89078bbcfb20dd96ba56400de63c'],
    '880955785025310780' : ['Tristan | Axie Pixel - Zeta', '0xdd4ce073df32a00f3a0244ad27e50ba6e1e6a224','eb620fe457f65a6a2bfa2fc176b95cb8c4f0398eb37001084ecc4e66bf58689d'],
    '840098568627159042' : ['Jamil | Axie Pixel - Etha', '0x973132d42ec668720185c4eb1eef21c75e433a06','7e4bba4be90785f50ebf9ab030988e20569080347e29d666fed4ff98f0c6d8be'],
    '855547397487853598' : ['Carlo | Axie Pixel - Etha', '0xd47ca611a00a918ab5d2118910e7680fa6fd393a','8d740814494eba228c37a341db889d039a0e446786501438125e28483df8c587'],
    '856362725399855124': ['Luis | Axie Pixel Gamma', '0xb34fd9e5b6f531282091519b90a038b01d9c9f98', '4218d6b2add78a8dbead2308442b3cb53f61ceb5052f64e8862f428018e01ce5']
}
# Put Your Discord Bot Token Here
DiscordBotToken = os.environ.get('BOT_TOKEN')
