from multiprocessing import Process, Pipe, Lock
from craigslist import CraigslistForSale
import time

sitesHold = ["sfbay", "seattle", "newyork", "boston", "losangeles", "sandiego", "portland", "washingtondc",
        "chicago", "sacramento", "denver", "atlanta", "austin", "vancouver", "philadelphia", "phoenix",
        "minneapolis", "fortlauderdale", "miami", "dallas", "detroit", "houston", "toronto", "lasvegas",
        "cleveland", "honolulu", "stlouis", "kansascity", "neworleans", "nashville", "pittsburgh", "baltimore",
        "cincinnati", "raleigh", "tampa", "providence", "orlando", "buffalo", "charlotte", "columbus",
        "fresno", "hartford", "indianapolis", "memphis", "milwaukee", "norfolk", "montreal", "albuquerque",
        "anchorage", "boise", "sanantonio", "oklahomacity", "omaha", "saltlakecity", "tucson", "louisville",
        "albany", "richmond", "greensboro", "santabarbara", "bakersfield", "auckland", "tulsa", "dublin",
        "ottawa", "calgary", "edmonton", "winnipeg", "jacksonville", "paris", "amsterdam", "reno", "eugene",
        "spokane", "modesto", "stockton", "desmoines", "wichita", "littlerock", "columbia", "monterey",
        "orangecounty", "inlandempire", "oslo", "copenhagen", "brussels", "saopaulo", "buenosaires",
        "fortmyers", "rochester", "bham", "charleston", "grandrapids", "syracuse", "dayton", "elpaso",
        "lexington", "jackson", "moscow", "rio", "stpetersburg", "marseilles", "lyon", "budapest", "jakarta",
        "santiago", "lima", "telaviv", "jerusalem", "cairo", "madison", "harrisburg", "allentown", "newhaven",
        "maine", "newjersey", "asheville", "annarbor", "westernmass", "halifax", "quebec", "saskatoon",
        "victoria", "caracas", "costarica", "puertorico", "puertorico", "tallahassee", "chico", "redding",
        "humboldt", "chambana", "slo", "montana", "delaware", "wv", "sd", "nd", "wyoming", "nh", "batonrouge",
        "mobile", "ithaca", "knoxville", "pensacola", "toledo", "savannah", "shreveport", "montgomery",
        "ventura", "palmsprings", "cosprings", "lansing", "hamilton", "kitchener", "dubai", "medford",
        "bellingham", "santafe", "gainesville", "chattanooga", "springfield", "columbiamo", "rockford",
        "peoria", "springfieldil", "fortwayne", "evansville", "southbend", "bloomington", "gulfport",
        "huntsville", "salem", "bend", "londonon", "windsor", "sarasota", "daytona", "capecod", "worcester",
        "greenbay", "eauclaire", "appleton", "flagstaff", "micronesia", "micronesia", "yakima", "utica",
        "binghamton", "hudsonvalley", "longisland", "akroncanton", "youngstown", "greenville", "myrtlebeach",
        "duluth", "augusta", "macon", "athensga", "flint", "saginaw", "kalamazoo", "up", "mcallen", "beaumont",
        "corpuschristi", "brownsville", "lubbock", "odessa", "amarillo", "waco", "laredo", "winstonsalem",
        "fayetteville", "wilmington", "erie", "scranton", "pennstate", "reading", "lancaster", "topeka",
        "newlondon", "lincoln", "lafayette", "lakecharles", "merced", "southjersey", "fortcollins", "rockies",
        "roanoke", "charlottesville", "blacksburg", "provo", "fayar", "pakistan", "bangladesh", "beirut",
        "malaysia", "panama", "caribbean", "christchurch", "wellington", "pei", "newfoundland", "cotedazur",
        "quadcities", "easttexas", "nmi", "vietnam", "pueblo", "rmn", "boulder", "westslope", "oregoncoast",
        "eastoregon", "tricities", "kpr", "wenatchee", "collegestation", "killeen", "easternshore", "westmd",
        "keys", "spacecoast", "treasure", "ocala", "lascruces", "eastnc", "outerbanks", "watertown",
        "plattsburgh", "iowacity", "cedarrapids", "siouxcity", "bgky", "columbusga", "bn", "carbondale",
        "visalia", "lawrence", "terrehaute", "cnj", "corvallis", "ogden", "stgeorge", "hiltonhead", "nwct",
        "altoona", "poconos", "york", "fortsmith", "texarkana", "tippecanoe", "muncie", "dubuque", "lacrosse",
        "abilene", "wichitafalls", "lynchburg", "danville", "pullman", "stcloud", "yuma", "tuscaloosa",
        "auburn", "goldcountry", "hattiesburg", "northmiss", "lakeland", "westky", "southcoast",
        "newbrunswick", "kelowna", "kamloops", "nanaimo", "princegeorge", "sudbury", "kingston", "niagara",
        "thunderbay", "peterborough", "barrie", "sherbrooke", "haifa", "salvador", "colombia", "toulouse",
        "bordeaux", "lille", "strasbourg", "loire", "prescott", "roswell", "mankato", "lawton", "joplin",
        "eastidaho", "jonesboro", "jxn", "valdosta", "ksu", "grandisland", "stillwater", "centralmich",
        "fargo", "mansfield", "limaohio", "athensohio", "charlestonwv", "morgantown", "parkersburg",
        "huntington", "wheeling", "martinsburg", "ames", "boone", "harrisonburg", "logan", "sanmarcos",
        "catskills", "chautauqua", "elmira", "mendocino", "imperial", "yubasutter", "fredericksburg", "wausau",
        "roseburg", "annapolis", "skagit", "hickory", "williamsport", "florencesc", "clarksville", "olympic",
        "dothan", "sierravista", "twinfalls", "galveston", "abbotsford", "whistler", "comoxvalley", "reddeer",
        "lethbridge", "ftmcmurray", "regina", "troisrivieres", "saguenay", "cornwall", "guelph", "belleville",
        "chatham", "soo", "sarnia", "owensound", "territories", "belohorizonte", "brasilia", "portoalegre",
        "recife", "curitiba", "fortaleza", "montpellier", "grenoble", "rennes", "rouen", "montevideo",
        "luxembourg", "quito", "zagreb", "ramallah", "racine", "janesville", "muskegon", "porthuron", "smd",
        "staugustine", "jacksontn", "gadsden", "shoals", "jerseyshore", "panamacity", "monroemi", "victoriatx",
        "mohave", "semo", "waterloo", "farmington", "decatur", "brunswick", "sheboygan", "swmi", "sandusky",
        "bucharest", "accra", "addisababa", "kuwait", "lapaz", "reykjavik", "casablanca", "tunis", "kenya",
        "ukraine", "bulgaria", "guatemala", "managua", "elsalvador", "baghdad", "tehran", "virgin", "virgin",
        "santodomingo", "hat", "peace", "cariboo", "sunshine", "skeena", "yellowknife", "whitehorse",
        "brantford", "thumb", "battlecreek", "monroe", "holland", "northernwi", "swv", "frederick", "onslow",
        "statesboro", "nwga", "albanyga", "lakecity", "cfl", "okaloosa", "meridian", "natchez", "houma",
        "cenla", "nacogdoches", "sanangelo", "delrio", "bigbend", "texoma", "enid", "showlow", "elko",
        "clovis", "lewiston", "moseslake", "missoula", "billings", "bozeman", "helena", "greatfalls", "butte",
        "kalispell", "bemidji", "brainerd", "marshall", "bismarck", "grandforks", "northplatte", "scottsbluff",
        "cookeville", "richmondin", "kokomo", "owensboro", "eastky", "klamath", "juneau", "fairbanks", "kenai",
        "siouxfalls", "rapidcity", "csd", "nesd", "potsdam", "oneonta", "fingerlakes", "glensfalls", "swks",
        "nwks", "seks", "salina", "ottumwa", "masoncity", "fortdodge", "stjoseph", "loz", "kirksville",
        "quincy", "lasalle", "mattoon", "ashtabula", "chillicothe", "zanesville", "tuscarawas", "twintiers",
        "chambersburg", "meadville", "susanville", "siskiyou", "hanford", "santamaria", "winchester", "swva",
        "eastco"]

results = []
def f(sites):
    localResults = []
    for site in sites:
        cl_fs = CraigslistForSale(site=site, category='msa', filters={'query': 'guild songbird'})
        for result in cl_fs.get_results(sort_by='newest'):
            localResults.append(result)
    if (len(localResults) > 0):
        print(localResults)


if __name__ == '__main__':
    amountOfLists = 50
    listLength = int(len(sitesHold) / amountOfLists);
    siteLists = []
    siteListCreatorCounter = 0
    for i in range(amountOfLists + 1):
        siteLists.append(sitesHold[siteListCreatorCounter:siteListCreatorCounter+listLength])
        siteListCreatorCounter = siteListCreatorCounter + listLength
    proccesses = []
    for i in range(len(siteLists)):
        proccesses.append(Process(target=f, args=(siteLists[i],)))
    started_at = time.monotonic()
    for process in proccesses:
        process.start()

    for process in proccesses:
        process.join()

    total_time_took = time.monotonic() - started_at
    print(f'Took {total_time_took} second long')