import os

rachel_copy = "This is for Rachel you big fat white nasty smelling fat bitch why you took me off the motherfucking schedule " \
              "with your trifling dirty white racist ass you big fat bitch oompa loompa body ass bitch I'm coming outside and " \
              "I'm going to beat the fuck out of you bitch and don't even call the police today because I'm gonna come " \
              "unexpected and wait on yo motherfucking ass bitch I'm going to beat the fuck out of you bitch cause you did " \
              "that on purpose with your aundry racist white ass danhard bitch watch I'm coming bout to fuck you up bitch I'm " \
              "telling you watch I know what kind of car you drive I'm gonna wait on you and I'm gonna beat yo ass bitch cause " \
              "I'mma show you not to play with Jasmine's money bitch that's the first thing you did and you got me fucked up " \
              "cause bitch I told you what the fuck was going on you white motherfuckers hate to see black people doing good " \
              "or doing goodanything for their motherfucking selfs ugly fat white bitch watch I'm telling you I'm coming " \
              "outside beat yo motherfucking ass danhard smelly white dog smelling ass bitch watch I'll come and fuck you up " \
              "cause you got me fucked up we see you trynna do that old audnry ass shit bitch you aundry the first day I came " \
              "up there talking about a bitch who had pajamas but you walking around here wearing those 10$ ass jeans on dirty " \
              "dusty white bitch sitting up behind that counter smelling like cheese bitch stinky fat white ass bitch are you " \
              "gonna not try to answer this phone I'm coming to fuck you up I'm telling you you better remember who I am cause " \
              "bitch you gonna run when you see me cause I'm gonna fuck you up bitch you wanna sit here and play with me about " \
              "my motherfucking money wanna play about my motherfucking money bitch wanna sit up there and try to do that bitch " \
              "little do you know little do you know I know enough people watch I'm coming to fuck you up I promise you that I " \
              "promise you I'm coming to fuck you up you fat stinky white bitch danhard yellow yuck mouth nasty mouth ass bitch " \
              "you stink you smell like fucking cheese you got that trifiling ass attitude I'mma beat that attitude up out you " \
              "bitch watch you treat everybody like that all these black people that you do like that you in the wrong position " \
              "you trifling ass racist ass bitch that's why nobody fuck with you you trifling and you racist bitch should've " \
              "fine did all that shit when I told you what the fuck going on gonna tell me I worked at that motherfucking job " \
              "when I telling you the fuck I didn't bitch why the fuck would I lie about shit like that watch I finna come " \
              "outside and beat yo motherfucking ass you better not get out that motherfucking car bitch I'm telling you fucking bitch."

angry_copy = "You swine. You vulgar little maggot. You worthless bag of filth. I wager you couldn't empty a boot of " \
             "excrement were the instructions on the heel. You are a canker. A sore that won't go away. I would rather " \
             "kiss a lawyer than be seen with you. Try to edit your responses of unnecessary material before attempting " \
             "to impress us with your insight. The evidence that you are a nincompoop will still be available to readers, " \
             "but they will be able to access it more rapidly. You snail-skulled little rabbit. Would that a hawk pick" \
             " you up, drive its beak into your brain, and upon finding it rancid set you loose to fly briefly before" \
             " spattering the ocean rocks with the frothy pink shame of your ignoble blood. May you choke on the queasy, " \
             "convulsing nausea of your own trite, foolish beliefs. You are weary, stale, flat and unprofitable. You " \
             "are grimy, squalid, nasty and profane. You are foul and disgusting. You're a fool, an ignoramus. And what " \
             "meaning do you expect your delusional self-important statements of unknowing, inexperienced opinion to " \
             "have to us who think and reason? What fantasy do you hold that you would believe that your tiny-fisted " \
             "tantrums would have more weight than that of a leprous desert rat, spinning rabidly in a circle, waiting " \
             "for the bite of the snake? You are a waste of flesh. You have no rhythm. You are ridiculous and obnoxious. " \
             "You are the moral equivalent of a leech. You are a living emptiness, a meaningless void. You are sour and" \
             " senile. You are a disease, you puerile one-handed slack-jawed , drooling meatslapper. You smarmy lagerlout " \
             "git. You bloody woofter sod. Bugger off, pillock. You grotty wanking oik artless base-court apple-john. " \
             "You clouted boggish foot-licking twit. You dankish clack-dish plonker. You gormless crook-pated tosser. " \
             "You churlish boil-brained clotpole ponce. You cockered bum-bailey poofter. You gob-kissing gleeking " \
             "flap-mouthed coxcomb. You dread-bolted fobbing beef-witted clapper-clawed flirt-gill. You are a fiend and " \
             "a coward, and you have bad breath. You are degenerate, noxious and depraved. I feel debased just for " \
             "knowing you exist. I despise everything about you, and I wish you would go away. I cannot believe how " \
             "incredibly stupid you are. I mean rock-hard stupid. Dehydrated-rock-hard stupid. Stupid so stupid that it " \
             "goes way beyond the stupid we know into a whole different dimension of stupid. You are trans-stupid stupid. " \
             "Meta-stupid. Some pure essence of a stupid so uncontaminated by anything else as to be beyond the laws " \
             "of physics that we know. I'm sorry. I can't go on. This is an epiphany of stupid for me. After this, you" \
             " may not hear from me again for a while. I don't have enough strength left to deride your ignorant " \
             "questions and half-baked comments about unimportant trivia, or any of the rest of this drivel. Duh. I " \
             "mean, really, stringing together a bunch of insults among a load of babbling was hardly effective. True, " \
             "these are rudimentary skills that many of us normal people take for granted that everyone has an easy " \
             "time of mastering. But we sometimes forget that there are challenged persons in this world who find these " \
             "things more difficult. If I had known, that this was your case then I would have never read your post. " \
             "It just wouldn't have been right. Sort of like parking in a handicap space. I wish you the best of luck " \
             "in the emotional, and social struggles that seem to be placing such a demand on you. You're an idiot. " \
             "A moron of the highest order. You're so stupid it's a wonder and a pity you can remember to breath. " \
             "Intelligent ideas bounce off your head as if it were coated with teflon. Creative thoughts take alternate " \
             "transportation in order to avoid even being in the same state as you. If you had an original thought it" \
             " would die of loneliness before the hour was out. On an intelligence scale of 1 to 10 (10 corresponding " \
             "to the highest attainable IQ) you're rating is so far into negative numbers that one would need to travel " \
             "into another quantum reality in order to even catch a distant glimpse of it. Your personality is that of " \
             "a rabid Chihuahua intent on destroying its own tail. Your powers of observation are akin to those of the " \
             "bird that keeps slamming into the picture window trying to get that other bird it keeps seeing. You are" \
             " walking, talking proof that you don't have to be sentient to survive, and that Barnum was thinking of" \
             " you when he uttered his immortal phrase regarding the birth of a sucker. You are, at varying times," \
             " tedious, boring, and even occasionally earth shatteringly hilarious in your idiocy, routinely childish," \
             " moronic, pathetic, wretched, disgusting and pitiful. You are wholly without any redeeming social grace " \
             "or value. If God ever decides to give the planet an enema you'd better run like the wind because anywhere" \
             " you stand is a suitable place for The Insertion. There is no animal so disgusting, so vile that it deserves " \
             "comparison to you, for even the lowest, dirtiest, most parasitic member of the animal kingdom fills an " \
             "ecological niche. You fill no niche. To call you a parasite would be injurious and defamatory to the " \
             "thousands of honest parasitic species. You are worse than vermin, for vermin do not pretend to be what " \
             "it is not. You are truly human garbage. You are a fraudulent, lying, predatory charlatan. You are of " \
             "less worth than a burnt-out light bulb. You will forever live in shame. You have nothing to say, and " \
             "Godwin's Law does not apply when writing about you. You are the anti-Midas, for all that you touch becomes " \
             "valueless and unusable. Mothers gather their children close when you appear. You are an aberration, a" \
             " corruption, and a boil that needs to be lanced. You are a poison in need of being vomited. You are a " \
             "tooth so rotten it infects the whole body. You are sperm that should have been captured in a condom and" \
             " flushed down a toilet. I don't like you. I don't like anybody who has as little respect for others as " \
             "you do. Go away, you swine. You're a putrescent mass, a walking vomit. You are a spineless little worm " \
             "deserving nothing but the profoundest contempt. You are a jerk, a cad, and a weasel. Your life is a " \
             "monument to stupidity. You are a stench, a revulsion, a big suck on a sour lemon. You are a curdled " \
             "staggering mutant dwarf smeared richly with the effluvia and offal accompanying your alleged birth into " \
             "this world. Meaningful to no one, abandoned by the puke-drooling, giggling beasts that sired you and " \
             "then killed themselves in recognition of what they had done. I will never get over the embarrassment of" \
             " belonging to the same species as you. You are a monster, an ogre, a malformity. I wretch at the very " \
             "thought of you. You have all the appeal of a paper cut. Lepers avoid you. You are vile, worthless, less " \
             "than nothing. You are a weed, a fungus, and the dregs of this earth. And did I mention you smell? Monkeys" \
             " look down on you. Even sheep won't have sex with you. You are unreservedly pathetic, starved for attention," \
             " and lost in a land that reality forgot. You are a waste of flesh. On a good day you're a halfwit. " \
             "You are deficient in all that lends character. You have the personality of wallpaper. You are dank and " \
             "filthy. You are asinine and benighted. You are the source of all unpleasantness. You spread misery and " \
             "sorrow wherever you go. You are a fiend and a coward, and you have bad breath. You are degenerate, " \
             "noxious and depraved. I feel debased just for knowing you exist. I despise everything about you, and " \
             "I wish you would go away. I cannot believe how incredibly stupid you are. The only thing worse than your" \
             " logic is your manners. Maybe later in life, after you have learned to read, write, study, spell, and " \
             "count, you will have more success. True, these are rudimentary skills that many of us normal people take" \
             " for granted that everyone has an easy time of mastering. It just wouldn't have been right Sort of like" \
             " parking in a handicap space. I wish you the best of luck in the emotional, and social struggles that " \
             "seem to be placing such a demand on you. You are hypocritical, greedy, violent, malevolent, vengeful, " \
             "cowardly, deadly, mendacious, meretricious, loathsome, despicable, belligerent, opportunistic, barratrous," \
             " contemptible, criminal, fascistic, bigoted, racist, sexist, avaricious, tasteless, idiotic, brain-damaged," \
             " imbecilic, insane, arrogant, deceitful, demented, lame, self-righteous, byzantine, conspiratorial, " \
             "satanic, fraudulent, libellous, bilious, splenetic, spastic, ignorant, clueless, illegitimate, harmful, " \
             "destructive, dumb, evasive, double-talking, devious, revisionist, narrow, manipulative, paternalistic, " \
             "fundamentalist, dogmatic, idolatrous, unethical, cultic, diseased, suppressive, controlling, restrictive, " \
             "malignant, deceptive, dim, crazy, weird, dystrophic, stifling, uncaring, plantigrade, grim, unsympathetic, " \
             "jargon-spouting, censorious, secretive, aggressive, mind-numbing, abrasive, poisonous, flagrant, " \
             "self-destructive, abusive, and socially-inept. Shut up and go away lest you achieve the physical retribution " \
             "your behaviour merits. Thank you for your kind attention to and expected cooperation in this matter."

me = "6145627043"
karen = "7812668787"
nick = "7179514334"
zoya = "6038181843"
john = "4018548454"
remmi = "7165836164"
lindsay = "2039743443"
tristen = "9084997937"
angela = "6143615329"
rachel = "5164298600"
jay = "4438788384"
mara = "5082442631"
tormey = "6178772796"
shabach = "6147532030"
logan = "4196194171"
hannah = "9258994971"
denes = "denes.tatar@hotmail.com"


def get_command(word):
    cmd = """osascript<<END

    tell application "Messages"

    send "~" to buddy "7165836164" of (service 1 whose service type is iMessage)

    end tell

    END"""

    return cmd.replace("~", word)


def send_this_is_for_rachel():
    words_sent = 0
    split_array = rachel_copy.split(" ")
    for i in split_array:
        os.system(get_command(i))
    print(words_sent, "words sent")

def send_angry_copy_pasta():
    words_sent = 0
    split_array = angry_copy.split(" ")
    for i in split_array:
        os.system(get_command(i))
        words_sent += 1
    print(words_sent, "words sent")

send_angry_copy_pasta()