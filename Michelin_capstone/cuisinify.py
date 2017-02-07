coding= unicode

def cuisinify(df):

    z = [0]*len(df)

    new_lil_cuisine = z

    en_francais = z

    french_gen = z
    middle_eastern_gen = z
    traditional_gen = z
    modern_gen = z
    american_gen = z
    spanish_gen = z
    british_gen = z
    latin_american_gen = z
    asian_gen = z
    creative_gen = z
    japanese_gen = z
    thai_gen = z
    spanish_gen = z
    sub_asian_gen = z
    international_gen = z
    traditional_gen = z
    regional_gen = z
    classic_gen = z
    meats_gen = z
    british_gen = z
    italian_gen = z
    chinese_gen = z
    mediterranean_gen = z
    contemporary_gen = z
    african_gen = z
    scandinavian_gen = z
    fusion_gen = z
    eastern_european_gen = z
    sub_asian = z
    innovative_gen = z
    latin_american = z

    afghan = z
    alsatian = z
    andalusian = z
    british_mod = z
    british_trad = z
    argentinian = z
    armenian = z
    asian = z
    asian_infl = z
    thai = z
    asturian = z
    austrian = z
    bangladeshi = z
    bbq = z
    basque = z
    meats = z
    burgundy = z
    brazilian = z
    breton = z
    british = z
    burgundian = z
    burmese = z
    cajun = z
    calabrian = z
    californian = z
    campanian = z
    cantonese = z
    caribbean = z
    castilian = z
    catalan = z
    central_asian = z
    chamorro = z
    cheese_fondue_raclette = z
    classic = z
    chinese = z
    belgian = z
    home_cooking = z
    fish_seafood = z
    corsican = z
    french = z
    international = z
    creative = z
    american = z
    chiu_chow = z
    cambodian = z
    pacific = z
    modern = z
    sushi = z
    japanese = z
    traditional = z
    regional = z
    mediterranean = z
    world = z
    piedmontese = z
    ligurian = z
    provencal = z
    korean = z
    contemporary = z
    african = z
    danish = z
    deli = z
    euro_asiatic = z
    organic = z
    vegetarian = z
    spanish = z
    emilian = z
    eastern_european = z
    dumplings = z
    dim_sum = z
    ethiopian = z
    european = z
    tuscan = z
    sicilian = z
    fish_chips = z
    filipino = z
    flemish = z
    greek = z
    grill = z
    hungarian = z
    fusion = z
    moroccan = z
    hotpot = z
    hakkanese = z
    hang_zhou = z
    hawaiian = z
    hunanese = z
    gastropub = z
    german = z
    galician = z
    swiss = z
    italian = z
    lebanese = z
    south_african = z
    swedish = z
    norwegian = z
    vietnamese = z
    terroir = z
    lyonnaise = z
    savoyard = z
    portuguese = z
    tibetan = z
    russian = z
    indian = z
    turkish = z
    market = z
    peruvian = z
    innovative = z
    lombardian = z
    lazio = z
    venetian = z
    mantuan = z
    marches = z
    sardinian = z
    scandinavian = z
    polish = z
    mauritian = z
    mexican = z
    noodles = z
    macanese = z
    shanghainese = z
    sichuan = z
    indonesian = z
    xinjiang = z
    ramen = z
    shaanxi = z
    teppanyaki = z
    malaysian = z
    pakistani = z
    pizza = z
    sri_lankan = z
    southern_US = z
    persian = z
    jamaican = z
    puerto_rican = z
    nepali = z
    israeli = z
    street_food = z
    singaporean = z
    tempura = z
    fujian = z
    middle_eastern = z

    df['cuisine'] = df['cuisine'].apply(lambda x: x.lstrip())
    df['cuisine'] = df['cuisine'].apply(lambda x: x.rstrip())

    for i in range(len(df)):

        lil_cuisine = df['cuisine'][i]

        if lil_cuisine == 'Afghan':
            afghan[i] = 1
            middle_eastern_gen[i] = 1
            new_lil_cuisine[i] = 'middle_eastern'

        elif lil_cuisine == 'Alsatian':
            alsatian[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Alsatian|Modern':
            alsatian[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Alsatian|Traditional':
            alsatian[i] = 1
            french_gen[i] = 1
            traditional_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'American':
            american[i] = 1
            american_gen[i] = 1
            new_lil_cuisine[i] = 'american'

        elif lil_cuisine == 'Andalouse':
            andalusian[i] = 1
            spanish_gen[i] = 1
            en_francais[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'

        elif lil_cuisine == 'Andalusian':
            andalusian[i] = 1
            spanish_gen[i] = 1
            andalusian[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'

        elif lil_cuisine == 'Anglaise moderne':
            british_mod[i] = 1
            modern_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'british'

        elif lil_cuisine == 'Anglaise traditionnelle':
            en_francais[i] = 1
            british_trad[i] = 1
            british_gen[i] = 1
            new_lil_cuisine[i] = 'british'

        elif lil_cuisine == 'Argentinian':
            argentinian[i] = 1
            latin_american_gen[i] = 1
            new_lil_cuisine[i] = 'latin_american'

        elif lil_cuisine == 'Armenian':
            armenian[i] = 1
            new_lil_cuisine[i] = 'central_asian'

        elif lil_cuisine == 'Asados':
            meats[i] = 1
            meats_gen[i] = 1
            grill[i] = 1
            new_lil_cuisine[i] = 'meats'

        elif lil_cuisine == 'Asian':
            asian[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'asian'

        elif lil_cuisine == 'Asian|Chinese':
            asian[i] = 1
            asian_gen[i] = 1
            chinese[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Asian|Sushi':
            asian[i] = 1
            asian_gen[i] = 1
            sushi[i] = 1
            japanese_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'

        elif lil_cuisine == 'Asian|Thai|Japanese':
            asian[i] = 1
            asian_gen[i] = 1
            thai[i] = 1
            thai_gen[i] = 1
            japanese[i] = 1
            japanese_gen[i] = 1
            new_lil_cuisine[i] = 'asian'

        elif lil_cuisine == 'Asian influences':
            asian_infl[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'asian'

        elif lil_cuisine == 'Asian influences|French creative':
            french_gen[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Asiatique':
            asian[i] = 1
            asian_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'asian'

        elif lil_cuisine == 'Asturian':
            asturian[i] = 1
            spanish_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'

        elif lil_cuisine in ['Austrian', 'Austrian|International', \
            'Austrian|Regional|Traditional', 'Austrian|Traditional', 'Austrian|international']:
            austrian[i] = 1
            if 'International' in lil_cuisine:
                international_gen[i] = 1
            elif 'international' in lil_cuisine:
                international_gen[i] = 1
            elif 'Traditional' in lil_cuisine:
                traditional_gen[i] = 1
                if 'Regional' in lil_cuisine:
                    regional_gen[i] = 1
            new_lil_cuisine[i] = 'austrian'

        elif lil_cuisine == 'Bangladeshi':
            bangladeshi[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'sub_asian'

        elif lil_cuisine in ['Barbecue', 'Barbecued', 'Barbecued|International']:
            bbq[i] = 1
            if lil_cuisine == 'Barbecued|International':
                international_gen[i] = 1
            new_lil_cuisine[i] = 'meats'

        elif lil_cuisine == 'Basque':
            basque[i] = 1
            spanish_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'

        elif lil_cuisine in ['Belge| classique', 'Belgian', 'Belgian|Classic', \
                                'Belgian|French', 'Belgian|Meats', 'Belgian|Traditional']:
            belgian[i] = 1
            if lil_cuisine == 'Belge| classique':
                en_francais[i] = 1
                classic_gen[i] = 1
            elif lil_cuisine == 'Belgian|Classic':
                classic_gen[i] = 1
            elif lil_cuisine == 'Belgian|French':
                french_gen[i] = 1
                french[i] = 1
            elif lil_cuisine == 'Belgian|Meats':
                meats[i] = 1
                meats_gen[i] = 1
            new_lil_cuisine[i] = 'belgian'

        elif lil_cuisine == 'Bourguignonne':
            burgundy[i] = 1
            french_gen[i] = 1
            en_francais[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Brazilian':
            brazilian[i] = 1
            latin_american_gen[i] = 1
            new_lil_cuisine[i] = 'latin_american'

        elif lil_cuisine == 'Breton':
            breton[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'traditionnelle|Bretonne':
            breton[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            en_francais[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine in ['British contemporary', 'British creative', 'British modern', \
                           'British traditional', 'British traditional|French classic']:
            british[i] = 1
            british_gen[i] = 1
            if 'contemporary' in lil_cuisine:
                contemporary_gen[i] = 1
                new_lil_cuisine[i] = 'british'
            elif 'creative' in lil_cuisine:
                creative_gen[i] = 1
                new_lil_cuisine[i] = 'british'
            elif 'modern' in lil_cuisine:
                modern_gen[i] = 1
                new_lil_cuisine[i] = 'british'
            elif 'traditional' in lil_cuisine:
                traditional_gen[i] = 1
                new_lil_cuisine[i] = 'british'
                if 'French' in lil_cuisine:
                    french[i] = 1
                    french_gen[i] = 1
                    classic_gen[i] = 1
                    new_lil_cuisine[i] = 'british'
            new_lil_cuisine[i] = 'british'

        elif lil_cuisine in ['Burgundian', 'Burgundian|French classic']:
            burgundian[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            if 'French' in lil_cuisine:
                french[i] = 1
                classic_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Burmese':
            burmese[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'

        elif lil_cuisine == 'Cajun':
            cajun[i] = 1
            american_gen[i] = 1
            new_lil_cuisine[i] = 'american'

        elif lil_cuisine in ['Calabraise', 'Calabrian', 'Calabrian|Italian']:
            calabrian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            if 'Calabraise' in lil_cuisine:
                en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'


        elif lil_cuisine == 'Californian':
            californian[i] = 1
            american_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'american'

        elif lil_cuisine == 'Cambodian':
            cambodian[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'

        elif lil_cuisine in ['Campanian', 'Campanian|Modern', 'Campanian|Regional']:
            campanian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            if 'Modern' in lil_cuisine:
                modern_gen[i] = 1
            elif 'Regional' in lil_cuisine:
                regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'de Campanie':
            campanian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Cantonese':
            cantonese[i] = 1
            chinese_gen[i] = 1
            asian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Cantonese Roast Meats':
            cantonese[i] = 1
            chinese_gen[i] = 1
            asian_gen[i] = 1
            meats[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Caribbean':
            caribbean[i] = 1
            new_lil_cuisine[i] = 'caribbean'

        elif lil_cuisine == 'Castilian':
            castilian[i] = 1
            spanish_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'

        elif lil_cuisine == 'Catalan':
            catalan[i] = 1
            spanish_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'

        elif lil_cuisine == 'Central Asian':
            asian_gen[i] = 1
            central_asian[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'central_asian'

        elif lil_cuisine == 'Chamorro':
            chamorro[i] = 1
            pacific[i] = 1
            new_lil_cuisine[i] = 's_pacific'

        elif lil_cuisine == 'Cheese, fondue and raclette':
            cheese_fondue_raclette[i] = 1
            new_lil_cuisine[i] = 'cheese_fondue'
        elif lil_cuisine == 'traditionnelle|Fromages, fondues-raclettes':
            cheese_fondue_raclette[i] = 1
            en_francais[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'cheese_fondue'
        elif lil_cuisine == 'Cheese, fondue and raclette|Meats':
            cheese_fondue_raclette[i] = 1
            meats[i] = 1
            new_lil_cuisine[i] = 'cheese_fondue'

        elif lil_cuisine == 'Chinese':
            chinese[i] = 1
            chinese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Chinese contemporary':
            contemporary_gen[i] = 1
            chinese[i] = 1
            chinese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Chinese|Asian':
            chinese[i] = 1
            chinese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Chinese|Cantonese|Asian':
            chinese[i] = 1
            chinese_gen[i] = 1
            asian_gen[i] = 1
            cantonese[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Chinese|Modern':
            chinese[i] = 1
            chinese_gen[i] = 1
            asian_gen[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Chinoise':
            chinese[i] = 1
            chinese_gen[i] = 1
            asian_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Chiu Chow':
            chinese_gen[i] = 1
            chiu_chow[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine in ['Classic',
                         'Classic |Belgian',
                         'Classic |Corsican',
                         'Classic |Creative',
                         'Classic |Creative|Modern',
                         'Classic |Fish and seafood',
                         'Classic |French',
                         'Classic |French classic',
                         'Classic |French classic|Mediterranean',
                         'Classic |French creative',
                         'Classic |French modern',
                         'Classic |French|Traditional',
                         'Classic |Home cooking',
                         'Classic |International',
                         'Classic |International|Fusion',
                         'Classic |International|Mediterranean',
                         'Classic |International|Regional',
                         'Classic |International|Swiss',
                         'Classic |Meats',
                         'Classic |Mediterranean',
                         'Classic |Mediterranean|Asian',
                         'Classic |Modern',
                         'Classic |Modern |Regional',
                         'Classic |Piedmontese|Ligurian',
                         'Classic |Proven\xc3\xa7al',
                         'Classic |Regional',
                         'Classic |Regional|International',
                         'Classic |Regional|Mediterranean',
                         'Classic |Traditional',
                         'Classic |World',
                         'classic',
                         'classic/traditional',
                         'classic/traditional|French classic',
                         'classic|Austrian',
                         'classic|Traditional',
                         'classic|creative',
                         'classique',
                         'classique| moderne',
                         'classique|Cr\xc3\xa9ative',
                         'classique|Internationale',
                         'classique|M\xc3\xa9diterran\xc3\xa9enne',
                         'classique|Poissons et fruits de mer',
                         'classique|R\xc3\xa9gionale',
                         'classique|Terroir',
                         'classique|Viandes']:
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'classic'
            if 'Belgian' in lil_cuisine:
                belgian[i] = 1
                new_lil_cuisine[i] = 'belgian'
            elif 'Corsican' in lil_cuisine:
                corsican[i] = 1
                new_lil_cuisine[i] = 'french'
            elif 'Creative' in lil_cuisine:
                creative[i] = 1
                creative_gen[i] = 1
                if 'Modern' in lil_cuisine:
                    modern[i] = 1
                    modern_gen[i] = 1
                    new_lil_cuisine[i] = 'modern'
                else:
                    new_lil_cuisine[i] = 'creative'
            elif 'Fish' in lil_cuisine:
                fish_seafood[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine in ['Classic |French', 'Classic |French classic', \
                    'Classic |French classic|Mediterranean', 'Classic |French creative',
                    'Classic |French modern', 'Classic |French|Traditional']:
                french_gen[i] = 1
                if lil_cuisine == 'Classic |French creative':
                    creative_gen[i] = 1
                elif lil_cuisine == 'Classic |French modern':
                    modern_gen[i] = 1
                elif lil_cuisine == 'Classic |French|Traditional':
                    traditional_gen[i] = 1
                new_lil_cuisine[i] = 'french'
            elif 'Home cooking' in lil_cuisine:
                home_cooking[i] = 1
                new_lil_cuisine[i] = 'home_cooking'
            elif 'International' in lil_cuisine:
                international[i] = 1
                international_gen[i] = 1
                new_lil_cuisine[i] = 'international'
            elif 'Meats' in lil_cuisine:
                meats[i] = 1
                new_lil_cuisine[i] = 'meats'
            elif lil_cuisine in ['Classic |Mediterranean', 'Classic |Mediterranean|Asian']:
                mediterranean[i] = 1
                mediterranean_gen[i] = 1
                if 'Asian' in lil_cuisine:
                    asian_gen[i] = 1
                new_lil_cuisine[i] = 'mediterranean'
            elif lil_cuisine in ['Classic |Modern', 'Classic |Modern |Regional']:
                modern[i] = 1
                modern_gen[i] = 1
                if 'Regional' in lil_cuisine:
                    regional_gen[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'Classic |Piedmontese|Ligurian':
                italian_gen[i] = 1
                regional_gen[i] = 1
                if 'Piedmontese' in lil_cuisine:
                    piedmontese[i] = 1
                elif 'Ligurian' in lil_cuisine:
                    ligurian[i] = 1
                new_lil_cuisine[i] = 'italian'
            elif lil_cuisine == 'Classic |Proven\xc3\xa7al':
                provencal[i] = 1
                french_gen[i] = 1
                regional_gen[i] = 1
                new_lil_cuisine[i] = 'french'
            elif lil_cuisine in ['Classic |Regional', 'Classic |Regional|International', \
                                 'Classic |Regional|Mediterranean']:
                regional[i] = 1
                new_lil_cuisine[i] = 'classic'
                if 'International' in lil_cuisine:
                    international[i] = 1
                    new_lil_cuisine[i] = 'international'
                elif 'Mediterranean' in lil_cuisine:
                    mediterranean[i] = 1
                    new_lil_cuisine[i] = 'mediterranean'
            elif lil_cuisine == 'Classic |Traditional':
                traditional[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'Classic |World':
                world[i] = 1
                new_lil_cuisine[i] = 'world'
            elif lil_cuisine == 'classic':
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'classic/traditional':
                traditional[i] = 1
                traditional_gen[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'classic/traditional|French classic':
                traditional[i] = 1
                traditional_gen[i] = 1
                french_gen[i] = 1
                new_lil_cuisine[i] = 'french'
            elif lil_cuisine == 'classic|Austrian':
                austrian[i] = 1
                new_lil_cuisine[i] = 'austrian'
            elif lil_cuisine == 'classic|Traditional':
                traditional[i] = 1
                traditional_gen[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'classic|creative':
                creative[i] = 1
                creative_gen[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'classique':
                en_francais[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'classique| moderne':
                en_francais[i] = 1
                modern[i] = 1
                modern_gen[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'classique|Cr\xc3\xa9ative':
                en_francais[i] = 1
                creative[i] = 1
                creative_gen[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'classique|Internationale':
                en_francais[i] = 1
                international[i] = 1
                international_gen[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'classique|M\xc3\xa9diterran\xc3\xa9enne':
                mediterranean[i] = 1
                mediterranean_gen[i] = 1
                new_lil_cuisine[i] = 'mediterranean'
            elif lil_cuisine == 'classique|R\xc3\xa9gionale':
                en_francais[i] = 1
                regional[i] = 1
                regional_gen[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'classique|Terroir':
                en_francais[i] = 1
                terroir[i] = 1
                new_lil_cuisine[i] = 'terroir'
            elif lil_cuisine == 'classique|Viandes':
                en_francais[i] = 1
                meats[i] = 1
                meats_gen[i] = 1
                new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'classique|Poissons et fruits de mer':
            en_francais[i] = 1
            fish_seafood[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] == 'fish_seafood'

        elif lil_cuisine == 'Congee':
            asian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'street_food'

        elif lil_cuisine == 'Contemporary':
            contemporary[i] = 1
            contemporary_gen[i] = 1
            new_lil_cuisine[i] = 'contemporary'

        elif lil_cuisine == 'Corse':
            corsican[i] = 1
            french_gen[i] = 1
            mediterranean_gen[i] = 1
            en_francais[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Corse|Poissons et fruits de mer':
            corsican[i] = 1
            french_gen[i] = 1
            mediterranean_gen[i] = 1
            fish_seafood[i] = 1
            en_francais[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Corsican':
            corsican[i] = 1
            french_gen[i] = 1
            mediterranean_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Corsican|French modern':
            corsican[i] = 1
            french_gen[i] = 1
            mediterranean_gen[i] = 1
            modern_gen[i] = 1
            regional[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Cor\xc3\xa9enne':
            korean[i] = 1
            asian_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'korean'

        elif lil_cuisine in ['Creative',
                         'Creative|African',
                         'Creative|Asian',
                         'Creative|Asian influences',
                         'Creative|Campanian',
                         'Creative|Classic',
                         'Creative|Creative',
                         'Creative|Creative|International',
                         'Creative|Fish and seafood',
                         'Creative|French',
                         'Creative|French classic',
                         'Creative|French modern',
                         'Creative|French modern|Modern',
                         'Creative|International',
                         'Creative|International|Classic',
                         'Creative|Japanese',
                         'Creative|Mediterranean',
                         'Creative|Modern',
                         'Creative|Modern |Classic',
                         'Creative|Organic',
                         'Creative|Regional',
                         'Creative|Traditional',
                         'Creative|Vegetarian',
                         'Cr\xc3\xa9ative',
                         'Cr\xc3\xa9ative| classique',
                         'Cr\xc3\xa9ative| moderne',
                         'Cr\xc3\xa9ative|Fran\xc3\xa7aise',
                         'Cr\xc3\xa9ative|Internationale',
                         'Cr\xc3\xa9ative|Poissons et fruits de mer',
                         'creative',
                         'creative|classic',
                         'creative|modern',
                         'creative|regional/country',
                         'regional/country|creative']:
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'creative'
            if 'African' in lil_cuisine:
                african[i] = 1
                african_gen[i] = 1
                new_lil_cuisine[i] = 'african'
            elif lil_cuisine == 'Creative|Asian':
                asian[i] = 1
                asian_gen[i] = 1
                new_lil_cuisine[i] = 'asian'
            elif lil_cuisine == 'Creative|Asian influences':
                asian_infl[i] = 1
                asian_gen[i] = 1
                new_lil_cuisine[i] = 'asian'
            elif lil_cuisine == 'Creative|Campanian':
                campanian[i] = 1
                italian_gen[i] = 1
                regional_gen[i] = 1
                new_lil_cuisine[i] = 'italian'
            elif lil_cuisine == 'Creative|Classic':
                classic[i] = 1
                classic_gen[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'Creative|Creative':
                new_lil_cuisine[i] = 'creative'
            elif lil_cuisine == 'Creative|Creative|International':
                international[i] = 1
                international_gen[i] = 1
                new_lil_cuisine[i] = 'creative'
            elif lil_cuisine == 'Creative|Fish and seafood':
                fish_seafood[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine in ['Creative|French',
                                 'Creative|French classic',
                                 'Creative|French modern',
                                 'Creative|French modern|Modern']:
                french[i] = 1
                french_gen[i] = 1
                if lil_cuisine == 'Creative|French classic':
                    classic_gen[i] = 1
                elif lil_cuisine in ['Creative|French modern', 'Creative|French modern|Modern']:
                    modern_gen[i] = 1
                new_lil_cuisine[i] = 'french'
            elif lil_cuisine == 'Creative|International|Classic':
                international[i] = 1
                international_gen[i] = 1
                classic[i] = 1
                classic_gen[i] = 1
                new_lil_cuisine[i] = 'classic'
            elif lil_cuisine == 'Creative|Japanese':
                japanese[i] = 1
                japanese_gen[i] = 1
                asian_gen[i] = 1
                new_lil_cuisine[i] = 'japanese'
            elif lil_cuisine == 'Creative|Mediterranean':
                mediterranean[i] = 1
                mediterranean_gen[i] = 1
                new_lil_cuisine[i] = 'mediterranean'
            elif lil_cuisine in ['Creative|Modern', 'Creative|Modern |Classic', 'creative|modern']:
                modern[i] = 1
                modern_gen[i] = 1
                if lil_cuisine == 'Creative|Modern |Classic':
                    classic[i] = 1
                    classic_gen[i] = 1
                new_lil_cuisine[i] = 'modern'
            elif lil_cuisine == 'Creative|Organic':
                organic[i] = 1
                new_lil_cuisine[i] = 'organic'
            elif lil_cuisine == 'Creative|Regional':
                regional[i] = 1
                regional_gen[i] = 1
                new_lil_cuisine[i] = 'creative'
            elif lil_cuisine == 'Creative|Traditional':
                traditional[i] = 1
                traditional_gen[i] = 1
                new_lil_cuisine[i] = 'traditional'
            elif lil_cuisine == 'Creative|Vegetarian':
                vegetarian[i] = 1
                new_lil_cuisine[i] = 'vegetarian_vegan'
            elif lil_cuisine in ['Cr\xc3\xa9ative',
                                 'Cr\xc3\xa9ative| classique',
                                 'Cr\xc3\xa9ative| moderne',
                                 'Cr\xc3\xa9ative|Fran\xc3\xa7aise',
                                 'Cr\xc3\xa9ative|Internationale',
                                 'Cr\xc3\xa9ative|Poissons et fruits de mer']:
                en_francais[i] = 1
                new_lil_cuisine[i] = 'creative'
                if lil_cuisine == 'Cr\xc3\xa9ative| classique':
                    classic[i] = 1
                    classic_gen[i] = 1
                    en_francais[i] = 1
                    new_lil_cuisine[i] = 'classic'
                elif lil_cuisine == 'Cr\xc3\xa9ative| moderne':
                    modern[i] = 1
                    modern_gen[i] = 1
                    new_lil_cuisine[i] = 'modern'
                elif lil_cuisine == 'Cr\xc3\xa9ative|Fran\xc3\xa7aise':
                    french[i] = 1
                    french_gen[i] = 1
                    new_lil_cuisine[i] = 'french'
                elif lil_cuisine == 'Cr\xc3\xa9ative|Internationale':
                    international[i] = 1
                    international_gen[i] = 1
                    new_lil_cuisine[i] = 'international'
                elif lil_cuisine == 'Cr\xc3\xa9ative|Poissons et fruits de mer':
                    fish_seafood[i] = 1
                    en_francais[i] = 1
                    new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine == 'creative|classic':
                classic[i] = 1
                classic_gen[i] = 1
                new_lil_cuisine[i] = 'creative'
            elif lil_cuisine in ['creative|regional/country', 'regional/country|creative']:
                regional[i] = 1
                regional_gen[i] = 1
                new_lil_cuisine[i] = 'creative'


        elif lil_cuisine == 'Danish':
            danish[i] = 1
            scandinavian_gen[i] = 1
            new_lil_cuisine[i] = 'danish'
        elif lil_cuisine == 'modern|sm\xc3\xb8rrebr\xc3\xb8d':
            modern[i] = 1
            modern_gen[i] = 1
            scandinavian_gen[i] = 1
            new_lil_cuisine[i] = 'scandinavian'
        elif lil_cuisine == 'sm\xc3\xb8rrebr\xc3\xb8d':
            scandinavian_gen[i] = 1
            new_lil_cuisine[i] = 'scandinavian'

        elif lil_cuisine == 'Deli':
            deli[i] = 1
            new_lil_cuisine[i] = 'deli'

        elif lil_cuisine == 'Dim Sum':
            dim_sum[i] = 1
            asian_gen[i] = 1
            chinese_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Dumplings':
            dumplings[i] = 1
            asian_gen[i] = 1
            chinese_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Eastern European':
            eastern_european[i] = 1
            eastern_european_gen[i] = 1
            new_lil_cuisine[i] = 'eastern_european'

        elif lil_cuisine in ['Emilian', 'Emilian|Classic', 'Emilian|Regional', 'Emilienne']:
            emilian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            if lil_cuisine == 'Emilian|Classic':
                classic[i] = 1
            elif lil_cuisine == 'Emilian|Regional':
                regional[i] = 1
            elif lil_cuisine == 'Emilienne':
                en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Espagnole':
            spanish[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'spanish'

        elif lil_cuisine == 'Ethiopian':
            ethiopian[i] = 1
            african_gen[i] = 1
            new_lil_cuisine[i] = 'african'

        elif lil_cuisine == 'Euro-asiatic':
            european[i] = 1
            new_lil_cuisine[i] = 'european'

        elif lil_cuisine == 'European':
            european[i] = 1
            new_lil_cuisine[i] = 'european'

        elif lil_cuisine == 'European contemporary':
            european[i] = 1
            contemporary_gen[i] = 1
            new_lil_cuisine[i] = 'european'

        elif lil_cuisine == 'Filipino':
            filipino[i] = 1
            pacific[i] = 1
            new_lil_cuisine[i] = 's_pacific'

        elif lil_cuisine == 'Fish and chips':
            fish_chips[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'

        elif lil_cuisine in ['Fish and seafood',
                         'Fish and seafood|Asturian',
                         'Fish and seafood|Belgian',
                         'Fish and seafood|Classic',
                         'Fish and seafood|Creative',
                         'Fish and seafood|French modern',
                         'Fish and seafood|International',
                         'Fish and seafood|Ligurian',
                         'Fish and seafood|Meats',
                         'Fish and seafood|Modern',
                         'Fish and seafood|Regional',
                         'Fish and seafood|Regional|Traditional',
                         'Fish and seafood|Sicilian',
                         'Fish and seafood|Sushi|Meats',
                         'Fish and seafood|Traditional',
                         'Fish and seafood|Traditional |Mediterranean',
                         'Fish and seafood|Tuscan',
                         'fish and seafood']:
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'
            if lil_cuisine == 'Fish and seafood|Asturian':
                asturian[i] = 1
                spanish_gen[i] = 1
                new_lil_cuisine[i] = 'spanish'
            elif lil_cuisine == 'Fish and seafood|Belgian':
                belgian[i] = 1
                new_lil_cuisine[i] = 'belgian'
            elif lil_cuisine == 'Fish and seafood|Classic':
                classic[i] = 1
                classic_gen[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine == 'Fish and seafood|Creative':
                creative[i] = 1
                creative_gen[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine == 'Fish and seafood|French modern':
                french_gen[i] = 1
                modern_gen[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine == 'Fish and seafood|International':
                international[i] = 1
                international_gen[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine == 'Fish and seafood|Ligurian':
                ligurian[i] = 1
                italian_gen[i] = 1
                regional_gen[i] = 1
                new_lil_cuisine[i] = 'italian'
            elif lil_cuisine == 'Fish and seafood|Meats':
                meats[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine == 'Fish and seafood|Modern':
                modern[i] = 1
                modern_gen[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine in ['Fish and seafood|Regional',
                                 'Fish and seafood|Regional|Traditional']:
                regional[i] = 1
                regional_gen[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
                if lil_cuisine == 'Fish and seafood|Regional|Traditional':
                    traditional[i] = 1
                    traditional_gen[i] = 1
                    new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine == 'Fish and seafood|Sicilian':
                sicilian[i] = 1
                italian_gen[i] = 1
                regional_gen[i] = 1
                new_lil_cuisine[i] = 'italian'
            elif lil_cuisine == 'Fish and seafood|Sushi|Meats':
                meats[i] = 1
                sushi[i] = 1
                japanese_gen[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine == 'Fish and seafood|Traditional':
                traditional[i] = 1
                traditional_gen[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine == 'Fish and seafood|Traditional |Mediterranean':
                traditional[i] = 1
                traditional_gen[i] = 1
                mediterranean[i] = 1
                mediterranean_gen[i] = 1
                new_lil_cuisine[i] = 'fish_seafood'
            elif lil_cuisine == 'Fish and seafood|Tuscan':
                tuscan[i] = 1
                italian_gen[i] = 1
                new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'poissons et fruits de mer':
            fish_seafood[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'

        elif lil_cuisine in ['Flamande',
                         'Flemish',
                         'Flemish|Regional']:
            flemish[i] = 1
            belgian[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            if lil_cuisine == 'Flamande':
                en_francais[i] = 1
            new_lil_cuisine[i] = 'belgian'

        elif lil_cuisine == 'Franche-comt\xc3':
            french_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        ## FRENCH
        elif lil_cuisine in ['Fran\xc3\xa7aise', 'fran\xc3\xa7aise']:
            french[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Fran\xc3\xa7aise classique':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Fran\xc3\xa7aise classique|Cr\xc3\xa9ative':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Fran\xc3\xa7aise classique|Fran\xc3\xa7aise moderne':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            modern_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Fran\xc3\xa7aise classique|Internationale':
            french[i] = 1
            french_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Fran\xc3\xa7aise cr\xc3\xa9ative':
            french[i] = 1
            french_gen[i] = 1
            creative_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Fran\xc3\xa7aise cr\xc3\xa9ative|Fran\xc3\xa7aise moderne':
            french[i] = 1
            french_gen[i] = 1
            creative_gen[i] = 1
            modern_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Fran\xc3\xa7aise moderne':
            french[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French':
            french[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|Classic':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|French modern':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|Hungarian':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            hungarian[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|International':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|Italian':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|Meats':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|Mediterranean':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|Modern':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|Regional':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|Regional|Mediterranean':
            french[i] = 1
            french_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|Swiss':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            swiss[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French classic|Traditional':
            french[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French contemporary':
            french[i] = 1
            french_gen[i] = 1
            contemporary_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French creative':
            french[i] = 1
            french_gen[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French creative|Creative':
            french[i] = 1
            french_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French creative|French modern':
            french[i] = 1
            french_gen[i] = 1
            creative_gen[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French creative|International':
            french[i] = 1
            french_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French creative|Modern':
            french[i] = 1
            french_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French modern':
            french[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French modern|Burgundian':
            french[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            burgundian[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French modern|Classic':
            french[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French modern|Creative':
            french[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French modern|French':
            french[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French modern|French classic':
            french[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French modern|French creative':
            french[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French modern|Modern':
            french[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            modern[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French modern|Regional':
            french[i] = 1
            french_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French|Classic':
            french[i] = 1
            french_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French|International':
            french[i] = 1
            french_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French|Mediterranean':
            french[i] = 1
            french_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French|Modern':
            french[i] = 1
            french_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French|Moroccan':
            french[i] = 1
            french_gen[i] = 1
            moroccan[i] = 1
            african_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French|Regional':
            french[i] = 1
            french_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French|Regional|Traditional':
            french[i] = 1
            french_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'French|Traditional':
            french[i] = 1
            french_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'french'


        elif lil_cuisine == 'Fujian':
            fujian[i] = 1
            chinese_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Fusion':
            fusion[i] = 1
            fusion_gen[i] = 1
            new_lil_cuisine[i] = 'fusion'
        elif lil_cuisine == 'Fusion|Japanese':
            fusion[i] = 1
            fusion_gen[i] = 1
            japanese[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Fusion|Meats':
            fusion[i] = 1
            fusion_gen[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'fusion'
        elif lil_cuisine == 'Fusion|Modern':
            fusion[i] = 1
            fusion_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'fusion'  ## FUSION or MODERN
        elif lil_cuisine == 'Fusion|Regional':
            fusion[i] = 1
            fusion_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'fusion'
        elif lil_cuisine == 'Fusion|Sushi|Meats':
            fusion[i] = 1
            fusion_gen[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            sushi[i] = 1
            japanese_gen[i] = 1
            new_lil_cuisine[i] = 'fusion'
        elif lil_cuisine == 'Fusion|Swiss':
            fusion[i] = 1
            fusion_gen[i] = 1
            swiss[i] = 1
            new_lil_cuisine[i] = 'swiss'

        elif lil_cuisine == 'Galician':
            galician[i] = 1
            spanish_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'
        elif lil_cuisine == 'Galician|Fish and seafood':
            galician[i] = 1
            spanish_gen[i] = 1
            regional_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'spanish'

        elif lil_cuisine == 'Gastropub':
            gastropub[i] = 1
            new_lil_cuisine[i] = 'gastropub'

        elif lil_cuisine == 'German':
            german[i] = 1
            new_lil_cuisine[i] = 'german'

        elif lil_cuisine in ['Grecque', 'grecque']:
            en_francais[i] = 1
            greek[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'greek'
        elif lil_cuisine == 'Greek':
            greek[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'greek'
        elif lil_cuisine == 'Greek|Creative':
            greek[i] = 1
            mediterranean_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'greek'
        elif lil_cuisine == 'Greek|Mediterranean':
            greek[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'greek'

        elif lil_cuisine == 'Grill':
            grill[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine in ['Grillades', 'viandes et grillades']:
            grill[i] = 1
            meats_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Grillades| classique':
            grill[i] = 1
            meats_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Grill|Meats':
            grill[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Grill|Meats|Classic':
            grill[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Grill|Modern':
            grill[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'meats'

        elif lil_cuisine == 'Hakkanese':
            chinese_gen[i] = 1
            regional_gen[i] = 1
            hakkanese[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Hang Zhou':
            chinese_gen[i] = 1
            regional_gen[i] = 1
            hang_zhou[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Hawaiian':
            pacific[i] = 1
            hawaiian[i] = 1
            american[i] = 1
            new_lil_cuisine[i] = 's_pacific'

        elif lil_cuisine == 'Home cooking':
            home_cooking[i] = 1
            regional_gen[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'home_cooking'
        elif lil_cuisine == 'Home cooking|Traditional':
            home_cooking[i] = 1
            regional_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'home_cooking'

        elif lil_cuisine == 'Hotpot':
            hotpot[i] = 1
            chinese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Hunanese':
            hunanese[i] = 1
            chinese_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'
        elif lil_cuisine == 'Hunanese and Sichuan':
            hunanese[i] = 1
            sichuan[i] = 1
            chinese_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Hungarian':
            hungarian[i] = 1
            eastern_european_gen[i] = 1
            new_lil_cuisine[i] = 'eastern_european'
        elif lil_cuisine == 'Hungarian|Traditional':
            hungarian[i] = 1
            eastern_european_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'eastern_european'
        elif lil_cuisine == 'Hungarian|international':
            hungarian[i] = 1
            eastern_european_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'eastern_european'
        elif lil_cuisine == 'Hungarian|modern':
            hungarian[i] = 1
            eastern_european_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'eastern_european'
        elif lil_cuisine == 'meats and grills|Hungarian':
            hungarian[i] = 1
            eastern_european_gen[i] = 1
            meats[i] = 1
            new_lil_cuisine[i] = 'eastern_european'

        ## INDIAN
        elif lil_cuisine == 'Indian':
            indian[i] = 1
            sub_asian[i] = 1
            new_lil_cuisine[i] = 'sub_asian'
        elif lil_cuisine == 'Indian vegetarian':
            indian[i] = 1
            sub_asian[i] = 1
            vegetarian[i] = 1
            new_lil_cuisine[i] = 'sub_asian'
        elif lil_cuisine == 'Indienne':
            en_francais[i] = 1
            indian[i] = 1
            sub_asian[i] = 1
            new_lil_cuisine[i] = 'sub_asian'

        elif lil_cuisine == 'Indonesian':
            indonesian[i] = 1
            pacific[i] = 1
            new_lil_cuisine[i] = 'SE_asian'

        elif lil_cuisine == 'Influences asiatiques':
            en_francais[i] = 1
            asian_gen[i] = 1
            asian_infl[i] = 1
            new_lil_cuisine[i] = 'asian'

        elif lil_cuisine in ['Innovative', 'innovative']:
            innovative[i] = 1
            innovative_gen[i] = 1
            new_lil_cuisine[i] = 'innovative'
        elif lil_cuisine == 'innovante':
            innovative[i] = 1
            innovative_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'innovative'
        elif lil_cuisine == 'modern|innovative':
            modern[i] = 1
            modern_gen[i] = 1
            innovative[i] = 1
            new_lil_cuisine[i] = 'innovative'

        ## INTERNATIONAL
        elif lil_cuisine in ['International', 'international']:
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'Internationale':
            international[i] = 1
            international_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'Internationale| classique':
            international[i] = 1
            international_gen[i] = 1
            en_francais[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine in ['Internationale| traditionnelle', 'traditionnelle|Internationale',\
                            'traditionnelle|internationale']:
            international[i] = 1
            international_gen[i] = 1
            en_francais[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'Internationale|Terroir':
            international[i] = 1
            international_gen[i] = 1
            en_francais[i] = 1
            terroir[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'Internationale|Viandes':
            international[i] = 1
            international_gen[i] = 1
            en_francais[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'International|African':
            international[i] = 1
            international_gen[i] = 1
            african[i] = 1
            african_gen[i] = 1
            new_lil_cuisine[i] = 'african'
        elif lil_cuisine == 'International|Austrian':
            international[i] = 1
            international_gen[i] = 1
            austrian[i] = 1
            new_lil_cuisine[i] = 'austrian'
        elif lil_cuisine == 'International|Classic':
            international[i] = 1
            international_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine in ['International|Creative', 'international|creative']:
            international[i] = 1
            international_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'International|Fish and seafood':
            international[i] = 1
            international_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'
        elif lil_cuisine == 'International|French':
            international[i] = 1
            international_gen[i] = 1
            french[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'International|French modern':
            international[i] = 1
            international_gen[i] = 1
            french[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'International|French|Mediterranean':
            international[i] = 1
            international_gen[i] = 1
            french[i] = 1
            french_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'International|Fusion':
            international[i] = 1
            international_gen[i] = 1
            fusion[i] = 1
            fusion_gen[i] = 1
            new_lil_cuisine[i] = 'fusion'
        elif lil_cuisine == 'International|Home cooking':
            international[i] = 1
            international_gen[i] = 1
            home_cooking[i] = 1
            new_lil_cuisine[i] = 'home_cooking'
        elif lil_cuisine == 'International|Mauritian':
            international[i] = 1
            international_gen[i] = 1
            mauritian[i] = 1
            pacific[i] = 1
            new_lil_cuisine[i] = 's_pacific'
        elif lil_cuisine == 'International|Meats':
            international[i] = 1
            international_gen[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'International|Meats|Regional':
            international[i] = 1
            international_gen[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'International|Mediterranean':
            international[i] = 1
            international_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'International|Mediterranean|Creative':
            international[i] = 1
            international_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'International|Mediterranean|Traditional':
            international[i] = 1
            international_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine in ['International|Modern', 'international|modern']:
            international[i] = 1
            international_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'International|Modern |Swiss':
            international[i] = 1
            international_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            swiss[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'International|Portuguese':
            international[i] = 1
            international_gen[i] = 1
            portuguese[i] = 1
            new_lil_cuisine[i] = 'portuguese'
        elif lil_cuisine in ['International|Regional', 'international|regional/country', \
                             'regional/country|international']:
            international[i] = 1
            international_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'International|Regional|Italian':
            international[i] = 1
            international_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            italian[i] = 1
            italian_gen[i]
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'International|Regional|Traditional':
            international[i] = 1
            international_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i]
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'International|Swiss':
            international[i] = 1
            international_gen[i] = 1
            swiss[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'International|Traditional':
            international[i] = 1
            international_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i]
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'International|World':
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'international'

        elif lil_cuisine == 'Israeli':
            israeli[i] = 1
            middle_eastern_gen[i] = 1
            new_lil_cuisine[i] = 'middle_eastern'

        ## ITALIAN
        elif lil_cuisine == 'Italian':
            italian[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'italienne':
            italian[i] = 1
            italian_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian-American':
            italian_gen[i] = 1
            american_gen[i] = 1
            new_lil_cuisine[i] = 'american'
        elif lil_cuisine == 'Italian|Classic':
            italian[i] = 1
            italian_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|Classic |Mediterranean':
            italian[i] = 1
            italian_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|Creative':
            italian[i] = 1
            italian_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|Fish and seafood':
            italian[i] = 1
            italian_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|French modern':
            italian[i] = 1
            italian_gen[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|International':
            italian[i] = 1
            italian_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|International|Regional':
            italian[i] = 1
            italian_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|Mediterranean':
            italian[i] = 1
            italian_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|Modern':
            italian[i] = 1
            italian_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|Proven\xc3\xa7al':
            provencal[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|Sardinian':
            sardinian[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|Sushi':
            italian[i] = 1
            italian_gen[i] = 1
            sushi[i] = 1
            japanese_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|Swiss':
            swiss[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italian|Traditional':
            italian[i] = 1
            italian_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italienne':
            italian[i] = 1
            italian_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Italienne|Sicilienne':
            sicilian[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Jamaican':
            jamaican[i] = 1
            new_lil_cuisine[i] = 'caribbean'

        ## JAPANESE
        elif lil_cuisine == 'Japanese':
            japanese[i] = 1
            japanese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japanese contemporary':
            japanese_gen[i] = 1
            contemporary_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japanese|Asian':
            japanese[i] = 1
            japanese_gen[i] = 1
            asian[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japanese|Fusion':
            japanese[i] = 1
            japanese_gen[i] = 1
            fusion[i] = 1
            fusion_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japanese|International':
            japanese[i] = 1
            japanese_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japanese|Korean':
            japanese[i] = 1
            japanese_gen[i] = 1
            korean[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japanese|Modern':
            japanese[i] = 1
            japanese_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japanese|Peruvian':
            japanese[i] = 1
            japanese_gen[i] = 1
            peruvian[i] = 1
            latin_american_gen[i] = 1
            asian_gen[i] = 1
            fusion_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japanese|Sushi':
            japanese[i] = 1
            japanese_gen[i] = 1
            sushi[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japanese|Sushi|Fusion':
            japanese[i] = 1
            japanese_gen[i] = 1
            sushi[i] = 1
            fusion[i] = 1
            fusion_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japanese|sushi':
            japanese[i] = 1
            japanese_gen[i] = 1
            sushi[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine in ['Japonaise', 'japonaise']:
            japanese[i] = 1
            japanese_gen[i] = 1
            asian_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japonaise|Internationale':
            en_francais[i] = 1
            japanese[i] = 1
            japanese_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japonaise|Sushi':
            en_francais[i] = 1
            japanese[i] = 1
            japanese_gen[i] = 1
            sushi[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Japonaise|Teppanyaki':
            en_francais[i] = 1
            japanese[i] = 1
            japanese_gen[i] = 1
            teppanyaki[i] = 1
            regional_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'

        elif lil_cuisine == 'Korean':
            korean[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'korean'
        elif lil_cuisine == 'Korean|Asian':
            korean[i] = 1
            asian_gen[i] = 1
            asian[i] = 1
            new_lil_cuisine[i] = 'korean'

        elif lil_cuisine == 'Latin American':
            latin_american[i] = 1
            latin_american_gen[i] = 1
            new_lil_cuisine[i] = 'latin_american'

        ## LEBANESE
        elif lil_cuisine == 'Lebanese':
            lebanese[i] = 1
            middle_eastern_gen[i] = 1
            new_lil_cuisine[i] = 'middle_eastern'
        elif lil_cuisine == 'Libanaise':
            lebanese[i] = 1
            middle_eastern_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'middle_eastern'

        elif lil_cuisine == 'Ligurian':
            ligurian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Ligurienne':
            en_francais[i] = 1
            ligurian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Lombarde':
            en_francais[i] = 1
            lombardian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Lombardian':
            lombardian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Lyonnaise':
            lyonnaise[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Macanese':
            macanese[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'

        elif lil_cuisine == 'Malaysian':
            malaysian[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'

        elif lil_cuisine == 'Mantuan':
            mantuan[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Mantuan|Asian':
            mantuan[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            fusion_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Mantuan|Italian':
            mantuan[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Market':
            market[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'market'
        elif lil_cuisine == 'Market |Classic':
            market[i] = 1
            regional_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'market'
        elif lil_cuisine == 'Market |Creative':
            market[i] = 1
            regional_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'market'
        elif lil_cuisine == 'Market |French modern':
            market[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'market'
        elif lil_cuisine == 'Market |International':
            market[i] = 1
            regional_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'market'
        elif lil_cuisine == 'Market |Modern':
            market[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'market'

        elif lil_cuisine == 'Meats':
            meats[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine in ['Meats and Grills', 'meats and grills']:
            meats[i] = 1
            grill[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'modern|meats and grills':
            meats[i] = 1
            grill[i] = 1
            meats_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'modern|meats and grills|international':
            meats[i] = 1
            grill[i] = 1
            meats_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|Barbecued':
            meats[i] = 1
            bbq[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|Castilian':
            meats[i] = 1
            meats_gen[i] = 1
            castilian[i] = 1
            spanish_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|Classic':
            meats[i] = 1
            meats_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|French classic':
            meats[i] = 1
            meats_gen[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|French modern':
            meats[i] = 1
            meats_gen[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|International':
            meats[i] = 1
            meats_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|Japanese':
            meats[i] = 1
            meats_gen[i] = 1
            japanese[i] = 1
            japanese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Meats|Mediterranean':
            meats[i] = 1
            meats_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|Regional':
            meats[i] = 1
            meats_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|Sushi':
            meats[i] = 1
            meats_gen[i] = 1
            sushi[i] = 1
            japanese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|Traditional':
            meats[i] = 1
            meats_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Meats|Vegetarian':
            meats[i] = 1
            meats_gen[i] = 1
            vegetarian[i] = 1
            new_lil_cuisine[i] = 'meats'

        elif lil_cuisine == 'Mediterranean':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Mediterranean|Asian influences':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            asian_infl[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Mediterranean|Classic':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Mediterranean|Creative':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Mediterranean|Fish and seafood':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'
        elif lil_cuisine == 'Mediterranean|French':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            french[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Mediterranean|French classic':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Mediterranean|International':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Mediterranean|Italian':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Mediterranean|Italian|Modern':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Mediterranean|Meats':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Mediterranean|Modern':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Mediterranean|Portuguese|Spanish':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            portuguese[i] = 1
            spanish[i] = 1
            spanish_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'
        elif lil_cuisine == 'Mediterranean|Regional':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Mediterranean|Swiss':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            swiss[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Mediterranean|Traditional':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Mediterranean|modern':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'

        elif lil_cuisine == 'Mexicaine':
            en_francais[i] = 1
            mexican[i] = 1
            latin_american_gen[i] = 1
            new_lil_cuisine[i] = 'latin_american'
        elif lil_cuisine == 'Mexican':
            mexican[i] = 1
            latin_american_gen[i] = 1
            new_lil_cuisine[i] = 'latin_american'

        elif lil_cuisine == 'Middle Eastern':
            middle_eastern[i] = 1
            middle_eastern_gen[i] = 1
            new_lil_cuisine[i] = 'middle_eastern'
        elif lil_cuisine == 'Middle Eastern |Moroccan|Lebanese':
            middle_eastern[i] = 1
            middle_eastern_gen[i] = 1
            moroccan[i] = 1
            lebanese[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'middle_eastern'

        elif lil_cuisine == 'Milanese':
            lombardian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine in ['Modern', 'modern']:
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'modern'
        elif lil_cuisine == 'moderne':
            modern[i] = 1
            modern_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'modern'
        elif lil_cuisine == 'Modern |Classic':
            modern[i] = 1
            modern_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'modern'
        elif lil_cuisine == 'Modern |Classic |Regional':
            modern[i] = 1
            modern_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'modern'
        elif lil_cuisine == 'Modern |Corsican|Fish and seafood':
            modern[i] = 1
            modern_gen[i] = 1
            corsican[i] = 1
            french_gen[i] = 1
            mediterranean_gen[i] = 1
            fish_seafood[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Modern |Creative':
            modern[i] = 1
            modern_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'modern'
        elif lil_cuisine == 'Modern |Creative|Asian':
            modern[i] = 1
            modern_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            asian[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'modern'
        elif lil_cuisine == 'Modern |Creative|Classic':
            modern[i] = 1
            modern_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'modern'
        elif lil_cuisine == 'Modern |Fish and seafood':
            modern[i] = 1
            modern_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'
        elif lil_cuisine == 'Modern |French':
            modern[i] = 1
            modern_gen[i] = 1
            french[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Modern |French classic':
            modern[i] = 1
            modern_gen[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Modern |French modern':
            modern[i] = 1
            modern_gen[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine in ['Modern |International', 'modern|international']:
            modern[i] = 1
            modern_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'modern'
        elif lil_cuisine == 'Modern |Italian':
            modern[i] = 1
            modern_gen[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Modern |Japanese':
            modern[i] = 1
            modern_gen[i] = 1
            japanese[i] = 1
            japanese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Modern |Mediterranean':
            modern[i] = 1
            modern_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'moderne|M\xc3\xa9diterran\xc3\xa9enne':
            modern[i] = 1
            modern_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Modern |Mediterranean|Classic':
            modern[i] = 1
            modern_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Modern |Mediterranean|Creative':
            modern[i] = 1
            modern_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Modern |Organic':
            modern[i] = 1
            modern_gen[i] = 1
            organic[i] = 1
            new_lil_cuisine[i] = 'organic'
        elif lil_cuisine == 'Modern |Regional':
            modern[i] = 1
            modern_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'modern'
        elif lil_cuisine == 'Modern |Regional|Fish and seafood':
            modern[i] = 1
            modern_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'
        elif lil_cuisine == 'Modern |Scandinavian':
            modern[i] = 1
            modern_gen[i] = 1
            scandinavian_gen[i] = 1
            scandinavian[i] = 1
            new_lil_cuisine[i] = 'scandinavian'
        elif lil_cuisine == 'Modern |Traditional':
            modern[i] = 1
            modern_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'modern'

        elif lil_cuisine == 'Moroccan':
            african_gen[i] = 1
            moroccan[i] = 1
            new_lil_cuisine[i] = 'african'

        elif lil_cuisine == 'M\xc3\xa9diterran\xc3\xa9enne':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'M\xc3\xa9diterran\xc3\xa9enne|Cr\xc3\xa9ative':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'M\xc3\xa9diterran\xc3\xa9enne|Terroir':
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            terroir[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'mediterranean'

        elif lil_cuisine == 'Nepali':
            nepali[i] = 1
            sub_asian[i] = 1
            new_lil_cuisine[i] = 'sub_asian'

        elif lil_cuisine == 'Noodles':
            noodles[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'street_food'
        elif lil_cuisine == 'Noodles and congee':
            noodles[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'street_food'

        elif lil_cuisine == 'Nord-am\xc3\xa9ricaine':
            american_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'american'

        elif lil_cuisine == 'North African':
            african_gen[i] = 1
            new_lil_cuisine[i] = 'african'
        elif lil_cuisine == 'North-African':
            african_gen[i] = 1
            new_lil_cuisine[i] = 'african'

        elif lil_cuisine == 'North-American':
            american_gen[i] = 1
            new_lil_cuisine[i] = 'american'

        elif lil_cuisine == 'Norwegian':
            norwegian[i] = 1
            scandinavian_gen[i] = 1
            new_lil_cuisine[i] = 'scandinavian'
        elif lil_cuisine == 'Norwegian|modern':
            norwegian[i] = 1
            scandinavian_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'scandinavian'

        elif lil_cuisine == 'Organic':
            organic[i] = 1
            new_lil_cuisine[i] = 'organic'
        elif lil_cuisine == 'Organic|Creative':
            organic[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'organic'
        elif lil_cuisine == 'Organic|Regional|Modern':
            organic[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'organic'
        elif lil_cuisine == 'Organic|Vegetarian|Modern':
            organic[i] = 1
            vegetarian[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'organic'

        elif lil_cuisine == 'Pakistani':
            pakistani[i] = 1
            sub_asian[i] = 1
            new_lil_cuisine[i] = 'sub_asian'

        elif lil_cuisine == 'Pekingese':
            chinese_gen[i] = 1
            regional_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Persian':
            persian[i] = 1
            middle_eastern_gen[i] = 1
            new_lil_cuisine[i] = 'middle_eastern'

        elif lil_cuisine == 'Peruvian':
            peruvian[i] = 1
            latin_american_gen[i] = 1
            new_lil_cuisine[i] = 'latin_american'

        ## PIEMONTESE
        elif lil_cuisine == 'Piedmontese':
            piedmontese[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Piedmontese|Classic':
            piedmontese[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Piedmontese|Creative':
            piedmontese[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Piedmontese|Fish and seafood':
            piedmontese[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Piedmontese|Modern':
            piedmontese[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Piedmontese|Regional':
            piedmontese[i] = 1
            italian_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Pi\xc3\xa9montaise':
            en_francais[i] = 1
            piedmontese[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Pi\xc3\xa9montaise|R\xc3\xa9gionale':
            en_francais[i] = 1
            piedmontese[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Pizza':
            pizza[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Poissons et fruits de mer':
            fish_seafood[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'
        elif lil_cuisine == 'Poissons et fruits de mer| moderne':
            fish_seafood[i] = 1
            en_francais[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'

        elif lil_cuisine == 'Polish':
            eastern_european_gen[i] = 1
            polish[i] = 1
            new_lil_cuisine[i] = 'eastern_european'
        elif lil_cuisine == 'polonaise':
            eastern_european_gen[i] = 1
            polish[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'eastern_european'

        elif lil_cuisine == 'Portugaise':
            portuguese[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'portuguese'
        elif lil_cuisine == 'Portuguese':
            portuguese[i] = 1
            new_lil_cuisine[i] = 'portuguese'

        elif lil_cuisine == 'Proven\xc3\xa7al':
            provencal[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Proven\xc3\xa7ale':
            provencal[i] = 1
            en_francais[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Proven\xc3\xa7al|Italian':
            provencal[i] = 1
            french_gen[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Proven\xc3\xa7al|Mediterranean|Regional':
            provencal[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            regional[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Proven\xc3\xa7al|Traditional':
            provencal[i] = 1
            french_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'


        elif lil_cuisine == 'Puerto Rican':
            puerto_rican[i] = 1
            new_lil_cuisine[i] = 'caribbean'

        elif lil_cuisine == 'P\xc3\xa9ruvienne':
            peruvian[i] = 1
            latin_american_gen[i] = 1
            new_lil_cuisine[i] = 'latin_american'

        elif lil_cuisine == 'Ramen':
            ramen[i] = 1
            asian_gen[i] = 1
            japanese_gen[i] = 1
            new_lil_cuisine[i] = 'street_food'

        elif lil_cuisine == 'Regional':
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'Regional| from the South West':
            regional[i] = 1
            regional_gen[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Regional| from the South West|Regional|Belgian':
            regional[i] = 1
            regional_gen[i] = 1
            french_gen[i] = 1
            belgian[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Regional|Asian':
            regional[i] = 1
            regional_gen[i] = 1
            asian[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'asian'
        elif lil_cuisine == 'Regional|Austrian':
            regional[i] = 1
            regional_gen[i] = 1
            austrian[i] = 1
            new_lil_cuisine[i] = 'austrian'
        elif lil_cuisine == 'Regional|Austrian|Swiss':
            regional[i] = 1
            regional_gen[i] = 1
            austrian[i] = 1
            swiss[i] = 1
            new_lil_cuisine[i] = 'austrian'
        elif lil_cuisine == 'Regional|Belgian':
            regional[i] = 1
            regional_gen[i] = 1
            belgian[i] = 1
            new_lil_cuisine[i] = 'belgian'
        elif lil_cuisine == 'Regional|Cheese, fondue and raclette|Traditional':
            cheese_fondue_raclette[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'cheese_fondue'
        elif lil_cuisine == 'Regional|Classic':
            regional[i] = 1
            regional_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'Regional|Classic |Creative':
            regional[i] = 1
            regional_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'Regional|Creative':
            regional[i] = 1
            regional_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'Regional|Emilian':
            regional[i] = 1
            regional_gen[i] = 1
            emilian[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Regional|Fish and seafood':
            regional[i] = 1
            regional_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'
        elif lil_cuisine == 'Regional|French':
            regional[i] = 1
            regional_gen[i] = 1
            french[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Regional|French classic':
            regional[i] = 1
            regional_gen[i] = 1
            french[i] = 1
            french_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Regional|International':
            regional[i] = 1
            regional_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'Regional|International|Swiss':
            regional[i] = 1
            regional_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            swiss[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Regional|International|Traditional':
            regional[i] = 1
            regional_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'Regional|Italian':
            regional[i] = 1
            regional_gen[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Regional|Lyonnaise':
            lyonnaise[i] = 1
            french_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Regional|Mantuan':
            mantuan[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Regional|Meats':
            regional[i] = 1
            regional_gen[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Regional|Mediterranean':
            regional[i] = 1
            regional_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Regional|Mediterranean|Asian':
            regional[i] = 1
            regional_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            asian[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Regional|Modern':
            regional[i] = 1
            regional_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'Regional|Piedmontese':
            piedmontese[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Regional|Swiss':
            swiss[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Regional|Traditional':
            regional[i] = 1
            regional_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'Regional|Traditional |Classic':
            regional[i] = 1
            regional_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'Regional|Tuscan':
            tuscan[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Regional|Venetian':
            venetian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Roman':
            lazio[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'du Lazio':
            lazio[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine in ['from Lazio', 'from Lazio|Regional']:
            lazio[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Russian':
            eastern_european_gen[i] = 1
            russian[i] = 1
            new_lil_cuisine[i] = 'eastern_european'

        elif lil_cuisine == 'R\xc3\xa9gionale':
            regional[i] = 1
            regional_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'R\xc3\xa9gionale| moderne':
            regional[i] = 1
            regional_gen[i] = 1
            en_francais[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'traditionnelle|R\xc3\xa9gionale':
            regional[i] = 1
            regional_gen[i] = 1
            en_francais[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'regional'
        elif lil_cuisine == 'R\xc3\xa9gionale|Ligurienne':
            ligurian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'R\xc3\xa9gionale|Pi\xc3\xa9montaise':
            piedmontese[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'R\xc3\xa9gionale|Toscane':
            tuscan[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            regional[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Sarde':
            sardinian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Sardinian':
            sardinian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Savoyard':
            savoyard[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'Scandinavian':
            scandinavian[i] = 1
            scandinavian_gen[i] = 1
            new_lil_cuisine[i] = 'scandinavian'
        elif lil_cuisine == 'scandinave':
            scandinavian[i] = 1
            scandinavian_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'scandinavian'

        elif lil_cuisine == 'Seafood':
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'

        elif lil_cuisine == 'Shaanxi':
            chinese_gen[i] = 1
            asian_gen[i] = 1
            regional_gen[i] = 1
            shaanxi[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Shanghainese':
            shanghainese[i] = 1
            chinese_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Shun Tak':
            cantonese[i] = 1
            chinese_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Sichuan':
            sichuan[i] = 1
            chinese_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'Sicilian':
            sicilian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Sicilian|Fish and seafood':
            sicilian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Sicilian|Italian':
            sicilian[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Sicilian|Modern':
            sicilian[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Sicilienne':
            sicilian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Sicilienne| moderne':
            sicilian[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            italian_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Singaporean':
            singaporean[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'
        elif lil_cuisine == 'Singaporean and Malaysian':
            singaporean[i] = 1
            asian_gen[i] = 1
            regional_gen[i] = 1
            malaysian[i] = 1
            new_lil_cuisine[i] = 'SE_asian'

        elif lil_cuisine == 'South African':
            african_gen[i] = 1
            south_african[i] = 1
            new_lil_cuisine[i] = 'african'

        elif lil_cuisine == 'South-East Asian':
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'
        elif lil_cuisine == 'sud-est asiatique':
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'

        elif lil_cuisine == 'South-indian':
            indian[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'sub_asian'

        elif lil_cuisine == 'Southern':
            american_gen[i] = 1
            southern_US[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'american'

        elif lil_cuisine == 'Southwestern':
            american_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'american'

        elif lil_cuisine == 'Spanish':
            spanish[i] = 1
            new_lil_cuisine[i] = 'spanish'
        elif lil_cuisine == 'Spanish|French classic':
            spanish[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'
        elif lil_cuisine == 'Spanish|Mediterranean':
            spanish[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'

        elif lil_cuisine == 'Sri Lankan':
            sri_lankan[i] = 1
            sub_asian_gen[i] = 1
            new_lil_cuisine[i] = 'sub_asian'

        elif lil_cuisine == 'Steakhouse':
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'

        elif lil_cuisine == 'Street Food':
            street_food[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'street_food'

        elif lil_cuisine == 'Suisse':
            swiss[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Suisse| moderne':
            swiss[i] = 1
            en_francais[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Suisse|M\xc3\xa9diterran\xc3\xa9enne|Internationale':
            swiss[i] = 1
            en_francais[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Suisse|Terroir':
            swiss[i] = 1
            terroir[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Suisse|Viandes':
            swiss[i] = 1
            meats[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'traditionnelle|Suisse':
            swiss[i] = 1
            en_francais[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'

        elif lil_cuisine in ['Sushi', 'sushi']:
            sushi[i] = 1
            japanese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Sushi|Indian|Teppanyaki|Thai|Japanese':
            sushi[i] = 1
            indian[i] = 1
            teppanyaki[i] = 1
            japanese[i] = 1
            japanese_gen[i] = 1
            thai[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Sushi|Japanese':
            sushi[i] = 1
            japanese[i] = 1
            japanese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'

        elif lil_cuisine == 'Swedish':
            swedish[i] = 1
            scandinavian_gen[i] = 1
            new_lil_cuisine[i] = 'scandinavian'
        elif lil_cuisine == 'Swedish|modern':
            swedish[i] = 1
            scandinavian_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'scandinavian'
        elif lil_cuisine == 'su\xc3\xa9doise':
            swedish[i] = 1
            scandinavian_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'scandinavian'

        elif lil_cuisine == 'Swiss':
            swiss[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Swiss|Cheese, fondue and raclette':
            cheese_fondue_raclette[i] = 1
            swiss[i] = 1
            new_lil_cuisine[i] = 'cheese_fondue'
        elif lil_cuisine == 'Swiss|Classic':
            swiss[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Swiss|Creative':
            swiss[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Swiss|International':
            swiss[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Swiss|Mediterranean':
            swiss[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Swiss|Modern':
            swiss[i] == 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Swiss|Regional':
            swiss[i] == 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Swiss|Traditional':
            swiss[i] == 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'

        elif lil_cuisine == 'Tempura':
            tempura[i] = 1
            japanese_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'

        elif lil_cuisine == 'Teppanyaki':
            teppanyaki[i] = 1
            japanese_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'
        elif lil_cuisine == 'Teppanyaki|Japanese':
            teppanyaki[i] = 1
            japanese[i] = 1
            japanese_gen[i] = 1
            new_lil_cuisine[i] = 'japanese'

        elif lil_cuisine == 'Terroir':
            terroir[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'terroir'
        elif lil_cuisine in ['Terroir| moderne', 'moderne|Terroir']:
            terroir[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'terroir'
        elif lil_cuisine in ['Terroir| traditionnelle', 'traditionnelle|Terroir']:
            terroir[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'terroir'
        elif lil_cuisine == 'Terroir|Fran\xc3\xa7aise':
            terroir[i] = 1
            french[i] = 1
            french_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Terroir|Internationale':
            terroir[i] = 1
            international[i] = 1
            international_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'terroir'
        elif lil_cuisine == 'Terroir|Suisse| traditionnelle':
            terroir[i] = 1
            swiss[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'bourgeoise|Terroir':
            terroir[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'terroir'
        elif lil_cuisine == 'moderne|Terroir|Internationale':
            terroir[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            en_francais[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'terroir'
        elif lil_cuisine == 'r\xc3\xa9gionale et terroir':
            regional_gen[i] = 1
            terroir[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'terroir'

        elif lil_cuisine == 'Thai':
            thai[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'
        elif lil_cuisine == 'Thai|Asian':
            thai[i] = 1
            asian[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'
        elif lil_cuisine == 'Thai|Mediterranean|Barbecued':
            thai[i] = 1
            mediterranean[i] = 1
            asian_gen[i] = 1
            mediterranean_gen[i] = 1
            bbq[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'
        elif lil_cuisine == 'Thai|Traditional':
            thai[i] = 1
            asian_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'
        elif lil_cuisine == 'Tha\xc3\xaflandaise':
            thai[i] = 1
            asian_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'SE_asian'

        elif lil_cuisine == 'Tibetan':
            tibetan[i] = 1
            sub_asian_gen[i] = 1
            new_lil_cuisine[i] = 'sub_asian'

        ## TRADITIONAL
        elif lil_cuisine == 'Traditional':
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'traditional'
        elif lil_cuisine == 'traditionnelle':
            traditional[i] = 1
            traditional_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'traditional'
        elif lil_cuisine == 'Traditional | from Auvergne':
            traditional[i] = 1
            traditional_gen[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Traditional | from The Marches':
            traditional[i] = 1
            traditional_gen[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Traditional |Alsatian':
            alsatian[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Traditional |Asian influences':
            traditional[i] = 1
            traditional_gen[i] = 1
            asian_infl[i] = 1
            new_lil_cuisine[i] = 'traditional'
        elif lil_cuisine == 'Traditional |Austrian':
            austrian[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'austrian'
        elif lil_cuisine == 'Traditional |Belgian':
            belgian[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'belgian'
        elif lil_cuisine == 'Traditional |Belgian|Classic':
            belgian[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'belgian'
        elif lil_cuisine == 'Traditional |Burgundian':
            burgundian[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Traditional |Catalan':
            catalan[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'
        elif lil_cuisine == 'Traditional |Classic':
            traditional[i] = 1
            traditional_gen[i] = 1
            classic[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'traditional'
        elif lil_cuisine == 'Traditional |Corsican':
            corsican[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            french_gen[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Traditional |Corsican|Fish and seafood':
            corsican[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            french_gen[i] = 1
            mediterranean_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Traditional |Creative':
            traditional[i] = 1
            traditional_gen[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'traditional'
        elif lil_cuisine == 'Traditional |Fish and seafood':
            traditional[i] = 1
            traditional_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'fish_seafood'
        elif lil_cuisine == 'Traditional |French':
            traditional[i] = 1
            traditional_gen[i] = 1
            french[i] = 1
            french_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'traditionnelle|Fran\xc3\xa7aise':
            traditional[i] = 1
            traditional_gen[i] = 1
            french[i] = 1
            french_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Traditional |French classic':
            traditional[i] = 1
            traditional_gen[i] = 1
            french_gen[i] = 1
            classic_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Traditional |French creative':
            traditional[i] = 1
            traditional_gen[i] = 1
            french_gen[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Traditional |French modern':
            traditional[i] = 1
            traditional_gen[i] = 1
            french_gen[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Traditional |Galician':
            galician[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'spanish'
        elif lil_cuisine == 'Traditional |Home cooking':
            traditional[i] = 1
            traditional_gen[i] = 1
            home_cooking[i] = 1
            new_lil_cuisine[i] = 'home_cooking'
        elif lil_cuisine == 'Traditional |International':
            traditional[i] = 1
            traditional_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'Traditional |International|Mediterranean':
            traditional[i] = 1
            traditional_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Traditional |International|Regional':
            traditional[i] = 1
            traditional_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'Traditional |Meats':
            traditional[i] = 1
            traditional_gen[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Traditional |Mediterranean':
            traditional[i] = 1
            traditional_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Traditional |Modern':
            traditional[i] = 1
            traditional_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'modern'
        elif lil_cuisine == 'Traditional |Regional':
            traditional[i] = 1
            traditional_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'traditional'
        elif lil_cuisine == 'Traditional |Regional|International':
            traditional[i] = 1
            traditional_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'international'
        elif lil_cuisine == 'Traditional |Regional|Meats':
            traditional[i] = 1
            traditional_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Traditional |Regional|Mediterranean':
            traditional[i] = 1
            traditional_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            mediterranean[i] = 1
            mediterranean_gen[i] = 1
            new_lil_cuisine[i] = 'mediterranean'
        elif lil_cuisine == 'Traditional |Savoyard':
            savoyard[i] = 1
            french_gen[i] = 1
            regional_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'Traditional |Sushi':
            traditional[i] = 1
            traditional_gen[i] = 1
            sushi[i] = 1
            japanese_gen[i] = 1
            new_lil_cuisine[i] = 'traditional'
        elif lil_cuisine == 'Traditional |Swiss':
            traditional[i] = 1
            traditional_gen[i] = 1
            swiss[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Traditional |Swiss|Creative':
            traditional[i] = 1
            traditional_gen[i] = 1
            swiss[i] = 1
            creative[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Traditional |Swiss|International':
            traditional[i] = 1
            traditional_gen[i] = 1
            swiss[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'swiss'
        elif lil_cuisine == 'Traditional|international':
            traditional[i] = 1
            traditional_gen[i] = 1
            international[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'international'

        elif lil_cuisine == 'Turkish':
            turkish[i] = 1
            middle_eastern_gen[i] = 1
            new_lil_cuisine[i] = 'middle_eastern'

        elif lil_cuisine == 'Toscane':
            en_francais[i] = 1
            tuscan[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Tuscan':
            tuscan[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Tuscan|Modern':
            tuscan[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Tuscan|Sicilian|Fish and seafood':
            tuscan[i] = 1
            sicilian[i] = 1
            italian_gen[i] = 1
            fish_seafood[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Tuscan|Tuscan':
            tuscan[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Vegan':
            vegetarian[i] = 1
            new_lil_cuisine[i] = 'vegetarian_vegan'

        elif lil_cuisine == 'Vegetarian':
            vegetarian[i] = 1
            new_lil_cuisine[i] = 'vegetarian_vegan'
        elif lil_cuisine == 'V\xc3\xa9g\xc3\xa9tarienne':
            vegetarian[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'vegetarian_vegan'

        elif lil_cuisine == 'Venetian':
            venetian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'Venetian|Italian':
            venetian[i] = 1
            italian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'
        elif lil_cuisine == 'V\xc3\xa9nitienne':
            en_francais[i] = 1
            venetian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'Viandes':
            en_francais[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'Viandes|Sushi':
            en_francais[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            sushi[i] = 1
            japanese_gen[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'meats'
        elif lil_cuisine == 'traditionnelle|Viandes':
            en_francais[i] = 1
            meats[i] = 1
            meats_gen[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'meats'

        elif lil_cuisine == 'Vietnamese':
            vietnamese[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'
        elif lil_cuisine == 'Vietnamese|Asian':
            vietnamese[i] = 1
            asian[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'
        elif lil_cuisine == 'Vietnamienne':
            en_francais[i] = 1
            vietnamese[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'SE_asian'

        elif lil_cuisine in ['World', 'other world kitchens']:
            world[i] = 1
            international_gen[i] = 1
            new_lil_cuisine[i] = 'world'
        elif lil_cuisine == 'World |French creative':
            world[i] = 1
            international_gen[i] = 1
            french_gen[i] = 1
            creative_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'du monde':
            world[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'world'

        elif lil_cuisine == 'Xinjiang':
            chinese_gen[i] = 1
            xinjiang[i] = 1
            asian_gen[i] = 1
            new_lil_cuisine[i] = 'chinese'

        elif lil_cuisine == 'du Sud-Ouest':
            french_gen[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'du Sud-Ouest|Terroir':
            french_gen[i] = 1
            en_francais[i] = 1
            terroir[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'du march\xc3\xa9':
            market[i] = 1
            en_francais[i] = 1
            new_lil_cuisine[i] = 'market'
        elif lil_cuisine == 'du march\xc3\xa9| moderne':
            market[i] = 1
            en_francais[i] = 1
            modern[i] = 1
            modern_gen[i] = 1
            new_lil_cuisine[i] = 'market'

        elif lil_cuisine == 'from Abruzzo':
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'from Alentejo':
            portuguese[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'portuguese'

        elif lil_cuisine == 'from Aveyron':
            french_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'
        elif lil_cuisine == 'traditionnelle|Aveyronnaise':
            french_gen[i] = 1
            regional_gen[i] = 1
            en_francais[i] = 1
            traditional[i] = 1
            traditional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'from The Marches':
            marches[i] = 1
            regional_gen[i] = 1
            italian_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'from Valtellina':
            lombardian[i] = 1
            italian_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'italian'

        elif lil_cuisine == 'from the South West':
            french_gen[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'from the South West|Regional|Regional':
            french_gen[i] = 1
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'french'

        elif lil_cuisine == 'other world kitchens|Peruvian|Mexican|Brazilian':
            latin_american_gen[i] = 1
            new_lil_cuisine[i] = 'latin_american'

        elif lil_cuisine == 'regional/country':
            regional[i] = 1
            regional_gen[i] = 1
            new_lil_cuisine[i] = 'regional'




    df['new_cuisine'] = new_lil_cuisine

    return df
