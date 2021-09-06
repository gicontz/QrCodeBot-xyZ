import os;

ScholarsDict = {
    # 'DiscordID' : ['DiscordName', 'RoninWalletAddress', 'RoninPrivateKey']

    # The RoninWalletAddress should start with 0x instead of ronin:
    # The RoninPrivateKey should be parsed without the 0x
    
    # The following are placeholders...
    os.environ.get('ALPHA_ISKO') : ['Josh | Axie Pixel - Alpha', '0x5cf87ecafb97ef82ff26563879ef364d11a5bb6c', os.environ.get('ALPHA_SK')],
    '698092015237201990' : ['ghilo17 | Axie Pixel - Alpha', '0x3e108a8776613656ffafce31da3dc88c3538f016', os.environ.get('BETA_SK')],
    os.environ.get('GAMMA_ISKO') : ['Kyle | Axie Pixel - Gamma', '0x23a7149ff395c0649ce739b8dc62b98a78e09c05', os.environ.get('GAMMA_SK')],
    os.environ.get('DELTA_ISKO') : ['Grace | Axie Pixel - Delta', '0xfa54eda8f2213c579964983d3fdbbe6bb7ee2fd3', os.environ.get('DELTA_SK')],
    os.environ.get('EPSILON_ISKO') : ['Luis | Axie Pixel Gamma', '0xb34fd9e5b6f531282091519b90a038b01d9c9f98', os.environ.get('EPSILON_SK')],
    os.environ.get('ZETA_ISKO') : ['Tristan | Axie Pixel - Zeta', '0xdd4ce073df32a00f3a0244ad27e50ba6e1e6a224', os.environ.get('ZETA_SK')],
    os.environ.get('ETA_ISKO') : ['Jamil | Axie Pixel - Etha', '0x973132d42ec668720185c4eb1eef21c75e433a06', os.environ.get('ETA_SK')],
    os.environ.get('THETA_ISKO') : ['Carlo | Axie Pixel - Etha', '0xd47ca611a00a918ab5d2118910e7680fa6fd393a', os.environ.get('TETHA_SK')],
}
# Put Your Discord Bot Token Here
DiscordBotToken = os.environ.get('BOT_TOKEN')
