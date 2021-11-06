states = [("al", "Alabama"), ("ak", "Alaska"), ("az", "Arizona"), ("ar", "Arkansas"), ("ca", "California"), ("co", "Colorado"), ("ct", "Connecticut"), ("cd", "Washington D.C."), ("de", "Delaware"), ("fl", "Florida"), ("ga", "Georgia"), ("hi", "Hawaii"), ("id", "Idaho"), ("il", "Illinois"), ("in", "Indiana"), ("ia", "Iowa"), ("ks", "Kansas"), ("ky", "Kentucky"), ("la", "Louisiana"), ("me", "Maine"), ("md", "Maryland"), ("ma", "Massachusetts"), ("mi", "Michigan"), ("mn", "Minnesota"), ("ms", "Missouri"), ("MO", "Montana"), ("mt", "Montana"), ("ne", "Nebraska"), ("nv", "Nevada"), ("nh", "New Hampshire"), ("nj", "New Jersey"), ("nm", "New Mexico"), ("ny", "New York"), ("nc", "North Carolina"), ("nd", "North Dakota"), ("oh", "Ohio"), ("ok", "Oklahoma"), ("or", "Oregon"), ("pa", "Pennsylvania"), ("ri", "Rhode Island"), ("sc", "South Carolina"), ("sd", "South Dakota"), ("tn", "Tennessee"), ("tx", "Texas"), ("ut", "Utah"), ("vt", "Vermont"), ("va", "Virginia"), ("wa", "Washington"), ("wv", "West Virginia"), ("wi", "Wisconson"), ("wy", "Wyoming")]

cars = [("Acura"), ("Alfa Romeo"), ("Aston Martin"), ("Audi"), ("Bentley"), ("BMW"), ("Bugatti"), ("Buick"), ("Cadillac"), ("Chevrolet"), ("Chrysler"), ("Dodge"), ("Ferrari"), ("Fiat"), ("Ford"), ("General Motors"), ("GMC"),  ("Honda"), ("Hyundai"), ("Infiniti"), ("Isuzu"),("Jaguar"), ("Jeep"), ("Kia"), ("Koenigsegg"),  ("Lamborghini"), ("Land Rover"), ("Lexus"), ("Lincoln"), ("Lotus"), ("Maserati"), ("Mazda"), ("Mercedes Benz"), ("Mercury"),  ("Mini"), ("Mitsubishi"), ("Nissan"), ("Plymouth"), ("Pontiac"),   ("Porsche"), ("Ram"), ("Rolls Royce"), ("Saab"), ("Saturn"), ("Shelby"), ("Smart"), ("Subaru"), ("Suzuki"), ("Toyota"), ("Tesla"), ("Volkswagon"), ("Volvo")]


airports = [('',''),('BHM', 'Birmingham International Airport'), ('DHN', 'Dothan Regional Airport'), ('HSV', 'Huntsville International Airport'), ('MOB', 'Mobile'), ('MGM', 'Montgomery'), ('ANC', 'Anchorage International Airport'), ('FAI', 'Fairbanks International Airport'), ('JNU', 'Juneau International Airport'), ('FLG', 'Flasgstaff'), ('PHX', 'Phoenix Sky Harbor International Airport'), ('TUS', 'Tucson International Airport'), ('YUM', 'Yuma International Airport'), ('FYV', 'Fayetteville'), ('LIT', 'Little Rock National Airport'), ('XNA', 'Northwest Arkansas Regional Airport'), ('BUR', 'Burbank'), ('FAT', 'Fresno'), ('LGB', 'Long Beach'), ('LAX', 'Los Angeles International Airport'), ('OAK', 'Oakland'), ('ONT', 'Ontario'), ('PSP', 'Palm Springs'), ('SMF', 'Sacramento'), ('SAN', 'San Diego'), ('SFO', 'San Fransisco International Airport'), ('SJC', 'San Jose'), ('SNA', 'Santa Ana'), ('ASE', 'Aspen'), ('COS', 'Colorado Springs'), ('DEN', 'Denver International Airport'), ('GJT', 'Grand Junction'), ('PUB', 'Pueblo'), ('BDL', 'Hartford'), ('HVN', 'Tweed New Haven'), ('IAD', 'Washington Dulles International Airport'), ('DCA', 'Washington National Airport'), ('DAB', 'Dayton Beach'), ('FLL', 'Fort Lauderdale-Hollywood International Airport'), ('RSW', 'Fort Meyers'), ('JAX', 'Jacksonville'), ('EYW', 'Key West International Airport'), ('MIA', 'Miami International Airport'), ('MCO', 'Orlando'), ('PNS', 'Pensecola'), ('PIE', 'St. Petersburg'), ('SRQ', 'Sarasota'), ('TPA', 'Tampa'), ('PBI', 'West Palm Beach'), ('PFN', 'Panama City-Bay County International Aiprot'), ('ATL', 'Atlanta Hartfield International Airport'), ('AGS', 'Augusta'), ('SAV', 'Savannah'), ('ITO', 'Hilo'), ('HNL', 'Honolulu International Airport'), ('OGG', 'Kahului'), ('LIH', 'Lihue'), ('BOI', 'Boise'), ('MDW', 'Chicago Midway Airport'), ('ORD', "Chicago, O'Hare International Airport"), ('MLI', 'Moline'), ('PIA', 'Peoria'), ('EVV', 'Evansville'), ('FWA', 'Fort Wayne'), ('IND', 'Indianapolis International Airport'), ('SBN', 'South Bend'), ('CID', 'Ceder Rapids'), ('DSM', 'Des Moines'), ('ICT', 'Wichita'), ('LEX', 'Lexington'), ('SDF', 'Louisville'), ('BTR', 'Baton Rouge'), ('MSY', 'New Orleans International Airport'), ('SHV', 'Shreveport'), ('AUG', 'Augusta'), ('BGR', 'Bangor'), ('PWM', 'Portland'), ('BWI', 'Baltimore'), ('BOS', 'Boston, Logan International Airport'), ('HYA', 'Hyannis'), ('ACK', 'Nantucket'), ('ORH', 'Worcester')]


# Battlecreek	BTL
# Detroit Metropolitan Airport	DTW
# Detroit	DET
# Flint	FNT
# Grand Rapids	GRR
# Kalamazoo-Battle Creek International Airport	AZO
# Lansing	LAN
# Saginaw	MBS
# Minnesota	MN
# Duluth	DLH
# Minneapolis/St.Paul International Airport	MSP
# Rochester	RST
# Mississippi	MS
# Gulfport	GPT
# Jackson	JAN
# Missouri	MO
# Kansas City	MCI
# St Louis, Lambert International Airport	STL
# Springfield	SGF
# Montana	MT
# Billings	BIL
# Nebraska	NE
# Lincoln	LNK
# Omaha	OMA
# Nevada	NV
# Las Vegas, Las Vegas McCarran International Airport	LAS
# Reno-Tahoe International Airport	RNO
# New Hampshire	NH
# Manchester	MHT
# New Jersey	NJ
# Atlantic City International Airport	ACY
# Newark International Airport	EWR
# Trenton	TTN
# New Mexico	NM
# Albuquerque International Airport	ABQ
# Alamogordo	ALM
# New York	NY
# Albany International Airport	ALB
# Buffalo	BUF
# Islip	ISP
# New York, John F Kennedy International Airport	JFK
# New York, La Guardia Airport	LGA
# Newburgh	SWF
# Rochester	ROC
# Syracuse	SYR
# Westchester	HPN
# North Carolina	NC
# Asheville	AVL
# Charlotte/Douglas International Airport	CLT
# Fayetteville	FAY
# Greensboro	GSO
# Raleigh	RDU
# Winston-Salem	INT
# North Dakota	ND
# Bismark	BIS
# Fargo	FAR
# Ohio	OH
# Akron	CAK
# Cincinnati	CVG
# Cleveland	CLE
# Columbus	CMH
# Dayton	DAY
# Toledo	TOL
# Oklahoma	OK
# Oklahoma City	OKC
# Tulsa	TUL
# Oregon	OR
# Eugene	EUG
# Portland International Airport	PDX
# Portland, Hillsboro Airport	HIO
# Salem	SLE
# Pennsylvania	PA
# Allentown	ABE
# Erie	ERI
# Harrisburg	MDT
# Philadelphia	PHL
# Pittsburgh	PIT
# Scranton	AVP
# Rhode Island	RI
# Providence - T.F. Green Airport	PVD
# South Carolina	SC
# Charleston	CHS
# Columbia	CAE
# Greenville	GSP
# Myrtle Beach	MYR
# South Dakota	SD
# Pierre	PIR
# Rapid City	RAP
# Sioux Falls	FSD
# Tennessee	TN
# Bristol	TRI
# Chattanooga	CHA
# Knoxville	TYS
# Memphis	MEM
# Nashville	BNA
# Texas	TX
# Amarillo	AMA
# Austin Bergstrom International Airport	AUS
# Corpus Christi	CRP
# Dallas Love Field Airport	DAL
# Dallas/Fort Worth International Airport	DFW
# El Paso	ELP
# Houston, William B Hobby Airport	HOU
# Houston, George Bush Intercontinental Airport	IAH
# Lubbock	LBB
# Midland	MAF
# San Antonio International Airport	SAT
# Utah	UT
# Salt Lake City	SLC
# Vermont	VT
# Burlington	BTV
# Montpelier	MPV
# Rutland	RUT
# Virginia	VA
# Dulles	IAD
# Newport News	PHF
# Norfolk	ORF
# Richmond	RIC
# Roanoke	ROA
# Washington	WA
# Pasco, Pasco/Tri-Cities Airport	PSC
# Seattle, Tacoma International Airport	SEA
# Spokane International Airport	GEG
# West Virginia	WV
# Charleston	CRW
# Clarksburg	CKB
# Huntington Tri-State Airport	HTS
# Wisconsin	WI
# Green Bay	GRB
# Madison	MSN
# Milwaukee	MKE
# Wyoming	WY
# Casper	CPR
# Cheyenne	CYS
# Jackson Hole	JAC
# Rock Springs	RKS