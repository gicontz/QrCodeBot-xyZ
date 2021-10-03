import os;

ScholarsDict = {
    # 'DiscordID' : ['DiscordName', 'RoninWalletAddress', 'RoninPrivateKey']

    # The RoninWalletAddress should start with 0x instead of ronin:
    # The RoninPrivateKey should be parsed without the 0x
    
    # The following are placeholders...
    os.environ.get('ALPHA_ISKO') : ['Josh | Axie Pixel - Alpha', os.environ.get('ALPHA_RONIN'), os.environ.get('ALPHA_SK')],
    os.environ.get('BETA_ISKO') : ['ghilo17 | Axie Pixel - Alpha', os.environ.get('BETA_RONIN'), os.environ.get('BETA_SK')],
    os.environ.get('GAMMA_ISKO') : ['Kyle | Axie Pixel - Gamma', os.environ.get('GAMMA_RONIN'), os.environ.get('GAMMA_SK')],
    os.environ.get('DELTA_ISKO') : ['Grace | Axie Pixel - Delta', os.environ.get('DELTA_RONIN'), os.environ.get('DELTA_SK')],
    os.environ.get('EPSILON_ISKO') : ['Luis | Axie Pixel - Gamma', os.environ.get('EPSILONG_RONIN'), os.environ.get('EPSILON_SK')],
    os.environ.get('ZETA_ISKO') : ['Tristan | Axie Pixel - Zeta', os.environ.get('ZETA_RONIN'), os.environ.get('ZETA_SK')],
    os.environ.get('ETA_ISKO') : ['Jamil | Axie Pixel - Etha', os.environ.get('ETA_RONIN'), os.environ.get('ETA_SK')],
    os.environ.get('THETA_ISKO') : ['Carlo | Axie Pixel - Etha', os.environ.get('THETA_RONIN'), os.environ.get('THETA_SK')],
    os.environ.get('IOTA_ISKO') : ['Carlo | Axie Pixel - Etha', os.environ.get('IOTA_RONIN'), os.environ.get('IOTA_SK')],
    os.environ.get('KAPPA_ISKO') : ['Francis | Axie Pixel - Kappa', os.environ.get('KAPPA_RONIN'), os.environ.get('KAPPA_SK')],
}
# Put Your Discord Bot Token Here
DiscordBotToken = os.environ.get('BOT_TOKEN')
