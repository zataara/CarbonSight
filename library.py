states = [("al", "Alabama"), ("ak", "Alaska"), ("az", "Arizona"), ("ar", "Arkansas"), ("ca", "California"), ("co", "Colorado"), ("ct", "Connecticut"), ("cd", "Washington D.C."), ("de", "Delaware"), ("fl", "Florida"), ("ga", "Georgia"), ("hi", "Hawaii"), ("id", "Idaho"), ("il", "Illinois"), ("in", "Indiana"), ("ia", "Iowa"), ("ks", "Kansas"), ("ky", "Kentucky"), ("la", "Louisiana"), ("me", "Maine"), ("md", "Maryland"), ("ma", "Massachusetts"), ("mi", "Michigan"), ("mn", "Minnesota"), ("ms", "Missouri"), ("MO", "Montana"), ("mt", "Montana"), ("ne", "Nebraska"), ("nv", "Nevada"), ("nh", "New Hampshire"), ("nj", "New Jersey"), ("nm", "New Mexico"), ("ny", "New York"), ("nc", "North Carolina"), ("nd", "North Dakota"), ("oh", "Ohio"), ("ok", "Oklahoma"), ("or", "Oregon"), ("pa", "Pennsylvania"), ("ri", "Rhode Island"), ("sc", "South Carolina"), ("sd", "South Dakota"), ("tn", "Tennessee"), ("tx", "Texas"), ("ut", "Utah"), ("vt", "Vermont"), ("va", "Virginia"), ("wa", "Washington"), ("wv", "West Virginia"), ("wi", "Wisconson"), ("wy", "Wyoming")]

cars = [("Acura"), ("Alfa Romeo"), ("Aston Martin"), ("Audi"), ("Bentley"), ("BMW"), ("Bugatti"), ("Buick"), ("Cadillac"), ("Chevrolet"), ("Chrysler"), ("Dodge"), ("Ferrari"), ("Fiat"), ("Ford"), ("General Motors"), ("GMC"),  ("Honda"), ("Hyundai"), ("Infiniti"), ("Isuzu"),("Jaguar"), ("Jeep"), ("Kia"), ("Koenigsegg"),  ("Lamborghini"), ("Land Rover"), ("Lexus"), ("Lincoln"), ("Lotus"), ("Maserati"), ("Mazda"), ("Mercedes Benz"), ("Mercury"),  ("Mini"), ("Mitsubishi"), ("Nissan"), ("Plymouth"), ("Pontiac"),   ("Porsche"), ("Ram"), ("Rolls Royce"), ("Saab"), ("Saturn"), ("Shelby"), ("Smart"), ("Subaru"), ("Suzuki"), ("Toyota"), ("Tesla"), ("Volkswagon"), ("Volvo")]


airports = [('',''),('BHM', 'Birmingham International Airport'), ('DHN', 'Dothan Regional Airport'), ('HSV', 'Huntsville International Airport'), ('MOB', 'Mobile'), ('MGM', 'Montgomery'), ('ANC', 'Anchorage International Airport'), ('FAI', 'Fairbanks International Airport'), ('JNU', 'Juneau International Airport'), ('FLG', 'Flasgstaff'), ('PHX', 'Phoenix Sky Harbor International Airport'), ('TUS', 'Tucson International Airport'), ('YUM', 'Yuma International Airport'), ('FYV', 'Fayetteville'), ('LIT', 'Little Rock National Airport'), ('XNA', 'Northwest Arkansas Regional Airport'), ('BUR', 'Burbank'), ('FAT', 'Fresno'), ('LGB', 'Long Beach'), ('LAX', 'Los Angeles International Airport'), ('OAK', 'Oakland'), ('ONT', 'Ontario'), ('PSP', 'Palm Springs'), ('SMF', 'Sacramento'), ('SAN', 'San Diego'), ('SFO', 'San Fransisco International Airport'), ('SJC', 'San Jose')]



# Santa Ana	SNA
# Colorado	CO
# Aspen	ASE
# Colorado Springs	COS
# Denver International Airport	DEN
# Grand Junction	GJT
# Pueblo	PUB
# Connecticut	CT
# Hartford	BDL
# Tweed New Haven	HVN
# District of Columbia	DC
# Washington, Dulles International Airport	IAD
# Washington National Airport	DCA
# Florida	FL
# Daytona Beach	DAB
# Fort Lauderdale-Hollywood International Airport	FLL
# Fort Meyers	RSW
# Jacksonville	JAX
# Key West International Airport	EYW
# Miami International Airport	MIA
# Orlando	MCO
# Pensacola	PNS
# St. Petersburg	PIE
# Sarasota	SRQ
# Tampa	TPA
# West Palm Beach	PBI
# Panama City-Bay County International Airport	PFN
# Georgia	GA
# Atlanta Hartsfield International Airport	ATL
# Augusta	AGS
# Savannah	SAV
# Hawaii	HI
# Hilo	ITO
# Honolulu International Airport	HNL
# Kahului	OGG
# Kailua	KOA
# Lihue	LIH
# Idaho	ID
# Boise	BOI
# Illinois	IL
# Chicago Midway Airport	MDW
# Chicago, O'Hare International Airport Airport	ORD
# Moline	MLI
# Peoria	PIA
# Indiana	IN
# Evansville	EVV
# Fort Wayne	FWA
# Indianapolis International Airport	IND
# South Bend	SBN
# Iowa	IA
# Cedar Rapids	CID
# Des Moines	DSM
# Kansas	KS
# Wichita	ICT
# Kentucky	KY
# Lexington	LEX
# Louisville	SDF
# Louisiana	LA
# Baton Rouge	BTR
# New Orleans International Airport	MSY
# Shreveport	SHV
# Maine	ME
# Augusta	AUG
# Bangor	BGR
# Portland	PWM
# Maryland	MD
# Baltimore	BWI
# Massachusetts	MA
# Boston, Logan International Airport	BOS
# Hyannis	HYA
# Nantucket	ACK
# Worcester	ORH
# Michigan	MI
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