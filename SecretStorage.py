import os;

ScholarsDict = {
    # 'DiscordID' : ['DiscordName', 'RoninWalletAddress', 'RoninPrivateKey']

    # The RoninWalletAddress should start with 0x instead of ronin:
    # The RoninPrivateKey should be parsed without the 0x
    
    # The following are placeholders...
    '698092015237201990' : ['ghilo17 | Axie Pixel - Alpha', '0x3e108a8776613656ffafce31da3dc88c3538f016', '2941c3d3756ff6a881472d9fcf4f1e0afd17cb0516bdc037a8f65c9be253b7b1'],
}
# Put Your Discord Bot Token Here
DiscordBotToken = os.environ.get('BOT_TOKEN')
