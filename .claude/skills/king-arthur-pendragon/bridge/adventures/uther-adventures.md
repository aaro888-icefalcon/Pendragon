# Ingested Adventure — Uther Period Adventures (Book of Uther, 480–495)   (hook: adventure-ingest; pure sandbox)
fidelity: light

Source module: `campaign/uther/06-adventures.md` — runnable scenario briefs for the named Book of Uther scenarios. One cluster per authored adventure; fragments are the authored scene beats only (no invented content).

## Clusters (authored scenes/nodes) → each with a scene description + member fragments

### cluster: menevia-480 — "Battle of Menevia"   (source: 06-adventures.md § Battle of Menevia, 480)
scene: Uther musters Logres' forces to break King Paschent's Irish invasion of Wales near Menevia, and the player-knights are called to the banner for a pitched battle that ends in Decisive British Victory.
threads: [Break Paschent's Irish invasion]   characters: [Uther, Gillomanius]   elements: [Menevia / St David's, Logres–Wales border]   themes: [Action]
gate: none
fragments:
  - plot_point: "Muster at the border; Uther presents the battle plan."   themes: [Social]   weight: 1
  - plot_point: "The pitched battle itself (9 rounds, Large)."   themes: [Action]   weight: 1
  - plot_point: "Pursuit of Irish survivors; personal combat vs. Irish champions for individual glory."   themes: [Action]   weight: 1

### cluster: salisbury-480 — "Battle of Salisbury"   (source: 06-adventures.md § Battle of Salisbury, 480)
scene: The Saxons threaten Logres proper and the player-knights ride with Aurelius' army; Aurelius is pale and feverish from a Saxon spy's poison, collapses and dies mid-battle, and Gorlois must rally the knights to turn defeat into victory, after which Uther is crowned.
threads: [Defeat the Saxons at Salisbury, Uncover the Saxon poison-spy]   characters: [Aurelius, Aesc of Kent, Gorlois]   elements: [Sarum / Salisbury]   themes: [Tension]
gate: none
fragments:
  - plot_point: "Pre-battle: Aurelius is pale and feverish; knights may investigate the Saxon spy (Intrigue or Awareness)."   themes: [Mystery]   weight: 1
  - plot_point: "Battle opens — Aurelius (Battle 16) vs. Aesc (Battle 18)."   themes: [Action]   weight: 1
  - plot_point: "Round 6: Aurelius collapses and dies of the poison; the army risks routing."   themes: [Tension]   weight: 1
  - plot_point: "Gorlois (Battle 21) takes command, rallies the knights, and turns the battle."   themes: [Action]   weight: 1
  - plot_point: "Aftermath: Saxon defeat, Aurelius mourned, Uther crowned."   themes: [Social]   weight: 1

### cluster: bedegraine-481 — "Battle of Bedegraine"   (source: 06-adventures.md § Battle of Bedegraine, 481)
scene: Uther declares Bedegraine must swear homage; when its king refuses to submit, the royal army fights a small battle and Uther personally slays the King of Bedegraine in single combat, absorbing the county into Logres.
threads: [Compel Bedegraine's homage]   characters: [Uther, King of Bedegraine]   elements: [Bedegraine County, Oakmeet lead and silver mines]   themes: [Action]
gate: none
fragments:
  - plot_point: "March to Bedegraine; its king refuses to submit."   themes: [Tension]   weight: 1
  - plot_point: "The battle (3 rounds, Small)."   themes: [Action]   weight: 1
  - plot_point: "Uther personally slays the King of Bedegraine in single combat."   themes: [Action]   weight: 1
  - plot_point: "Occupation and sheriff appointment; distinguished knights may garrison Bedegraine."   themes: [Social]   weight: 1

### cluster: eburacum-484 — "Battle of Eburacum (Ambush)"   (source: 06-adventures.md § Battle of Eburacum, 484)
scene: Uther marches north to relieve Malahaut from Saxon pressure and walks into a Saxon ambush; the British suffer a Decisive Defeat and the player-knights must fight a rearguard to prevent total annihilation while Uther plans a night counterattack.
threads: [Survive the Eburacum disaster, Relieve Malahaut]   characters: [Uther, Octa, Eosa]   elements: [Eburacum / York, Malahaut, Linden]   themes: [Tension]
gate: none
fragments:
  - plot_point: "March through Linden and Malahaut territory."   themes: [Action]   weight: 1
  - plot_point: "The trap springs: Saxon ambush (British -10 round 1)."   themes: [Tension]   weight: 1
  - plot_point: "The battle (6 rounds, Large; Decisive British Defeat)."   themes: [Action]   weight: 1
  - plot_point: "Retreat: player-knights fight the rearguard to prevent annihilation (significant glory)."   themes: [Action]   weight: 1
  - plot_point: "Night: Uther plans the Mt. Damen counterattack."   themes: [Social]   weight: 1

### cluster: mt-damen-484 — "Battle of Mt. Damen (Night Attack)"   (source: 06-adventures.md § Battle of Mt. Damen, 484)
scene: After the Eburacum disaster, Uther rallies survivors for a desperate volunteers-only night raid on the Saxon camp; moving silently, the British achieve surprise and a Decisive Victory, restoring the army's morale.
threads: [Restore the army's morale by night raid]   characters: [Uther, Octa, Eosa, Saxon Veteran Axemen]   elements: [Mt. Damen, Saxon camp]   themes: [Action]
gate: [follows eburacum-484]
fragments:
  - plot_point: "Uther's midnight plan: volunteers only, move silently."   themes: [Tension]   weight: 1
  - plot_point: "Night approach (Stealth rolls; sentries handled quietly)."   themes: [Tension]   weight: 1
  - plot_point: "The attack (3 rounds, Medium; British surprise bonus)."   themes: [Action]   weight: 1
  - plot_point: "Saxon camp in chaos; target Octa or Eosa, the battle standards, or a chieftain for major glory."   themes: [Action]   weight: 1

### cluster: water-leapers-488 — "Adventure of Water Leapers"   (source: 06-adventures.md § Adventure of Water Leapers, 488)
scene: Reports reach court of a nest of "water leapers" attacking travelers and fishermen near a river or lake in Logres, and Uther assigns the knights to hunt and destroy the nest.
threads: [Destroy the water-leaper nest]   characters: [Water Leapers]   elements: [river / wetland in Logres, Lonazep's fens, the nest]   themes: [Action]
gate: none
fragments:
  - plot_point: "Investigation: locals report attacks; find the lair (Awareness, Hunting, Folklore)."   themes: [Mystery]   weight: 1
  - plot_point: "Approach: water leapers attack when crossing water or nearing the nest."   themes: [Tension]   weight: 1
  - plot_point: "The nest: multiple water leapers (1d6+2); combat in or near water."   themes: [Action]   weight: 1

### cluster: lindsey-embassy-487 — "Lindsey Embassy"   (source: 06-adventures.md § Lindsey Embassy, 487)
scene: Uther visits Duke Corneus at Linden Pool Castle with the player-knights as escort; the climax is Uther drawing Excalibur in the great hall, shaking the wary duke into renewing his oath, with Malahaut envoys arriving to press the Centurion King's request for aid.
threads: [Secure Corneus' renewed loyalty]   characters: [Duke Corneus, Centurion King's envoys]   elements: [Linden Pool Castle / Lincoln, Excalibur]   themes: [Social]
gate: none
fragments:
  - plot_point: "The Progress: travel north through baronial lands with hospitality at each stop."   themes: [Social]   weight: 1
  - plot_point: "Arrival at Linden Pool: assess the Duke's mood (Intrigue)."   themes: [Tension]   weight: 1
  - plot_point: "The Revelation: Uther draws Excalibur; Corneus is shaken and renews his oath."   themes: [Tension]   weight: 1
  - plot_point: "Optional: Malahaut envoys arrive; knights overhear tense talks of the Centurion King's request for aid."   themes: [Mystery]   weight: 1

### cluster: princes-passion-483 — "The Prince's Passion"   (source: 06-adventures.md § The Prince's Passion, 483)
scene: Prince Madoc is entangled in a love affair with a lady promised to another and connected to one of Uther's baronial rivals, and he asks the player-knights to help manage the situation discreetly before it becomes a political incident.
threads: [Manage Madoc's secret affair]   characters: [Prince Madoc, The Lady, Her Father (a baron)]   elements: [Court (current location)]   themes: [Social]
gate: none
fragments:
  - plot_point: "Madoc approaches the knights privately and explains the situation."   themes: [Personal]   weight: 1
  - plot_point: "Knights must facilitate the affair, discourage it, or manage its discovery."   themes: [Social]   weight: 1
  - plot_point: "The father discovers the liaison; confrontation at court."   themes: [Tension]   weight: 1
  - plot_point: "Resolution: legal, violent, or diplomatic."   themes: [Tension]   weight: 1

### cluster: summerland-482 — "Invasion of Summerland (Alternate 482)"   (source: 06-adventures.md § Invasion of Summerland, 482*)
scene: Uther decides Summerland must submit to Logres more formally and the player-knights ride into its deeply magical terrain, where Cadwy refuses to fight yet refuses to fully submit, until an advisor brokers the special agreement.
threads: [Force Summerland's submission]   characters: [Cadwy, Merlin, Gwion the Abbot]   elements: [Glamour Forest, Lake of Diana, Glastonbury Abbey]   themes: [Mystery]
gate: none
fragments:
  - plot_point: "Advance into Summerland's strange terrain (Glamour Forest, Lake of Diana)."   themes: [Mystery]   weight: 1
  - plot_point: "Faerie encounters in deeply magical Summerland."   themes: [Mystery]   weight: 1
  - plot_point: "Confrontation with Cadwy, who refuses to fight but also refuses to fully submit."   themes: [Social]   weight: 1
  - plot_point: "Merlin or another advisor brokers the special agreement (annual gift; mutual non-aggression)."   themes: [Social]   weight: 1

### cluster: excaliburs-peace-489 — "Excalibur's Peace (489 Political Crisis)"   (source: 06-adventures.md § Excalibur's Peace, 489)
scene: Uther calls his banners against Cornwall but the muster is murky and understrength; Merlin arrives, publicly displays Excalibur, and brokers a peace that turns the two armies into one combined force marching north against the Saxons.
threads: [Resolve the Cornwall crisis, Discern Merlin's hidden purpose]   characters: [Merlin, Gorlois]   elements: [road Logres→Cornwall, Excalibur, northern campaign]   themes: [Mystery]
gate: none
fragments:
  - plot_point: "Muster: few barons send full levies (Intrigue to understand why)."   themes: [Mystery]   weight: 1
  - plot_point: "Advance toward Cornwall; Gorlois sends envoys to negotiate."   themes: [Social]   weight: 1
  - plot_point: "Merlin intervenes; the public display of Excalibur."   themes: [Tension]   weight: 1
  - plot_point: "The two armies camp together; knights interact with Cornish knights."   themes: [Social]   weight: 1
  - plot_point: "United march north against the Saxons; the crisis is over for now (subsequent skirmishing glory)."   themes: [Action]   weight: 1

### cluster: linden-pool-490 — "Battle of Linden Pool"   (source: 06-adventures.md § Battle of Linden Pool, 490)
scene: Octa and Eosa march south bypassing Malahaut, Uther musters, and the combined British army wins its biggest victory — capturing both Saxon leaders — after which the Victory Feast at Linden Pool Castle reveals something changing in Uther as Ygraine attends.
threads: [Defeat and capture Octa and Eosa]   characters: [Octa, Eosa, Gorlois, Sir Bellias, Ygraine, Uther]   elements: [Linden Pool / Lincoln, Linden Pool Castle, Victory Feast]   themes: [Action]
gate: none
fragments:
  - plot_point: "Intelligence: scouts report two Saxon armies converging on Linden Pool."   themes: [Mystery]   weight: 1
  - plot_point: "Positioning: Uther and Gorlois discuss strategy (Gorlois' Battle 21 crucial)."   themes: [Social]   weight: 1
  - plot_point: "The battle (treat as Large, 8–10 rounds)."   themes: [Action]   weight: 1
  - plot_point: "Pursuit: Octa and Eosa caught and taken prisoner; Sir Bellias killed."   themes: [Action]   weight: 1
  - plot_point: "Victory Feast: Uther's obsession with Ygraine is visible; knights may notice Gorlois noticing (Intrigue)."   themes: [Tension]   weight: 1

### cluster: tintagel-491 — "The Tintagel Campaign"   (source: 06-adventures.md § The Tintagel Campaign, 491)
scene: War against Cornwall is declared and the player-knights besiege Castle Terrabil, which cannot be taken; Uther's desperation, a false retreat, and Merlin's magic lure Gorlois into a fatal night sortie, and by dawn Gorlois is dead and Tintagel surrenders as Ygraine emerges with the news.
threads: [Take Cornwall / win at Terrabil, Witness Merlin's bargain]   characters: [Gorlois, Prince Madoc, Sir Goreau, Merlin, Uther, Ygraine]   elements: [Castle Terrabil / Bossiney, Tintagel Castle]   themes: [Tension]
gate: none
fragments:
  - plot_point: "The siege: Terrabil cannot be taken; the army ravages the countryside; frustration builds."   themes: [Tension]   weight: 1
  - plot_point: "Uther's desperation: he meets privately with Merlin; knights may notice something strange."   themes: [Mystery]   weight: 1
  - plot_point: "The withdrawal: Uther orders a false retreat; knights are confused."   themes: [Mystery]   weight: 1
  - plot_point: "The sortie: Gorlois rides out from Terrabil (Merlin's magic); combat in the dark."   themes: [Action]   weight: 1
  - plot_point: "Dawn: Gorlois (and Madoc, Goreau) are dead; Tintagel surrenders; Ygraine brings the news."   themes: [Tension]   weight: 1
  - plot_point: "Winter garrison: knights winter at Terrabil among hostile locals (a 'man who looked like Gorlois' mystery)."   themes: [Mystery]   weight: 1

### cluster: helping-merlin-492 — "Helping Merlin (Treason)"   (source: 06-adventures.md § Helping Merlin, 492)
scene: Merlin urgently asks the player-knights to delay some riders without explaining why; the riders turn out to be Uther's household knights carrying the infant Arthur, and after Merlin vanishes with the baby the knights are named as conspirators and face a treason trial.
threads: [Help Merlin / survive the treason charge, Learn that Arthur exists]   characters: [Merlin, Uther's household knights, Count Roderick, Baby Arthur]   elements: [near Tintagel / Londinium, King's Bench]   themes: [Tension]
gate: none
fragments:
  - plot_point: "Merlin's approach: friendly and urgent; asks the knights to intercept and delay riders for an hour."   themes: [Mystery]   weight: 1
  - plot_point: "The intercept: the riders are Uther's household knights carrying the baby Arthur."   themes: [Tension]   weight: 1
  - plot_point: "The confrontation: Uther's men demand the knights stand aside; Merlin is already gone."   themes: [Tension]   weight: 1
  - plot_point: "The chase: Uther's men reach Merlin's spot — nothing; the baby is gone."   themes: [Mystery]   weight: 1
  - plot_point: "The accusation: the knights are named as conspirators."   themes: [Social]   weight: 1
  - plot_point: "Treason Trial: King's Bench convenes; Roderick defends them; Merlin outlawed; acquittal, amercement, or conviction."   themes: [Social]   weight: 1

### cluster: questing-beast-492 — "Adventure of the Questing Beast"   (source: 06-adventures.md § Adventure of the Questing Beast, 492)
scene: Traveling or hunting, the player-knights cross paths with the Glatisant — a creature baying like thirty hounds, with a serpent's head, leopard's body, and lion's hindquarters — pursued by the exhausted King Pellinore, who has given up his kingdom to hunt it.
threads: [Encounter Pellinore and the Glatisant, Learn of Norgales' chaos]   characters: [King Pellinore, The Glatisant / Questing Beast, Lamorak]   elements: [rural Logres, Norgales border]   themes: [Mystery]
gate: none
fragments:
  - plot_point: "The creature crosses their path; it is not threatening them; it is running from something."   themes: [Mystery]   weight: 1
  - plot_point: "King Pellinore arrives exhausted and focused entirely on the beast, barely acknowledging the knights."   themes: [Social]   weight: 1
  - plot_point: "Conversation: Pellinore explains he gave up his kingdom and ignores his son Lamorak's misrule of Norgales."   themes: [Personal]   weight: 1
  - plot_point: "Optional: the Beast pauses; the knights must decide — interfere, follow, or let it go."   themes: [Tension]   weight: 1

### cluster: argan-scandal-493 — "The Argan Scandal (Court Adventure)"   (source: 06-adventures.md § The Argan Scandal, 493)
scene: At Easter Court, Constable Sir Argan ap Maelgad — having already killed his wife — publicly accuses King Uther of adultery and demands trial by combat; Uther accepts but God delivers justice, Uther loses, and must pay a ransom of a strong castle thereafter named Uther's Shame.
threads: [Navigate the Argan accusation and its fallout]   characters: [Sir Argan, Uther, Dyagenne]   elements: [Silchester Castle, Easter Court, the castle "Uther's Shame"]   themes: [Tension]
gate: none
fragments:
  - plot_point: "Public accusation: Argan, half-mad with grief, accuses Uther in open court (he has already killed Dyagenne)."   themes: [Tension]   weight: 1
  - plot_point: "The challenge: Argan demands trial by combat; Uther accepts."   themes: [Tension]   weight: 1
  - plot_point: "The duel: Argan (Sword 21) vs. Uther (Sword 23 + Excalibur); God's justice overrides mechanics."   themes: [Action]   weight: 1
  - plot_point: "Uther loses — wounded, disarmed, helpless; pays the ransom of a strong castle ('Uther's Shame')."   themes: [Social]   weight: 1
  - plot_point: "Political fallout: knights must choose sides; the court is in shock."   themes: [Social]   weight: 1

### cluster: malahaut-embassy-493 — "Embassy to Malahaut (493)"   (source: 06-adventures.md § Embassy to Malahaut, 493)
scene: Count Roderick must deliver Uther's ultimatum to the Centurion King with the player-knights as bodyguard; the cold court at Eburacum receives it badly, Saxon men-at-arms are visible in the city, and Saxon warriors ambush the embassy on the road home.
threads: [Deliver Uther's ultimatum, Confirm the Saxon–Malahaut alliance]   characters: [Count Roderick, Centurion King, Saxon Ambushers]   elements: [road Salisbury→Linden→Eburacum, Malahaut, Eburacum]   themes: [Tension]
gate: none
fragments:
  - plot_point: "The journey north through Linden (Corneus now suspicious of strangers)."   themes: [Tension]   weight: 1
  - plot_point: "The Centurion King's court at Eburacum: cold, formal, dismissive; the ultimatum is badly received."   themes: [Social]   weight: 1
  - plot_point: "Discovery: Saxon men-at-arms are visible in the city (Awareness/Intrigue) — proof of the alliance."   themes: [Mystery]   weight: 1
  - plot_point: "The departure: Roderick is unwelcome; they must leave before relations shatter."   themes: [Tension]   weight: 1
  - plot_point: "The ambush: Saxon warriors strike on the road home; Roderick barely survives."   themes: [Action]   weight: 1

### cluster: st-albans-495 — "Battle of St Albans"   (source: 06-adventures.md § Battle of St Albans, 495)
scene: A visibly ill Uther raises his understrength army at the Castle of the Rock and marches with Count Roderick's Salisbury knights to St Albans; an initial assault fails, but the next morning the Saxon gamble on Malahaut collapses and the player-knights crush the flank for victory — Uther's last.
threads: [Win Uther's last battle at St Albans]   characters: [Uther, Ulfius, Brastias, Count Roderick]   elements: [Castle of the Rock, St Albans]   themes: [Action]
gate: none
fragments:
  - plot_point: "Muster: the army is understrength; many lordless knights have not rallied."   themes: [Tension]   weight: 1
  - plot_point: "The march: Uther's illness is visible; soldiers are worried but loyal."   themes: [Personal]   weight: 1
  - plot_point: "Arrival too late: the Saxons hold St Albans; the initial assault fails."   themes: [Tension]   weight: 1
  - plot_point: "Night: Uther refuses to retreat; plans the morning battle."   themes: [Social]   weight: 1
  - plot_point: "The field battle: the Saxon gamble on Malahaut fails; knights crush Malahaut and turn the flank."   themes: [Action]   weight: 1
  - plot_point: "Victory: Saxons routed; celebration begins (Ulfius and Brastias gravely wounded)."   themes: [Action]   weight: 1

### cluster: infamous-feast-495 — "The Infamous Feast"   (source: 06-adventures.md § The Infamous Feast, 495)
scene: At the St Albans victory feast Uther seems almost well for the first time in years, but the poured wine is poisoned; knights collapse one by one, the Saxon physician is seized and executed, and by morning "there are no lords in Logres."
threads: [Survive the poisoned feast, Investigate the poisoning]   characters: [Uther, Count Roderick, Saxon physician, Ulfius, Brastias]   elements: [victory feast hall, the poisoned wine]   themes: [Tension]
gate: [follows st-albans-495]
fragments:
  - plot_point: "The feast: glory and celebration; Uther seems almost well for the first time in years."   themes: [Social]   weight: 1
  - plot_point: "The first deaths: someone collapses, then another; the pattern points to the wine."   themes: [Tension]   weight: 1
  - plot_point: "Chaos: panic and accusations; the Saxon physician is seized and executed."   themes: [Action]   weight: 1
  - plot_point: "Triage: knights may try to save NPCs (Chirurgery, First Aid); Roderick and Uther are dying."   themes: [Tension]   weight: 1
  - plot_point: "The morning after: 'There are no lords in Logres'; the Sword in the Stone appears by Christmas."   themes: [Mystery]   weight: 1

### cluster: savage-forest-495 — "The Savage Forest (495, Post-Feast)"   (source: 06-adventures.md § The Savage Forest, 495 onward)
scene: The Savage Forest suddenly appears around Castle Dykes and spreads to protect the newly-visible Castle Sauvage; one of ten possible reasons (roll 1d10) draws the player-knights into the faerie wood, which is protective rather than hostile and demands Courtesy and Faerie Lore to navigate.
threads: [Enter the Savage Forest and resolve its faerie matter]   characters: [Faerie lords, Castle Sauvage's faerie lord]   elements: [Savage Forest, Castle Dykes / Wuerensis, Castle Sauvage]   themes: [Mystery]
gate: [follows infamous-feast-495]
fragments:
  - plot_point: "The Forest appears around Castle Dykes and spreads; Castle Sauvage becomes visible."   themes: [Mystery]   weight: 1
  - plot_point: "A reason draws the knights in (roll 1d10: kidnapped relative, changeling, missing Eliwlod, a fated castle, a slain father, a stolen heirloom, an undelivered healing potion, a churchman's command, Merlin's word, or Excalibur owed to the faeries)."   themes: [Personal]   weight: 1
  - plot_point: "The Forest is protective, not hostile by default; faerie lords follow their own customs (Courtesy, Faerie Lore)."   themes: [Social]   weight: 1
  - plot_point: "The chosen reason determines what Castle Sauvage contains and who can resolve the situation; the Forest keeps growing through the Anarchy."   themes: [Mystery]   weight: 1

## Seed the Lists from all clusters: Threads (objectives), Characters (NPCs), Adventure Features (locations/hazards).
- **Threads (objectives):** break Paschent's invasion; defeat the Saxons at Salisbury and uncover the spy; compel Bedegraine's homage; survive Eburacum; restore morale at Mt. Damen; destroy the water-leaper nest; secure Corneus' loyalty; manage Madoc's affair; force Summerland's submission; resolve the Cornwall crisis and discern Merlin's purpose; capture Octa and Eosa; win Terrabil / witness Merlin's bargain; survive the treason charge and learn Arthur exists; encounter Pellinore and the Glatisant; navigate the Argan scandal; deliver and confirm the Malahaut ultimatum; win St Albans; survive and investigate the poisoned feast; enter the Savage Forest.
- **Characters (NPCs):** Uther, Aurelius, Gorlois, Ygraine, Aesc of Kent, Octa, Eosa, Gillomanius, King of Bedegraine, Saxon Veteran Axemen, Water Leapers, Duke Corneus, Centurion King, Prince Madoc, Cadwy, Merlin, Gwion the Abbot, Sir Bellias, Sir Goreau, Count Roderick, Uther's household knights, baby Arthur, King Pellinore, the Glatisant, Lamorak, Sir Argan, Dyagenne, Saxon Ambushers, Saxon physician, Ulfius, Brastias, faerie lords.
- **Adventure Features (locations/hazards):** Menevia; Sarum/Salisbury; Bedegraine and the Oakmeet mines; Eburacum/York and Malahaut; Mt. Damen and the Saxon camp; Logres rivers/fens (Lonazep); Linden Pool Castle/Lincoln and Excalibur; the court; the Glamour Forest, Lake of Diana, Glastonbury Abbey; the Logres–Cornwall road; Castle Terrabil and Tintagel Castle; the King's Bench; Silchester and "Uther's Shame"; the Salisbury–Eburacum road; Castle of the Rock and St Albans; the poisoned wine; the Savage Forest, Castle Dykes, and Castle Sauvage; the Sword in the Stone.

## Diminisher (solo scaling): 1/2
