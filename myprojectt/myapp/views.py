from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from .models import Package
from django.http import HttpResponse
from weasyprint import HTML
import tempfile
import os


def index(request):
    return render(request, 'customers/home.html')

def all_cars(request):
    return render(request, 'customers/allcars.html')

def about_view(request):
    return render(request, 'customers/about.html')

def contact_view(request):
    return render(request, 'customers/contact.html')

def domestic(request):
    return render(request, 'customers/domestic_tamilnadu.html')


def all_destinations(request):
    return render(request, 'customers/all_destination.html')

def destination_detail(request, destination_slug):
    # Complete destination data with detailed itineraries for all 30 destinations
    destination_data = {
        'madurai': {
            'name': 'Madurai',
            'tagline': 'City of Temples',
            'duration': '3 Days',
            'image_path': 'images/madurai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Meenakshi Temple',
                    'activities': [
                        'Arrive in Madurai and check into your hotel',
                        'Afternoon visit to the magnificent Meenakshi Amman Temple',
                        'Explore the temple complex with its 14 gopurams',
                        'Evening: Witness the evening ceremony at the temple'
                    ],
                    'highlight': 'Evening puja ceremony at Meenakshi Temple'
                },
                {
                    'day': 2,
                    'title': 'Historical Exploration',
                    'activities': [
                        'Morning visit to Thirumalai Nayakkar Palace',
                        'Explore the Gandhi Museum',
                        'Afternoon visit to Alagar Koyil',
                        'Evening shopping for Madurai specialties'
                    ],
                    'highlight': 'Light and sound show at Thirumalai Nayakkar Palace'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Vandiyur Mariamman Teppakulam',
                        'Last minute shopping for souvenirs',
                        'Depart from Madurai'
                    ],
                    'highlight': 'Boat ride in the temple tank (seasonal)'
                }
            ]
        },
        'ooty': {
            'name': 'Ooty',
            'tagline': 'Queen of Hill Stations',
            'duration': '4 Days',
            'image_path': 'images/ooty.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Local Sightseeing',
                    'activities': [
                        'Arrive in Ooty and check into your hotel',
                        'Visit the Botanical Gardens',
                        'Enjoy a ride on the Nilgiri Mountain Railway',
                        'Evening stroll around Ooty Lake'
                    ],
                    'highlight': 'Toy train ride through scenic landscapes'
                },
                {
                    'day': 2,
                    'title': 'Nature Exploration',
                    'activities': [
                        'Morning visit to Doddabetta Peak',
                        'Explore Pykara Lake and Waterfalls',
                        'Visit the Tea Museum',
                        'Evening at Rose Garden'
                    ],
                    'highlight': 'Boat ride in Pykara Lake'
                },
                {
                    'day': 3,
                    'title': 'Coonoor Excursion',
                    'activities': [
                        'Day trip to Coonoor',
                        'Visit Sims Park and Lamb\'s Rock',
                        'Explore tea plantations',
                        'Return to Ooty in evening'
                    ],
                    'highlight': 'View from Dolphin\'s Nose'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to local markets',
                        'Buy homemade chocolates and tea',
                        'Depart from Ooty'
                    ],
                    'highlight': 'Shopping for Ooty specialties'
                }
            ]
        },
        'mahabalipuram': {
            'name': 'Mahabalipuram',
            'tagline': 'UNESCO World Heritage Site',
            'duration': '2 Days',
            'image_path': 'images/mahabalipuram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Shore Temple',
                    'activities': [
                        'Arrive in Mahabalipuram and check in',
                        'Visit the Shore Temple complex',
                        'Explore Pancha Rathas',
                        'Evening at the beach'
                    ],
                    'highlight': 'Sunset view of Shore Temple'
                },
                {
                    'day': 2,
                    'title': 'Rock Cut Monuments',
                    'activities': [
                        'Morning visit to Arjuna\'s Penance',
                        'See Krishna\'s Butterball',
                        'Explore the Tiger Cave',
                        'Depart from Mahabalipuram'
                    ],
                    'highlight': 'Detailed guide of Arjuna\'s Penance'
                }
            ]
        },
        'kanyakumari': {
            'name': 'Kanyakumari',
            'tagline': 'Land\'s End of India',
            'duration': '2 Days',
            'image_path': 'images/kanyakumari.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Sunset View',
                    'activities': [
                        'Arrive in Kanyakumari and check in',
                        'Visit Vivekananda Rock Memorial',
                        'See Thiruvalluvar Statue',
                        'Witness sunset at Triveni Sangam'
                    ],
                    'highlight': 'Sunset viewing point'
                },
                {
                    'day': 2,
                    'title': 'Sunrise & Departure',
                    'activities': [
                        'Early morning sunrise viewing',
                        'Visit Kumari Amman Temple',
                        'See Gandhi Memorial',
                        'Depart from Kanyakumari'
                    ],
                    'highlight': 'Sunrise over the Bay of Bengal'
                }
            ]
        },
        'chettinad': {
            'name': 'Chettinad',
            'tagline': 'Land of Mansions & Spices',
            'duration': '2 Days',
            'image_path': 'images/chettinad.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Heritage Walk',
                    'activities': [
                        'Arrive in Chettinad and check in',
                        'Heritage walk through Chettinad mansions',
                        'Visit local craft workshops',
                        'Evening cooking demonstration'
                    ],
                    'highlight': 'Chettinad mansion architecture'
                },
                {
                    'day': 2,
                    'title': 'Cultural Experience',
                    'activities': [
                        'Visit Athangudi tile factory',
                        'Explore local markets for spices',
                        'Lunch with authentic Chettinad cuisine',
                        'Depart from Chettinad'
                    ],
                    'highlight': 'Authentic Chettinad meal'
                }
            ]
        },
        'kodaikanal': {
            'name': 'Kodaikanal',
            'tagline': 'Princess of Hill Stations',
            'duration': '3 Days',
            'image_path': 'images/kodainal.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Lake Tour',
                    'activities': [
                        'Arrive in Kodaikanal and check in',
                        'Boat ride on Kodai Lake',
                        'Walk through Coaker\'s Walk',
                        'Evening at Bryant Park'
                    ],
                    'highlight': 'Boat ride on the lake'
                },
                {
                    'day': 2,
                    'title': 'Nature Exploration',
                    'activities': [
                        'Visit Pillar Rocks and Guna Caves',
                        'See Silver Cascade waterfall',
                        'Explore Bear Shola Falls',
                        'Evening shopping'
                    ],
                    'highlight': 'View from Pillar Rocks'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Kurinji Andavar Temple',
                        'Buy homemade chocolates and oils',
                        'Depart from Kodaikanal'
                    ],
                    'highlight': 'Shopping for local products'
                }
            ]
        },
        'thanjavur': {
            'name': 'Thanjavur',
            'tagline': 'Rice Bowl of Tamil Nadu',
            'duration': '2 Days',
            'image_path': 'images/thanjavur.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Brihadeeswarar Temple',
                    'activities': [
                        'Arrive in Thanjavur and check in',
                        'Visit Brihadeeswarar Temple',
                        'Explore the Royal Palace',
                        'Evening at Sivaganga Park'
                    ],
                    'highlight': 'UNESCO World Heritage Site tour'
                },
                {
                    'day': 2,
                    'title': 'Art & Culture',
                    'activities': [
                        'Visit Saraswathi Mahal Library',
                        'See Thanjavur paintings demonstration',
                        'Explore local handicraft markets',
                        'Depart from Thanjavur'
                    ],
                    'highlight': 'Ancient manuscripts viewing'
                }
            ]
        },
        'rameshwaram': {
            'name': 'Rameshwaram',
            'tagline': 'Sacred Island Town',
            'duration': '2 Days',
            'image_path': 'images/rameshwaram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Temple Visit',
                    'activities': [
                        'Arrive in Rameshwaram and check in',
                        'Visit Ramanathaswamy Temple',
                        'Take holy bath in temple theerthams',
                        'Evening at Agnitheertham'
                    ],
                    'highlight': 'Temple rituals experience'
                },
                {
                    'day': 2,
                    'title': 'Dhanushkodi Excursion',
                    'activities': [
                        'Day trip to Dhanushkodi',
                        'Visit abandoned town and beach',
                        'See Adam\'s Bridge viewpoint',
                        'Depart from Rameshwaram'
                    ],
                    'highlight': 'Ghost town exploration'
                }
            ]
        },
        'yercaud': {
            'name': 'Yercaud',
            'tagline': 'Jewel of the South',
            'duration': '2 Days',
            'image_path': 'images/yercaud.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Local Sightseeing',
                    'activities': [
                        'Arrive in Yercaud and check in',
                        'Visit Yercaud Lake for boating',
                        'Explore Pagoda Point',
                        'Evening at Lady\'s Seat'
                    ],
                    'highlight': 'Sunset view from viewpoints'
                },
                {
                    'day': 2,
                    'title': 'Nature Walk & Departure',
                    'activities': [
                        'Morning coffee plantation visit',
                        'Trek to Kiliyur Falls (seasonal)',
                        'Buy local spices and coffee',
                        'Depart from Yercaud'
                    ],
                    'highlight': 'Coffee estate tour'
                }
            ]
        },
        'coonoor': {
            'name': 'Coonoor',
            'tagline': 'Tea Country Paradise',
            'duration': '2 Days',
            'image_path': 'images/coonoor.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Tea Estates',
                    'activities': [
                        'Arrive in Coonoor and check in',
                        'Visit tea estates and factories',
                        'Explore Sims Park',
                        'Evening at Dolphin\'s Nose viewpoint'
                    ],
                    'highlight': 'Tea tasting experience'
                },
                {
                    'day': 2,
                    'title': 'Nature & Departure',
                    'activities': [
                        'Morning visit to Lamb\'s Rock',
                        'Ride the Nilgiri Mountain Railway',
                        'Buy local tea and souvenirs',
                        'Depart from Coonoor'
                    ],
                    'highlight': 'Scenic train ride'
                }
            ]
        },
        'kumbakonam': {
            'name': 'Kumbakonam',
            'tagline': 'Temple Town',
            'duration': '2 Days',
            'image_path': 'images/kumbakonam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Temple Tour',
                    'activities': [
                        'Arrive in Kumbakonam and check in',
                        'Visit Adi Kumbeswarar Temple',
                        'Explore Nageswaran Temple',
                        'Evening at Mahamaham Tank'
                    ],
                    'highlight': 'Ancient temple architecture'
                },
                {
                    'day': 2,
                    'title': 'More Temples & Departure',
                    'activities': [
                        'Morning visit to Sarangapani Temple',
                        'See the famous bronze idols',
                        'Explore local handicrafts',
                        'Depart from Kumbakonam'
                    ],
                    'highlight': 'Bronze idol craftsmanship'
                }
            ]
        },
        'velankanni': {
            'name': 'Velankanni',
            'tagline': 'Lourdes of the East',
            'duration': '2 Days',
            'image_path': 'images/velankanni.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Basilica Visit',
                    'activities': [
                        'Arrive in Velankanni and check in',
                        'Visit Basilica of Our Lady of Good Health',
                        'Attend mass service',
                        'Evening beach walk'
                    ],
                    'highlight': 'Basilica architecture and history'
                },
                {
                    'day': 2,
                    'title': 'Spiritual Experience',
                    'activities': [
                        'Morning prayer and offerings',
                        'Visit museum and shrines',
                        'Explore local markets',
                        'Depart from Velankanni'
                    ],
                    'highlight': 'Spiritual atmosphere'
                }
            ]
        },
        'hogenakkal': {
            'name': 'Hogenakkal',
            'tagline': 'Niagara of India',
            'duration': '1 Day',
            'image_path': 'images/hogenakkal.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Waterfalls Experience',
                    'activities': [
                        'Morning drive to Hogenakkal',
                        'Coracle boat ride in the river',
                        'Swim in natural pools (seasonal)',
                        'Enjoy fish therapy',
                        'Return by evening'
                    ],
                    'highlight': 'Coracle ride through the falls'
                }
            ]
        },
        'courtallam': {
            'name': 'Courtallam',
            'tagline': 'Spa of South India',
            'duration': '1 Day',
            'image_path': 'images/courtallam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Waterfalls Tour',
                    'activities': [
                        'Morning drive to Courtallam',
                        'Visit Five Falls and Main Falls',
                        'Enjoy therapeutic bath in waterfalls',
                        'Explore local markets',
                        'Return by evening'
                    ],
                    'highlight': 'Medicinal properties of the falls'
                }
            ]
        },
        'kovalam': {
            'name': 'Kovalam',
            'tagline': 'Beach Paradise',
            'duration': '1 Day',
            'image_path': 'images/kovalam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Beach Day',
                    'activities': [
                        'Morning drive to Kovalam',
                        'Relax on the golden sands',
                        'Enjoy water sports (seasonal)',
                        'Fresh seafood lunch',
                        'Return by evening'
                    ],
                    'highlight': 'Serene beach experience'
                }
            ]
        },
        'pollachi': {
            'name': 'Pollachi',
            'tagline': 'Gateway to Western Ghats',
            'duration': '1 Day',
            'image_path': 'images/pollachi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Countryside Tour',
                    'activities': [
                        'Morning drive to Pollachi',
                        'Visit coconut and jaggery farms',
                        'Explore Anamalai Wildlife Sanctuary',
                        'Enjoy local cuisine',
                        'Return by evening'
                    ],
                    'highlight': 'Rustic countryside experience'
                }
            ]
        },
        'tranquebar': {
            'name': 'Tranquebar',
            'tagline': 'Danish Heritage Town',
            'duration': '1 Day',
            'image_path': 'images/tranquebar.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Heritage Walk',
                    'activities': [
                        'Morning drive to Tranquebar',
                        'Visit Danish Fort Dansborg',
                        'Explore Zion Church and other colonial buildings',
                        'Beach walk and seafood lunch',
                        'Return by evening'
                    ],
                    'highlight': 'Colonial heritage exploration'
                }
            ]
        },
        'valparai': {
            'name': 'Valparai',
            'tagline': 'Emerald Green Plateau',
            'duration': '2 Days',
            'image_path': 'images/valparai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Tea Estates',
                    'activities': [
                        'Arrive in Valparai and check in',
                        'Visit tea and coffee plantations',
                        'Explore Sholayar Dam',
                        'Evening wildlife spotting'
                    ],
                    'highlight': 'Tea estate tour'
                },
                {
                    'day': 2,
                    'title': 'Nature & Departure',
                    'activities': [
                        'Morning visit to Aliyar Dam',
                        'Trek to Monkey Falls',
                        'Explore local markets',
                        'Depart from Valparai'
                    ],
                    'highlight': 'Scenic waterfalls'
                }
            ]
        },
        'dhanushkodi': {
            'name': 'Dhanushkodi',
            'tagline': 'Ghost Town',
            'duration': '1 Day',
            'image_path': 'images/dhanushkodi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Ghost Town Exploration',
                    'activities': [
                        'Morning drive to Dhanushkodi',
                        'Explore abandoned railway station and buildings',
                        'Visit Adam\'s Bridge viewpoint',
                        'Beach walk and photography',
                        'Return by evening'
                    ],
                    'highlight': 'Eerie abandoned town experience'
                }
            ]
        },
        'kolli-hills': {
            'name': 'Kolli Hills',
            'tagline': 'Land of 70 Hairpin Bends',
            'duration': '2 Days',
            'image_path': 'images/kolli-hills.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Scenic Views',
                    'activities': [
                        'Arrive in Kolli Hills and check in',
                        'Drive through 70 hairpin bends',
                        'Visit Agaya Gangai Waterfalls',
                        'Evening at Seekuparai Viewpoint'
                    ],
                    'highlight': 'Panoramic hill views'
                },
                {
                    'day': 2,
                    'title': 'Nature & Departure',
                    'activities': [
                        'Morning trek to Tampcol Medicinal Farm',
                        'Explore local tribal villages',
                        'Buy organic coffee and honey',
                        'Depart from Kolli Hills'
                    ],
                    'highlight': 'Tribal culture experience'
                }
            ]
        },
        'vellore': {
            'name': 'Vellore',
            'tagline': 'Fort City',
            'duration': '1 Day',
            'image_path': 'images/vellore.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Historical Tour',
                    'activities': [
                        'Morning drive to Vellore',
                        'Explore Vellore Fort',
                        'Visit Jalakandeswarar Temple',
                        'See the Golden Temple (Sripuram)',
                        'Return by evening'
                    ],
                    'highlight': 'Majestic fort architecture'
                }
            ]
        },
        'srirangam': {
            'name': 'Srirangam',
            'tagline': 'Temple Island',
            'duration': '1 Day',
            'image_path': 'images/srirangam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Tour',
                    'activities': [
                        'Morning drive to Srirangam',
                        'Explore Sri Ranganathaswamy Temple complex',
                        'Visit all 7 prakarams (enclosures)',
                        'See the famous golden vimana',
                        'Return by evening'
                    ],
                    'highlight': 'Massive temple complex exploration'
                }
            ]
        },
        'chidambaram': {
            'name': 'Chidambaram',
            'tagline': 'Dance of Shiva',
            'duration': '1 Day',
            'image_path': 'images/chidambaram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Experience',
                    'activities': [
                        'Morning drive to Chidambaram',
                        'Visit Nataraja Temple',
                        'Learn about cosmic dance of Shiva',
                        'Explore temple art and architecture',
                        'Return by evening'
                    ],
                    'highlight': 'Spiritual significance of the temple'
                }
            ]
        },
        'gangaikondacholapuram': {
            'name': 'Gangaikondacholapuram',
            'tagline': 'Chola Capital',
            'duration': '1 Day',
            'image_path': 'images/gangaikondacholapuram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'UNESCO Heritage Tour',
                    'activities': [
                        'Morning drive to Gangaikondacholapuram',
                        'Explore Brihadisvara Temple',
                        'Learn about Chola architecture',
                        'Visit nearby historical sites',
                        'Return by evening'
                    ],
                    'highlight': 'UNESCO World Heritage Site'
                }
            ]
        },
        'darasuram': {
            'name': 'Darasuram',
            'tagline': 'Chola Architectural Marvel',
            'duration': '1 Day',
            'image_path': 'images/darasuram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Exploration',
                    'activities': [
                        'Morning drive to Darasuram',
                        'Visit Airavatesvara Temple',
                        'Study intricate stone carvings',
                        'Learn about temple history',
                        'Return by evening'
                    ],
                    'highlight': 'Exquisite stone sculptures'
                }
            ]
        },
        'tiruvannamalai': {
            'name': 'Tiruvannamalai',
            'tagline': 'Spiritual Capital',
            'duration': '1 Day',
            'image_path': 'images/tiruvannamalai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple & Girivalam',
                    'activities': [
                        'Morning drive to Tiruvannamalai',
                        'Visit Arunachaleswarar Temple',
                        'Walk around the holy hill (Girivalam)',
                        'Visit Ramana Maharshi Ashram',
                        'Return by evening'
                    ],
                    'highlight': 'Spiritual energy of the mountain'
                }
            ]
        },
        'kanchipuram': {
            'name': 'Kanchipuram',
            'tagline': 'City of Thousand Temples',
            'duration': '1 Day',
            'image_path': 'images/kanchipuram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple & Silk Tour',
                    'activities': [
                        'Morning drive to Kanchipuram',
                        'Visit Ekambareswarar Temple',
                        'Explore Kailasanathar Temple',
                        'Silk saree shopping',
                        'Return by evening'
                    ],
                    'highlight': 'Ancient temples and silk weaving'
                }
            ]
        },
        'mudumalai': {
            'name': 'Mudumalai',
            'tagline': 'Wildlife Sanctuary',
            'duration': '2 Days',
            'image_path': 'images/mudumalai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Safari',
                    'activities': [
                        'Arrive in Mudumalai and check in',
                        'Afternoon jeep safari',
                        'Visit elephant camp',
                        'Evening nature walk'
                    ],
                    'highlight': 'Wildlife spotting'
                },
                {
                    'day': 2,
                    'title': 'More Wildlife & Departure',
                    'activities': [
                        'Morning bird watching',
                        'Visit tribal museum',
                        'Explore local markets',
                        'Depart from Mudumalai'
                    ],
                    'highlight': 'Elephant encounters'
                }
            ]
        },
        'vedanthangal': {
            'name': 'Vedanthangal',
            'tagline': 'Bird Watcher\'s Paradise',
            'duration': '1 Day',
            'image_path': 'images/vedanthangal.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Bird Sanctuary Visit',
                    'activities': [
                        'Early morning drive to Vedanthangal',
                        'Guided bird watching tour',
                        'Photography session',
                        'Learn about migratory birds',
                        'Return by evening'
                    ],
                    'highlight': 'Thousands of migratory birds'
                }
            ]
        },
        'pichavaram': {
            'name': 'Pichavaram',
            'tagline': 'Mangrove Forest',
            'duration': '1 Day',
            'image_path': 'images/pichavaram.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Boat Ride Through Mangroves',
                    'activities': [
                        'Morning drive to Pichavaram',
                        'Boat ride through mangrove canals',
                        'Bird watching',
                        'Fresh seafood lunch',
                        'Return by evening'
                    ],
                    'highlight': 'Serene mangrove ecosystem'
                }
            ]
        },
        'yelagiri': {
            'name': 'Yelagiri',
            'tagline': 'Unexplored Hill Station',
            'duration': '2 Days',
            'image_path': 'images/yelagiri.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Nature Walk',
                    'activities': [
                        'Arrive in Yelagiri and check in',
                        'Visit Punganoor Lake Park',
                        'Explore Nature Park',
                        'Evening at Swamimalai Hills'
                    ],
                    'highlight': 'Peaceful hill station atmosphere'
                },
                {
                    'day': 2,
                    'title': 'Adventure & Departure',
                    'activities': [
                        'Morning paragliding (seasonal)',
                        'Visit Jalagamparai Waterfalls',
                        'Buy local honey and fruits',
                        'Depart from Yelagiri'
                    ],
                    'highlight': 'Adventure activities'
                }
            ]
        },
        'thoothukudi': {
            'name': 'Thoothukudi',
            'tagline': 'Pearl City',
            'duration': '1 Day',
            'image_path': 'images/tuticorin.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Port City Tour',
                    'activities': [
                        'Morning drive to Thoothukudi',
                        'Visit Harbour and beaches',
                        'Explore pearl markets',
                        'Enjoy famous Thoothukudi macaroon',
                        'Return by evening'
                    ],
                    'highlight': 'Pearl shopping'
                }
            ]
        },
        'karaikudi': {
            'name': 'Karaikudi',
            'tagline': 'Heart of Chettinad',
            'duration': '1 Day',
            'image_path': 'images/karaikudi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Chettinad Heritage',
                    'activities': [
                        'Morning drive to Karaikudi',
                        'Visit Chettinad mansions',
                        'Explore antique collections',
                        'Enjoy Chettinad lunch',
                        'Return by evening'
                    ],
                    'highlight': 'Grand mansions architecture'
                }
            ]
        },
        'kovilpatti': {
            'name': 'Kovilpatti',
            'tagline': 'Land of Sweets',
            'duration': '1 Day',
            'image_path': 'images/kovilpatti.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Culinary Tour',
                    'activities': [
                        'Morning drive to Kovilpatti',
                        'Visit kadalai mittai (peanut candy) factories',
                        'Explore local markets',
                        'Enjoy traditional sweets',
                        'Return by evening'
                    ],
                    'highlight': 'Famous peanut candy tasting'
                }
            ]
        },
        'salem': {
            'name': 'Salem',
            'tagline': 'Mango City',
            'duration': '1 Day',
            'image_path': 'images/salem.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'City Tour',
                    'activities': [
                        'Morning drive to Salem',
                        'Visit Sugavaneswarar Temple',
                        'Explore Kiliyur Falls',
                        'Shop for famous Salem silk',
                        'Return by evening'
                    ],
                    'highlight': 'Silk shopping'
                }
            ]
        },
        'erode': {
            'name': 'Erode',
            'tagline': 'Turmeric City',
            'duration': '1 Day',
            'image_path': 'images/erode.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Market Tour',
                    'activities': [
                        'Morning drive to Erode',
                        'Visit turmeric and textile markets',
                        'Explore Bhavani Sangameswarar Temple',
                        'Enjoy local cuisine',
                        'Return by evening'
                    ],
                    'highlight': 'Turmeric market experience'
                }
            ]
        }
    }
    
    destination = destination_data.get(destination_slug, {})
    return render(request, 'customers/destination_detail.html', {'destination': destination})

# admin
def admin_dashboard(request):
    packages = Package.objects.all()
    return render(request, 'customers/admin_dashboard.html', {'packages': packages})


def add_package(request):
    if request.method == "POST":
        name = request.POST["name"]
        customer = request.POST["customer"]
        destination = request.POST["destination"]
        start_date = request.POST["start_date"]
        duration = request.POST["duration"]
        pax = request.POST["pax"]
        amount = request.POST["amount"]

        day1 = request.POST["day1"]
        day2 = request.POST["day2"]
        day3 = request.POST["day3"]

        itinerary = f"Day 1: {day1}\nDay 2: {day2}\nDay 3: {day3}"

        Package.objects.create(
            name=name,
            customer=customer,
            destination=destination,
            start_date=start_date,
            duration=duration,
            pax=pax,
            amount=amount,
            itinerary=itinerary
        )
        return redirect("admin_dashboard")  

    return render(request, "customers/addpackage.html")


# pdf function
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

def generate_package_pdf(request, package_id):
    package = get_object_or_404(Package, pk=package_id)

    # Convert itinerary text to a dictionary format
    itinerary = {}
    lines = package.itinerary.strip().split('\n')
    for line in lines:
        if ':' in line:
            day, plan = line.split(':', 1)
            itinerary[day.strip()] = plan.strip()

    html_string = render_to_string("customers/pdfpage.html", {
        "package": {
            "name": package.name,
            "customer": package.customer,
            "amount": package.amount,
            "destination": package.destination,
            "start_date": package.start_date,
            "duration": package.duration,
            "pax": package.pax,
            "trip_id": package.trip_id,
            "itinerary": itinerary,
        }
    })


    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="Package_{package.name}.pdf"'
    return response


#international

def home(request): 
    return render(request,'International/international.html')
def all_international(request):
    return render(request, 'International/all_international.html')

def destination_detail_inter(request, destination_slug):
    # Complete international destination data with detailed itineraries
    destination_data = {
        'paris': {
            'name': 'Paris',
            'tagline': 'City of Love',
            'duration': '5 Days',
            'image_path': 'images/nia.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Eiffel Tower',
                    'activities': [
                        'Arrive in Paris and check into your hotel',
                        'Afternoon visit to the Eiffel Tower',
                        'Seine River cruise in the evening',
                        'Dinner in Montmartre'
                    ],
                    'highlight': 'Eiffel Tower views at sunset'
                },
                {
                    'day': 2,
                    'title': 'Art & History',
                    'activities': [
                        'Morning visit to the Louvre Museum',
                        'Explore Notre-Dame Cathedral',
                        'Walk along Champs-Élysées',
                        'Evening at Arc de Triomphe'
                    ],
                    'highlight': 'Seeing Mona Lisa at the Louvre'
                },
                {
                    'day': 3,
                    'title': 'Palace of Versailles',
                    'activities': [
                        'Day trip to Palace of Versailles',
                        'Tour of the Hall of Mirrors',
                        'Explore the royal gardens',
                        'Return to Paris for evening leisure'
                    ],
                    'highlight': 'Grandeur of Versailles Palace'
                },
                {
                    'day': 4,
                    'title': 'Cultural Exploration',
                    'activities': [
                        'Visit Musée d\'Orsay',
                        'Explore Latin Quarter',
                        'See Sacré-Cœur Basilica',
                        'Evening cabaret show at Moulin Rouge'
                    ],
                    'highlight': 'Montmartre artists\' square'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Last minute shopping at Galeries Lafayette',
                        'Visit Opera Garnier',
                        'Final French pastry tasting',
                        'Depart from Paris'
                    ],
                    'highlight': 'Shopping on Rue du Faubourg Saint-Honoré'
                }
            ]
        },
        'rome': {
            'name': 'Rome',
            'tagline': 'Eternal City',
            'duration': '4 Days',
            'image_path': 'images/rome.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Ancient Rome',
                    'activities': [
                        'Arrive in Rome and check into your hotel',
                        'Visit Colosseum and Roman Forum',
                        'See Palatine Hill',
                        'Evening walk through Piazza Navona'
                    ],
                    'highlight': 'Colosseum underground tour'
                },
                {
                    'day': 2,
                    'title': 'Vatican City',
                    'activities': [
                        'Morning visit to Vatican Museums',
                        'See Sistine Chapel',
                        'Tour St. Peter\'s Basilica',
                        'Evening at Trastevere district'
                    ],
                    'highlight': 'Michelangelo\'s Sistine Chapel ceiling'
                },
                {
                    'day': 3,
                    'title': 'Historic Center',
                    'activities': [
                        'Visit Pantheon',
                        'Throw coin in Trevi Fountain',
                        'Explore Spanish Steps',
                        'Evening food tour'
                    ],
                    'highlight': 'Gelato tasting near Pantheon'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Borghese Gallery',
                        'Last minute shopping',
                        'Final Italian espresso',
                        'Depart from Rome'
                    ],
                    'highlight': 'Borghese Gardens walk'
                }
            ]
        },
        'santorini': {
            'name': 'Santorini',
            'tagline': 'Greek Island Paradise',
            'duration': '4 Days',
            'image_path': 'images/santorini.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Oia Sunset',
                    'activities': [
                        'Arrive in Santorini and check into your hotel',
                        'Explore Fira town',
                        'Sunset viewing in Oia',
                        'Dinner with caldera views'
                    ],
                    'highlight': 'Famous Santorini sunset'
                },
                {
                    'day': 2,
                    'title': 'Volcano & Hot Springs',
                    'activities': [
                        'Boat tour to Nea Kameni volcano',
                        'Swim in hot springs',
                        'Visit Thirassia island',
                        'Evening in Imerovigli'
                    ],
                    'highlight': 'Volcanic hot springs swim'
                },
                {
                    'day': 3,
                    'title': 'Beach Day',
                    'activities': [
                        'Visit Red Beach',
                        'Relax at Perissa black sand beach',
                        'Wine tasting at local winery',
                        'Dinner in Pyrgos village'
                    ],
                    'highlight': 'Santorini wine tasting'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Akrotiri ruins',
                        'Last minute shopping for souvenirs',
                        'Final Greek coffee',
                        'Depart from Santorini'
                    ],
                    'highlight': 'Ancient Akrotiri archaeological site'
                }
            ]
        },
        'barcelona': {
            'name': 'Barcelona',
            'tagline': 'Gaudi\'s Masterpiece',
            'duration': '4 Days',
            'image_path': 'images/barcelona.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Gothic Quarter',
                    'activities': [
                        'Arrive in Barcelona and check into your hotel',
                        'Explore Gothic Quarter',
                        'Visit Barcelona Cathedral',
                        'Evening tapas tour'
                    ],
                    'highlight': 'Historic Gothic Quarter walk'
                },
                {
                    'day': 2,
                    'title': 'Gaudi Architecture',
                    'activities': [
                        'Visit Sagrada Familia',
                        'Explore Park Güell',
                        'See Casa Batlló',
                        'Evening at Magic Fountain show'
                    ],
                    'highlight': 'Sagrada Familia towers'
                },
                {
                    'day': 3,
                    'title': 'Montserrat & Local Culture',
                    'activities': [
                        'Day trip to Montserrat Monastery',
                        'Visit La Boqueria market',
                        'Walk along Las Ramblas',
                        'Flamenco show in evening'
                    ],
                    'highlight': 'Montserrat mountain views'
                },
                {
                    'day': 4,
                    'title': 'Beach & Departure',
                    'activities': [
                        'Morning at Barceloneta beach',
                        'Visit Picasso Museum',
                        'Last minute shopping',
                        'Depart from Barcelona'
                    ],
                    'highlight': 'Fresh seafood paella lunch'
                }
            ]
        },
        'tokyo': {
            'name': 'Tokyo',
            'tagline': 'Neon Metropolis',
            'duration': '5 Days',
            'image_path': 'images/tokyo.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Shibuya',
                    'activities': [
                        'Arrive in Tokyo and check into your hotel',
                        'See Shibuya Crossing',
                        'Visit Hachiko statue',
                        'Evening in Shinjuku'
                    ],
                    'highlight': 'Shibuya skyline view'
                },
                {
                    'day': 2,
                    'title': 'Traditional Tokyo',
                    'activities': [
                        'Visit Senso-ji Temple',
                        'Explore Asakusa district',
                        'Sumida River cruise',
                        'Evening at Tokyo Skytree'
                    ],
                    'highlight': 'Traditional tea ceremony'
                },
                {
                    'day': 3,
                    'title': 'Modern Tokyo',
                    'activities': [
                        'Visit teamLab Planets digital museum',
                        'Explore Akihabara electronics district',
                        'Harajuku and Takeshita Street',
                        'Robot Restaurant show'
                    ],
                    'highlight': 'Akihabara anime shopping'
                },
                {
                    'day': 4,
                    'title': 'Day Trip Options',
                    'activities': [
                        'Option 1: Nikko temples and nature',
                        'Option 2: Hakone hot springs',
                        'Option 3: Kamakura Great Buddha',
                        'Evening izakaya experience'
                    ],
                    'highlight': 'Onsen (hot spring) relaxation'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Tsukiji Outer Market',
                        'Visit Imperial Palace East Gardens',
                        'Last minute shopping in Ginza',
                        'Depart from Tokyo'
                    ],
                    'highlight': 'Fresh sushi breakfast'
                }
            ]
        },
        'bali': {
            'name': 'Bali',
            'tagline': 'Island of Gods',
            'duration': '6 Days',
            'image_path': 'images/bali.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Ubud',
                    'activities': [
                        'Arrive in Bali and transfer to Ubud',
                        'Visit Sacred Monkey Forest',
                        'Explore Ubud art market',
                        'Evening cultural performance'
                    ],
                    'highlight': 'Monkey Forest encounters'
                },
                {
                    'day': 2,
                    'title': 'Temples & Rice Terraces',
                    'activities': [
                        'Sunrise at Besakih Temple',
                        'Visit Tegallalang Rice Terraces',
                        'See Goa Gajah (Elephant Cave)',
                        'Evening Balinese cooking class'
                    ],
                    'highlight': 'Rice terrace swing photos'
                },
                {
                    'day': 3,
                    'title': 'Waterfalls & Volcano',
                    'activities': [
                        'Visit Tegenungan Waterfall',
                        'See Mount Batur volcano',
                        'Relax at hot springs',
                        'Sunset at Tanah Lot Temple'
                    ],
                    'highlight': 'Volcano views'
                },
                {
                    'day': 4,
                    'title': 'Beach Transfer & Relaxation',
                    'activities': [
                        'Transfer to Seminyak beach area',
                        'Relax at beach club',
                        'Sunset at Uluwatu Temple',
                        'Kecak fire dance performance'
                    ],
                    'highlight': 'Beach club luxury'
                },
                {
                    'day': 5,
                    'title': 'Island Exploration',
                    'activities': [
                        'Day trip to Nusa Penida island',
                        'See Kelingking Beach',
                        'Snorkel at Manta Point',
                        'Return to mainland'
                    ],
                    'highlight': 'Nusa Penida cliff views'
                },
                {
                    'day': 6,
                    'title': 'Departure',
                    'activities': [
                        'Morning spa treatment',
                        'Last minute shopping',
                        'Final Balinese meal',
                        'Depart from Bali'
                    ],
                    'highlight': 'Traditional Balinese massage'
                }
            ]
        },
        'dubai': {
            'name': 'Dubai',
            'tagline': 'City of Superlatives',
            'duration': '4 Days',
            'image_path': 'images/dubai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Modern Dubai',
                    'activities': [
                        'Arrive in Dubai and check into your hotel',
                        'Visit Burj Khalifa (At the Top)',
                        'Explore Dubai Mall and fountains',
                        'Evening desert safari with dinner'
                    ],
                    'highlight': 'Burj Khalifa observation deck'
                },
                {
                    'day': 2,
                    'title': 'Cultural & Traditional',
                    'activities': [
                        'Visit Dubai Museum',
                        'Explore Al Fahidi Historic District',
                        'Abra ride across Dubai Creek',
                        'Gold and spice souk shopping'
                    ],
                    'highlight': 'Traditional abra boat ride'
                },
                {
                    'day': 3,
                    'title': 'Palm Island & Luxury',
                    'activities': [
                        'Visit Palm Jumeirah',
                        'Aquaventure Waterpark',
                        'Lunch at Atlantis',
                        'Evening at The Pointe'
                    ],
                    'highlight': 'Palm Jumeirah monorail ride'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Jumeirah Beach',
                        'Visit Miracle Garden (seasonal)',
                        'Last minute shopping',
                        'Depart from Dubai'
                    ],
                    'highlight': 'Beach relaxation with Burj view'
                }
            ]
        },
        'newyork': {
            'name': 'New York',
            'tagline': 'The Big Apple',
            'duration': '5 Days',
            'image_path': 'images/newyork.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Manhattan',
                    'activities': [
                        'Arrive in NYC and check into your hotel',
                        'Times Square exploration',
                        'Broadway show in evening',
                        'Walk through Bryant Park'
                    ],
                    'highlight': 'First Broadway show experience'
                },
                {
                    'day': 2,
                    'title': 'Landmarks & Views',
                    'activities': [
                        'Statue of Liberty cruise',
                        'Visit Ellis Island',
                        'Walk across Brooklyn Bridge',
                        'Evening in DUMBO'
                    ],
                    'highlight': 'Statue of Liberty up close'
                },
                {
                    'day': 3,
                    'title': 'Museums & Central Park',
                    'activities': [
                        'Visit Metropolitan Museum of Art',
                        'Explore Central Park',
                        'See Guggenheim Museum',
                        'Evening rooftop bar'
                    ],
                    'highlight': 'Central Park bike ride'
                },
                {
                    'day': 4,
                    'title': 'Neighborhood Exploration',
                    'activities': [
                        'Explore Greenwich Village',
                        'Walk the High Line',
                        'Visit Chelsea Market',
                        'Evening in SoHo'
                    ],
                    'highlight': 'High Line elevated park'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Grand Central Terminal',
                        'Visit Top of the Rock or Edge',
                        'Last minute shopping',
                        'Depart from NYC'
                    ],
                    'highlight': 'Skyline views from observation deck'
                }
            ]
        },
        'machupicchu': {
            'name': 'Machu Picchu',
            'tagline': 'Lost City of the Incas',
            'duration': '4 Days',
            'image_path': 'images/machupicchu.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival in Cusco',
                    'activities': [
                        'Arrive in Cusco and acclimatize',
                        'Explore Plaza de Armas',
                        'Visit Sacsayhuamán ruins',
                        'Evening briefing'
                    ],
                    'highlight': 'First views of Cusco'
                },
                {
                    'day': 2,
                    'title': 'Sacred Valley',
                    'activities': [
                        'Visit Pisac market and ruins',
                        'Explore Ollantaytambo fortress',
                        'Train to Aguas Calientes',
                        'Prepare for Machu Picchu'
                    ],
                    'highlight': 'Sacred Valley scenery'
                },
                {
                    'day': 3,
                    'title': 'Machu Picchu',
                    'activities': [
                        'Sunrise at Machu Picchu',
                        'Guided tour of the citadel',
                        'Optional hike to Sun Gate',
                        'Return to Cusco'
                    ],
                    'highlight': 'First glimpse of Machu Picchu'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Visit Koricancha temple',
                        'Explore San Pedro market',
                        'Final Peruvian meal',
                        'Depart from Cusco'
                    ],
                    'highlight': 'Last minute alpaca souvenirs'
                }
            ]
        },
        'sydney': {
            'name': 'Sydney',
            'tagline': 'Harbor City',
            'duration': '4 Days',
            'image_path': 'images/sydney.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Harbor',
                    'activities': [
                        'Arrive in Sydney and check into your hotel',
                        'Visit Sydney Opera House',
                        'Walk across Harbour Bridge',
                        'Evening at The Rocks'
                    ],
                    'highlight': 'Opera House guided tour'
                },
                {
                    'day': 2,
                    'title': 'Beaches & Coastal Walk',
                    'activities': [
                        'Bondi Beach visit',
                        'Bondi to Coogee coastal walk',
                        'Relax at Bronte Beach',
                        'Evening in Darling Harbour'
                    ],
                    'highlight': 'Coastal walk scenery'
                },
                {
                    'day': 3,
                    'title': 'Blue Mountains',
                    'activities': [
                        'Day trip to Blue Mountains',
                        'See Three Sisters rock formation',
                        'Scenic World rides',
                        'Return to Sydney'
                    ],
                    'highlight': 'Blue Mountains vistas'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Manly Beach',
                        'Visit Taronga Zoo',
                        'Last minute shopping',
                        'Depart from Sydney'
                    ],
                    'highlight': 'Ferry ride to Manly'
                }
            ]
        },
        'kyoto': {
            'name': 'Kyoto',
            'tagline': 'Ancient Capital of Japan',
            'duration': '4 Days',
            'image_path': 'images/kyoto.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Higashiyama',
                    'activities': [
                        'Arrive in Kyoto and check into ryokan',
                        'Visit Kiyomizu-dera Temple',
                        'Walk through Higashiyama district',
                        'Evening at Gion district'
                    ],
                    'highlight': 'Spotting geisha in Gion'
                },
                {
                    'day': 2,
                    'title': 'Golden Pavilion & Arashiyama',
                    'activities': [
                        'Visit Kinkaku-ji (Golden Pavilion)',
                        'Explore Ryoan-ji rock garden',
                        'Bamboo forest in Arashiyama',
                        'Monkey Park visit'
                    ],
                    'highlight': 'Bamboo forest walk'
                },
                {
                    'day': 3,
                    'title': 'Fushimi & Nara Day Trip',
                    'activities': [
                        'Fushimi Inari Shrine (thousand torii gates)',
                        'Day trip to Nara',
                        'See Todai-ji Temple and Great Buddha',
                        'Feed deer in Nara Park'
                    ],
                    'highlight': 'Fushimi Inari early morning'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Nishiki Market',
                        'Tea ceremony experience',
                        'Last minute shopping',
                        'Depart from Kyoto'
                    ],
                    'highlight': 'Matcha tasting'
                }
            ]
        },
        'iceland': {
            'name': 'Iceland',
            'tagline': 'Land of Fire and Ice',
            'duration': '7 Days',
            'image_path': 'images/iceland.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Reykjavik',
                    'activities': [
                        'Arrive in Reykjavik and check in',
                        'Explore Hallgrímskirkja church',
                        'Visit Harpa Concert Hall',
                        'Northern Lights hunt (seasonal)'
                    ],
                    'highlight': 'First glimpse of aurora'
                },
                {
                    'day': 2,
                    'title': 'Golden Circle',
                    'activities': [
                        'Visit Thingvellir National Park',
                        'See Geysir geothermal area',
                        'Gullfoss waterfall',
                        'Secret Lagoon hot spring'
                    ],
                    'highlight': 'Strokkur geyser eruption'
                },
                {
                    'day': 3,
                    'title': 'South Coast',
                    'activities': [
                        'Seljalandsfoss waterfall',
                        'Skogafoss waterfall',
                        'Black sand beach at Reynisfjara',
                        'Vik village visit'
                    ],
                    'highlight': 'Walking behind waterfalls'
                },
                {
                    'day': 4,
                    'title': 'Glacier & Lagoon',
                    'activities': [
                        'Skaftafell National Park',
                        'Glacier hike on Vatnajökull',
                        'Jökulsárlón Glacier Lagoon',
                        'Diamond Beach'
                    ],
                    'highlight': 'Glacier lagoon boat tour'
                },
                {
                    'day': 5,
                    'title': 'East Fjords',
                    'activities': [
                        'Scenic drive through fjords',
                        'Visit fishing villages',
                        'Hengifoss waterfall hike',
                        'Local seafood dinner'
                    ],
                    'highlight': 'Remote fjord landscapes'
                },
                {
                    'day': 6,
                    'title': 'Lake Myvatn',
                    'activities': [
                        'Dettifoss waterfall',
                        'Myvatn geothermal area',
                        'Grjótagjá lava cave',
                        'Myvatn Nature Baths'
                    ],
                    'highlight': 'Blue Lagoon alternative'
                },
                {
                    'day': 7,
                    'title': 'Departure',
                    'activities': [
                        'Whale watching tour',
                        'Last minute Reykjavik shopping',
                        'Try fermented shark (if brave)',
                        'Depart from Iceland'
                    ],
                    'highlight': 'Whale sightings'
                }
            ]
        },
        'cairo': {
            'name': 'Cairo',
            'tagline': 'City of a Thousand Minarets',
            'duration': '4 Days',
            'image_path': 'images/cairo.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Pyramids',
                    'activities': [
                        'Arrive in Cairo and check in',
                        'Visit Giza Pyramids',
                        'See Great Sphinx',
                        'Sound and Light show at night'
                    ],
                    'highlight': 'First view of the pyramids'
                },
                {
                    'day': 2,
                    'title': 'Museum & Old Cairo',
                    'activities': [
                        'Egyptian Museum visit',
                        'See Tutankhamun treasures',
                        'Explore Coptic Cairo',
                        'Khan el-Khalili bazaar'
                    ],
                    'highlight': 'Golden mask of Tutankhamun'
                },
                {
                    'day': 3,
                    'title': 'Islamic Cairo',
                    'activities': [
                        'Visit Citadel of Saladin',
                        'Mohamed Ali Mosque',
                        'Al-Azhar Mosque',
                        'Dinner cruise on Nile'
                    ],
                    'highlight': 'Panoramic city views from Citadel'
                },
                {
                    'day': 4,
                    'title': 'Day Trip & Departure',
                    'activities': [
                        'Day trip to Memphis and Saqqara',
                        'See Step Pyramid',
                        'Final Egyptian meal',
                        'Depart from Cairo'
                    ],
                    'highlight': 'Ancient Step Pyramid'
                }
            ]
        },
        'queenstown': {
            'name': 'Queenstown',
            'tagline': 'Adventure Capital of the World',
            'duration': '5 Days',
            'image_path': 'images/queenstown.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Scenic Views',
                    'activities': [
                        'Arrive in Queenstown and check in',
                        'Gondola ride up Bob\'s Peak',
                        'Luge rides',
                        'Dinner with lake views'
                    ],
                    'highlight': 'Sunset over Lake Wakatipu'
                },
                {
                    'day': 2,
                    'title': 'Adventure Day',
                    'activities': [
                        'Bungee jumping at Kawarau Bridge',
                        'Jet boat ride',
                        'Shotover Canyon Swing',
                        'Relax at Onsen Hot Pools'
                    ],
                    'highlight': 'First bungee jump'
                },
                {
                    'day': 3,
                    'title': 'Milford Sound',
                    'activities': [
                        'Scenic drive to Milford Sound',
                        'Boat cruise on the fjord',
                        'See waterfalls and wildlife',
                        'Return to Queenstown'
                    ],
                    'highlight': 'Mitre Peak views'
                },
                {
                    'day': 4,
                    'title': 'Wine & Relaxation',
                    'activities': [
                        'Gibbston Valley wine tour',
                        'Visit Arrowtown historic village',
                        'Fergburger experience',
                        'Evening lake walk'
                    ],
                    'highlight': 'Pinot Noir tasting'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Morning hike to Queenstown Hill',
                        'Last minute shopping',
                        'Final NZ flat white coffee',
                        'Depart from Queenstown'
                    ],
                    'highlight': 'Panoramic hike views'
                }
            ]
        },
        'capetown': {
            'name': 'Cape Town',
            'tagline': 'Mother City',
            'duration': '5 Days',
            'image_path': 'images/capetown.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Waterfront',
                    'activities': [
                        'Arrive in Cape Town and check in',
                        'Explore V&A Waterfront',
                        'Sunset at Signal Hill',
                        'Dinner with mountain views'
                    ],
                    'highlight': 'First view of Table Mountain'
                },
                {
                    'day': 2,
                    'title': 'Table Mountain & Penguins',
                    'activities': [
                        'Cable car up Table Mountain',
                        'Hike to Maclear\'s Beacon',
                        'Visit Boulders Beach penguins',
                        'Chapman\'s Peak drive'
                    ],
                    'highlight': 'Penguin encounters'
                },
                {
                    'day': 3,
                    'title': 'Cape Peninsula',
                    'activities': [
                        'Drive to Cape of Good Hope',
                        'Visit Cape Point lighthouse',
                        'Scenic coastal walks',
                        'Kirstenbosch Gardens'
                    ],
                    'highlight': 'Southernmost point of Africa'
                },
                {
                    'day': 4,
                    'title': 'Wine Lands',
                    'activities': [
                        'Day trip to Stellenbosch',
                        'Wine tasting at 3-4 estates',
                        'Explore Franschhoek village',
                        'Wine tram experience'
                    ],
                    'highlight': 'South African wine tasting'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Camps Bay beach',
                        'Visit Bo-Kaap colorful houses',
                        'Last minute shopping',
                        'Depart from Cape Town'
                    ],
                    'highlight': 'Bo-Kaap photography'
                }
            ]
        },
        'prague': {
            'name': 'Prague',
            'tagline': 'City of a Hundred Spires',
            'duration': '4 Days',
            'image_path': 'images/prague.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Old Town',
                    'activities': [
                        'Arrive in Prague and check in',
                        'Old Town Square exploration',
                        'See Astronomical Clock',
                        'Charles Bridge at sunset'
                    ],
                    'highlight': 'Astronomical Clock show'
                },
                {
                    'day': 2,
                    'title': 'Castle & Lesser Town',
                    'activities': [
                        'Prague Castle complex tour',
                        'St. Vitus Cathedral visit',
                        'Golden Lane exploration',
                        'Petrin Hill lookout'
                    ],
                    'highlight': 'Castle complex views'
                },
                {
                    'day': 3,
                    'title': 'Jewish Quarter & Culture',
                    'activities': [
                        'Jewish Quarter walking tour',
                        'Visit Old Jewish Cemetery',
                        'Czech beer tasting',
                        'Black Light Theater show'
                    ],
                    'highlight': 'Historic Jewish sites'
                },
                {
                    'day': 4,
                    'title': 'Day Trip & Departure',
                    'activities': [
                        'Day trip to Kutná Hora',
                        'See Sedlec Ossuary (Bone Church)',
                        'Last minute souvenir shopping',
                        'Depart from Prague'
                    ],
                    'highlight': 'Unique bone chapel'
                }
            ]
        },
        'maldives': {
            'name': 'Maldives',
            'tagline': 'Tropical Paradise',
            'duration': '5 Days',
            'image_path': 'images/maldives.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Resort',
                    'activities': [
                        'Seaplane transfer to resort',
                        'Check into overwater bungalow',
                        'Resort orientation',
                        'Sunset cocktails on the beach'
                    ],
                    'highlight': 'First view of turquoise water'
                },
                {
                    'day': 2,
                    'title': 'Snorkeling & Relaxation',
                    'activities': [
                        'House reef snorkeling',
                        'Relax on private deck',
                        'Spa treatment',
                        'Stargazing from bungalow'
                    ],
                    'highlight': 'Swimming with tropical fish'
                },
                {
                    'day': 3,
                    'title': 'Island Hopping',
                    'activities': [
                        'Visit local fishing village',
                        'Picnic on deserted island',
                        'Dolphin watching cruise',
                        'Beach barbecue dinner'
                    ],
                    'highlight': 'Private island experience'
                },
                {
                    'day': 4,
                    'title': 'Water Activities',
                    'activities': [
                        'Scuba diving (optional)',
                        'Stand-up paddleboarding',
                        'Sunset sailing',
                        'Underwater restaurant dinner'
                    ],
                    'highlight': 'Coral reef exploration'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Final morning swim',
                        'Relax on beach until transfer',
                        'Seaplane back to Male',
                        'Depart from Maldives'
                    ],
                    'highlight': 'Last moments in paradise'
                }
            ]
        },
        'vienna': {
            'name': 'Vienna',
            'tagline': 'City of Music',
            'duration': '4 Days',
            'image_path': 'images/vienna.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Imperial Vienna',
                    'activities': [
                        'Arrive in Vienna and check in',
                        'Visit Schönbrunn Palace',
                        'Walk through palace gardens',
                        'Evening classical concert'
                    ],
                    'highlight': 'Palace grandeur'
                },
                {
                    'day': 2,
                    'title': 'Historic Center',
                    'activities': [
                        'St. Stephen\'s Cathedral',
                        'Hofburg Palace complex',
                        'Spanish Riding School',
                        'Café Central experience'
                    ],
                    'highlight': 'Viennese coffee culture'
                },
                {
                    'day': 3,
                    'title': 'Art & Culture',
                    'activities': [
                        'Kunsthistorisches Museum',
                        'Belvedere Palace (Klimt\'s Kiss)',
                        'Prater amusement park',
                        'Heuriger wine tavern'
                    ],
                    'highlight': 'Seeing The Kiss painting'
                },
                {
                    'day': 4,
                    'title': 'Day Trip & Departure',
                    'activities': [
                        'Day trip to Wachau Valley',
                        'Melk Abbey visit',
                        'Danube river cruise',
                        'Depart from Vienna'
                    ],
                    'highlight': 'Danube Valley scenery'
                }
            ]
        },
        'lisbon': {
            'name': 'Lisbon',
            'tagline': 'City of Seven Hills',
            'duration': '4 Days',
            'image_path': 'images/lisbon.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Alfama',
                    'activities': [
                        'Arrive in Lisbon and check in',
                        'Explore Alfama district',
                        'Visit São Jorge Castle',
                        'Fado music evening'
                    ],
                    'highlight': 'Castle views over city'
                },
                {
                    'day': 2,
                    'title': 'Belém & Discoveries',
                    'activities': [
                        'Jerónimos Monastery',
                        'Belém Tower',
                        'Pasteis de Belém tasting',
                        'Discoveries Monument'
                    ],
                    'highlight': 'Original custard tarts'
                },
                {
                    'day': 3,
                    'title': 'Sintra Day Trip',
                    'activities': [
                        'Pena Palace visit',
                        'Quinta da Regaleira',
                        'Moorish Castle',
                        'Cabo da Roca sunset'
                    ],
                    'highlight': 'Colorful Pena Palace'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Tram 28 ride',
                        'LX Factory exploration',
                        'Last minute shopping',
                        'Depart from Lisbon'
                    ],
                    'highlight': 'Iconic tram experience'
                }
            ]
        },
        'budapest': {
            'name': 'Budapest',
            'tagline': 'Pearl of the Danube',
            'duration': '4 Days',
            'image_path': 'images/budapest.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Pest Side',
                    'activities': [
                        'Arrive in Budapest and check in',
                        'Heroes\' Square visit',
                        'Vajdahunyad Castle',
                        'Evening at ruin pub'
                    ],
                    'highlight': 'First ruin pub experience'
                },
                {
                    'day': 2,
                    'title': 'Buda Castle & Views',
                    'activities': [
                        'Fisherman\'s Bastion',
                        'Matthias Church',
                        'Buda Castle tour',
                        'Danube cruise at night'
                    ],
                    'highlight': 'City views from Bastion'
                },
                {
                    'day': 3,
                    'title': 'Thermal Baths',
                    'activities': [
                        'Széchenyi Thermal Baths',
                        'Andrássy Avenue walk',
                        'Opera House tour',
                        'Great Market Hall'
                    ],
                    'highlight': 'Thermal bath relaxation'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Gellért Hill hike',
                        'Liberty Statue views',
                        'Last minute shopping',
                        'Depart from Budapest'
                    ],
                    'highlight': 'Final panoramic views'
                }
            ]
        },
        'amsterdam': {
            'name': 'Amsterdam',
            'tagline': 'Venice of the North',
            'duration': '4 Days',
            'image_path': 'images/amsterdam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Canals',
                    'activities': [
                        'Arrive in Amsterdam and check in',
                        'Canal cruise',
                        'Dam Square walk',
                        'Evening in Jordaan district'
                    ],
                    'highlight': 'First canal views'
                },
                {
                    'day': 2,
                    'title': 'Museums & Culture',
                    'activities': [
                        'Rijksmuseum visit',
                        'Van Gogh Museum',
                        'Anne Frank House',
                        'Vondelpark relaxation'
                    ],
                    'highlight': 'Seeing Van Gogh\'s works'
                },
                {
                    'day': 3,
                    'title': 'Day Trip & Windmills',
                    'activities': [
                        'Zaanse Schans windmills',
                        'Edam cheese tasting',
                        'Volendam fishing village',
                        'Evening bike tour'
                    ],
                    'highlight': 'Traditional windmills'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Albert Cuyp Market',
                        'Last minute shopping',
                        'Final Dutch pancake',
                        'Depart from Amsterdam'
                    ],
                    'highlight': 'Local market experience'
                }
            ]
        },
        'seoul': {
            'name': 'Seoul',
            'tagline': 'Dynamic City',
            'duration': '5 Days',
            'image_path': 'images/seoul.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Modern Seoul',
                    'activities': [
                        'Arrive in Seoul and check in',
                        'Lotte World Tower visit',
                        'Dongdaemun Design Plaza',
                        'Evening in Myeongdong'
                    ],
                    'highlight': 'City views from Lotte'
                },
                {
                    'day': 2,
                    'title': 'Palaces & History',
                    'activities': [
                        'Gyeongbokgung Palace',
                        'Bukchon Hanok Village',
                        'Changdeokgung Palace',
                        'Insadong cultural street'
                    ],
                    'highlight': 'Palace guard ceremony'
                },
                {
                    'day': 3,
                    'title': 'DMZ Tour',
                    'activities': [
                        'DMZ day tour',
                        'Third Infiltration Tunnel',
                        'Dora Observatory',
                        'Return to Seoul'
                    ],
                    'highlight': 'View into North Korea'
                },
                {
                    'day': 4,
                    'title': 'Markets & Street Food',
                    'activities': [
                        'Gwangjang Market',
                        'Namsan Seoul Tower',
                        'Hongdae street performances',
                        'Korean BBQ dinner'
                    ],
                    'highlight': 'Street food tasting'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Han River',
                        'Last minute shopping',
                        'Final Korean meal',
                        'Depart from Seoul'
                    ],
                    'highlight': 'Relaxing by Han River'
                }
            ]
        },
        'bangkok': {
            'name': 'Bangkok',
            'tagline': 'City of Angels',
            'duration': '4 Days',
            'image_path': 'images/bangkok.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Temples',
                    'activities': [
                        'Arrive in Bangkok and check in',
                        'Grand Palace visit',
                        'Wat Pho (Reclining Buddha)',
                        'Evening at Khao San Road'
                    ],
                    'highlight': 'Emerald Buddha'
                },
                {
                    'day': 2,
                    'title': 'Markets & River',
                    'activities': [
                        'Chatuchak Weekend Market',
                        'Chao Phraya River cruise',
                        'Wat Arun at sunset',
                        'Chinatown street food'
                    ],
                    'highlight': 'Massive market shopping'
                },
                {
                    'day': 3,
                    'title': 'Cultural Experiences',
                    'activities': [
                        'Thai cooking class',
                        'Muay Thai boxing match',
                        'Traditional Thai massage',
                        'Rooftop bar evening'
                    ],
                    'highlight': 'Learning Thai cooking'
                },
                {
                    'day': 4,
                    'title': 'Day Trip & Departure',
                    'activities': [
                        'Day trip to Ayutthaya',
                        'Ancient ruins exploration',
                        'Last minute shopping',
                        'Depart from Bangkok'
                    ],
                    'highlight': 'Historic Ayutthaya'
                }
            ]
        },
        'istanbul': {
            'name': 'Istanbul',
            'tagline': 'City on Two Continents',
            'duration': '5 Days',
            'image_path': 'images/istanbul.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Old City',
                    'activities': [
                        'Arrive in Istanbul and check in',
                        'Hagia Sophia visit',
                        'Blue Mosque exploration',
                        'Evening in Sultanahmet'
                    ],
                    'highlight': 'First view of Hagia Sophia'
                },
                {
                    'day': 2,
                    'title': 'Topkapi & Bazaars',
                    'activities': [
                        'Topkapi Palace tour',
                        'Grand Bazaar shopping',
                        'Spice Market visit',
                        'Bosphorus cruise'
                    ],
                    'highlight': 'Palace harem rooms'
                },
                {
                    'day': 3,
                    'title': 'Asian Side & Modern',
                    'activities': [
                        'Cross to Asian side',
                        'Üsküdar and Kadıköy',
                        'Istiklal Street walk',
                        'Galata Tower sunset'
                    ],
                    'highlight': 'Two continents in one day'
                },
                {
                    'day': 4,
                    'title': 'Cultural Experiences',
                    'activities': [
                        'Turkish bath experience',
                        'Whirling Dervish show',
                        'Traditional Turkish dinner',
                        'Nighttime city views'
                    ],
                    'highlight': 'Authentic hamam'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Süleymaniye Mosque',
                        'Final Turkish coffee',
                        'Last minute shopping',
                        'Depart from Istanbul'
                    ],
                    'highlight': 'Mosque architecture'
                }
            ]
        },
        'niagarafalls': {
            'name': 'Niagara Falls',
            'tagline': 'Thundering Waters',
            'duration': '2 Days',
            'image_path': 'images/niagarafalls.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Canadian Side',
                    'activities': [
                        'Arrive and check into fallsview hotel',
                        'Hornblower Niagara Cruise',
                        'Explore Clifton Hill attractions',
                        'Evening falls illumination show'
                    ],
                    'highlight': 'Maid of the Mist boat ride'
                },
                {
                    'day': 2,
                    'title': 'American Side & Departure',
                    'activities': [
                        'Walk across Rainbow Bridge',
                        'Visit Cave of the Winds',
                        'Explore Niagara Falls State Park',
                        'Depart from Niagara'
                    ],
                    'highlight': 'Terrapin Point view (US side)'
                }
            ]
        },
        'swiss_alps': {
            'name': 'Swiss Alps',
            'tagline': 'Majestic Mountain Paradise',
            'duration': '4 Days',
            'image_path': 'images/swiss_alps.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Zermatt',
                    'activities': [
                        'Scenic train to Zermatt',
                        'Check into mountain lodge',
                        'Explore car-free village',
                        'Evening Matterhorn views'
                    ],
                    'highlight': 'First sight of Matterhorn'
                },
                {
                    'day': 2,
                    'title': 'Gornergrat Railway',
                    'activities': [
                        'Ride Gornergrat cogwheel train',
                        'Panoramic views at 3,089m',
                        'Hike Riffelsee Lake trail',
                        'Fondue dinner'
                    ],
                    'highlight': 'Matterhorn reflection in Riffelsee'
                },
                {
                    'day': 3,
                    'title': 'Glacier Paradise',
                    'activities': [
                        'Matterhorn Glacier Paradise cable car',
                        'Highest viewing platform in Europe',
                        'Glacier Palace ice caves',
                        'Sunset at Stellisee lake'
                    ],
                    'highlight': '365-day skiing at Glacier Paradise'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning hike to Five Lakes Trail',
                        'Last Swiss chocolate shopping',
                        'Scenic train departure'
                    ],
                    'highlight': 'Five Lakes Trail photo spots'
                }
            ]
        },
        'hong_kong': {
            'name': 'Hong Kong',
            'tagline': 'East Meets West',
            'duration': '4 Days',
            'image_path': 'images/hong_kong.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Victoria Peak',
                    'activities': [
                        'Arrive and check into Kowloon hotel',
                        'Star Ferry to Hong Kong Island',
                        'Peak Tram to Victoria Peak',
                        'Symphony of Lights show'
                    ],
                    'highlight': 'Peak Tower skyline view'
                },
                {
                    'day': 2,
                    'title': 'Lantau Island',
                    'activities': [
                        'Ngong Ping 360 cable car',
                        'Visit Tian Tan Buddha',
                        'Explore Po Lin Monastery',
                        'Evening Temple Street Night Market'
                    ],
                    'highlight': 'Giant Buddha statue'
                },
                {
                    'day': 3,
                    'title': 'City Exploration',
                    'activities': [
                        'Morning at Wong Tai Sin Temple',
                        'Afternoon in Causeway Bay',
                        'Ride Ding Ding trams',
                        'Nightlife in Lan Kwai Fong'
                    ],
                    'highlight': 'Hong Kong-style milk tea'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning dim sum breakfast',
                        'Last shopping in Mong Kok',
                        'Visit Avenue of Stars',
                        'Depart from Hong Kong'
                    ],
                    'highlight': 'Egg waffle street snack'
                }
            ]
        },
        'singapore': {
            'name': 'Singapore',
            'tagline': 'Garden City',
            'duration': '3 Days',
            'image_path': 'images/singapore.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Marina Bay',
                    'activities': [
                        'Arrive at Changi Airport',
                        'Check into Marina Bay hotel',
                        'Visit Gardens by the Bay',
                        'Evening light show at Supertree Grove'
                    ],
                    'highlight': 'Cloud Forest conservatory'
                },
                {
                    'day': 2,
                    'title': 'Cultural Districts',
                    'activities': [
                        'Morning in Chinatown',
                        'Afternoon in Little India',
                        'Explore Kampong Glam',
                        'Night safari at Singapore Zoo'
                    ],
                    'highlight': 'Sri Mariamman Temple'
                },
                {
                    'day': 3,
                    'title': 'Sentosa & Departure',
                    'activities': [
                        'Day at Sentosa Island',
                        'Visit Universal Studios',
                        'Siloso Beach sunset',
                        'Depart from Singapore'
                    ],
                    'highlight': 'Merlion statue photo'
                }
            ]
        },
        'los_angeles': {
            'name': 'Los Angeles',
            'tagline': 'City of Angels',
            'duration': '4 Days',
            'image_path': 'images/los_angeles.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Hollywood',
                    'activities': [
                        'Arrive and check into Hollywood hotel',
                        'Walk of Fame & TCL Chinese Theatre',
                        'Sunset at Griffith Observatory',
                        'Evening on Sunset Strip'
                    ],
                    'highlight': 'Hollywood sign view'
                },
                {
                    'day': 2,
                    'title': 'Beaches & Coastal',
                    'activities': [
                        'Morning at Santa Monica Pier',
                        'Explore Venice Beach boardwalk',
                        'Afternoon in Malibu',
                        'Dinner in Beverly Hills'
                    ],
                    'highlight': 'Venice Beach skate park'
                },
                {
                    'day': 3,
                    'title': 'Museums & Culture',
                    'activities': [
                        'Visit Getty Center',
                        'Explore LACMA',
                        'Shop on Rodeo Drive',
                        'Evening at The Grove'
                    ],
                    'highlight': 'Getty architecture'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning studio tour (Warner Bros/Universal)',
                        'Last meal at Grand Central Market',
                        'Visit The Broad museum',
                        'Depart from LAX'
                    ],
                    'highlight': 'Studio backlot tour'
                }
            ]
        },
        'rio_de_janeiro': {
            'name': 'Rio de Janeiro',
            'tagline': 'Cidade Maravilhosa',
            'duration': '5 Days',
            'image_path': 'images/rio.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Christ the Redeemer',
                    'activities': [
                        'Arrive in Rio and check in',
                        'Visit Christ the Redeemer',
                        'Explore Santa Teresa',
                        'Evening samba show'
                    ],
                    'highlight': 'Christ statue sunset views'
                },
                {
                    'day': 2,
                    'title': 'Beach Day',
                    'activities': [
                        'Morning at Copacabana Beach',
                        'Afternoon at Ipanema Beach',
                        'Sunset at Arpoador Rock',
                        'Evening caipirinha tasting'
                    ],
                    'highlight': 'Ipanema beach culture'
                },
                {
                    'day': 3,
                    'title': 'Nature & Views',
                    'activities': [
                        'Cable car up Sugarloaf Mountain',
                        'Visit Botanical Gardens',
                        'Hike in Tijuca Forest',
                        'Evening in Lapa'
                    ],
                    'highlight': 'Sugarloaf sunset'
                },
                {
                    'day': 4,
                    'title': 'Favela Culture',
                    'activities': [
                        'Responsible favela tour',
                        'Visit Selarón Steps',
                        'Explore downtown Rio',
                        'Evening churrascaria dinner'
                    ],
                    'highlight': 'Colorful Selarón Steps'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Parque Lage',
                        'Last minute shopping',
                        'Final feijoada lunch',
                        'Depart from Rio'
                    ],
                    'highlight': 'Parque Lage mansion'
                }
            ]
        },
        'toronto': {
            'name': 'Toronto',
            'tagline': 'Diverse City',
            'duration': '3 Days',
            'image_path': 'images/toronto.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Downtown',
                    'activities': [
                        'Arrive and check into downtown hotel',
                        'Visit CN Tower (EdgeWalk optional)',
                        'Explore Ripley\'s Aquarium',
                        'Evening in Distillery District'
                    ],
                    'highlight': 'CN Tower glass floor'
                },
                {
                    'day': 2,
                    'title': 'Island & Neighborhoods',
                    'activities': [
                        'Ferry to Toronto Islands',
                        'Bike rental on Ward\'s Island',
                        'Afternoon in Kensington Market',
                        'Dinner in Chinatown'
                    ],
                    'highlight': 'Island skyline views'
                },
                {
                    'day': 3,
                    'title': 'Culture & Departure',
                    'activities': [
                        'Visit Royal Ontario Museum',
                        'Stroll through High Park',
                        'Shop at St. Lawrence Market',
                        'Depart from Toronto'
                    ],
                    'highlight': 'ROM crystal addition'
                }
            ]
        },
        'marrakech': {
            'name': 'Marrakech',
            'tagline': 'Red City',
            'duration': '3 Days',
            'image_path': 'images/marrakech.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Medina',
                    'activities': [
                        'Arrive and check into riad',
                        'Explore Jemaa el-Fnaa square',
                        'Visit Koutoubia Mosque',
                        'Evening street food tasting'
                    ],
                    'highlight': 'Snake charmers in square'
                },
                {
                    'day': 2,
                    'title': 'Historic Sites',
                    'activities': [
                        'Visit Bahia Palace',
                        'Explore Saadian Tombs',
                        'Afternoon at Majorelle Garden',
                        'Evening hammam spa'
                    ],
                    'highlight': 'Majorelle blue walls'
                },
                {
                    'day': 3,
                    'title': 'Atlas Mountains & Departure',
                    'activities': [
                        'Day trip to Ourika Valley',
                        'Visit Berber village',
                        'Last minute souk shopping',
                        'Depart from Marrakech'
                    ],
                    'highlight': 'Atlas mountain tea break'
                }
            ]
        },
        'victoria_falls': {
            'name': 'Victoria Falls',
            'tagline': 'The Smoke That Thunders',
            'duration': '2 Days',
            'image_path': 'images/victoria_falls.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Zimbabwe Side',
                    'activities': [
                        'Arrive and check into safari lodge',
                        'Walking tour of the falls',
                        'Visit Devil\'s Pool (dry season)',
                        'Sunset cruise on Zambezi'
                    ],
                    'highlight': 'Main Falls viewpoint'
                },
                {
                    'day': 2,
                    'title': 'Zambia Side & Departure',
                    'activities': [
                        'Walk across Victoria Falls Bridge',
                        'Visit Livingstone Island',
                        'Helicopter flight (optional)',
                        'Depart from Victoria Falls'
                    ],
                    'highlight': 'Flight of Angels helicopter tour'
                }
            ]
        },
        'maasai_mara': {
            'name': 'Maasai Mara',
            'tagline': 'African Safari Adventure',
            'duration': '3 Days',
            'image_path': 'images/maasai_mara.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Evening Safari',
                    'activities': [
                        'Fly from Nairobi to Mara',
                        'Check into safari camp',
                        'Evening game drive',
                        'Campfire under the stars'
                    ],
                    'highlight': 'First wildlife sightings'
                },
                {
                    'day': 2,
                    'title': 'Full Day Safari',
                    'activities': [
                        'Sunrise game drive',
                        'Visit Mara River',
                        'Picnic lunch in the bush',
                        'Maasai village visit'
                    ],
                    'highlight': 'Big Five spotting'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning balloon safari (optional)',
                        'Final game drive',
                        'Fly back to Nairobi',
                        'Connect to onward flight'
                    ],
                    'highlight': 'Hot air balloon over savanna'
                }
            ]
        },
        'bora_bora': {
            'name': 'Bora Bora',
            'tagline': 'Pacific Paradise',
            'duration': '5 Days',
            'image_path': 'images/bora_bora.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Overwater Bungalow',
                    'activities': [
                        'Arrive by inter-island flight',
                        'Boat transfer to resort',
                        'Check into overwater bungalow',
                        'Evening lagoon swim'
                    ],
                    'highlight': 'First view of Mount Otemanu'
                },
                {
                    'day': 2,
                    'title': 'Lagoon Exploration',
                    'activities': [
                        'Snorkel at Coral Gardens',
                        'Swim with rays & sharks',
                        'Private beach picnic',
                        'Polynesian dance show'
                    ],
                    'highlight': 'Stingray encounter'
                },
                {
                    'day': 3,
                    'title': 'Island Tour',
                    'activities': [
                        '4x4 island safari',
                        'Visit WWII cannons',
                        'Bloody Mary\'s lunch',
                        'Sunset catamaran cruise'
                    ],
                    'highlight': 'Viewpoints tour'
                },
                {
                    'day': 4,
                    'title': 'Relaxation Day',
                    'activities': [
                        'Spa treatment over water',
                        'Stand-up paddleboarding',
                        'Private sunset dinner',
                        'Stargazing from deck'
                    ],
                    'highlight': 'Overwater spa'
                },
                {
                    'day': 5,
                    'title': 'Departure',
                    'activities': [
                        'Final lagoon swim',
                        'Resort relaxation',
                        'Boat transfer to airport',
                        'Depart from Bora Bora'
                    ],
                    'highlight': 'Last tropical sunrise'
                }
            ]
        },
        'cairo': {
            'name': 'Cairo',
            'tagline': 'Gateway to the Pyramids',
            'duration': '4 Days',
            'image_path': 'images/cairo.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Giza Plateau',
                    'activities': [
                        'Arrive and check into Nile-view hotel',
                        'Visit Great Pyramids & Sphinx',
                        'Solar Boat Museum',
                        'Sound & Light show at night'
                    ],
                    'highlight': 'Pyramid photo ops'
                },
                {
                    'day': 2,
                    'title': 'Egyptian Museum & Old Cairo',
                    'activities': [
                        'Tour Egyptian Museum',
                        'Visit Tahrir Square',
                        'Explore Coptic Cairo',
                        'Khan el-Khalili bazaar'
                    ],
                    'highlight': 'King Tut\'s golden mask'
                },
                {
                    'day': 3,
                    'title': 'Saqqara & Memphis',
                    'activities': [
                        'Day trip to Step Pyramid',
                        'Visit ancient Memphis',
                        'See Dahshur pyramids',
                        'Nile dinner cruise'
                    ],
                    'highlight': 'Bent Pyramid'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning at Citadel of Saladin',
                        'Visit Alabaster Mosque',
                        'Final Egyptian coffee',
                        'Depart from Cairo'
                    ],
                    'highlight': 'City views from Citadel'
                }
            ]
        }
    }
    
    destination = destination_data.get(destination_slug, {})
    return render(request, 'International/destination_detail_inter.html', {'destination': destination})

# kerala
from django.shortcuts import render

def kerala(request):
    return render(request, 'kerala/domestic_kerala.html')

def all_kerala(request):
    return render(request, 'kerala/all_kerala.html')

def destination_kerala(request, destination_slug):
    # Complete destination data for all 30 Kerala destinations
    destination_data = {
        'alleppey': {
            'name': 'Alleppey',
            'tagline': 'Venice of the East',
            'duration': '3 Days',
            'image_path': 'images/alleppey.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Backwater Cruise',
                    'activities': [
                        'Arrive in Alleppey and check into your houseboat',
                        'Begin backwater cruise through palm-fringed canals',
                        'Enjoy traditional Kerala lunch on board',
                        'Evening relaxation on the houseboat deck'
                    ],
                    'highlight': 'Sunset views from the houseboat'
                },
                {
                    'day': 2,
                    'title': 'Village Life & Canoe Ride',
                    'activities': [
                        'Morning village walk to see coir-making and fishing',
                        'Traditional Kerala breakfast at a local home',
                        'Afternoon canoe ride through narrow canals',
                        'Visit to Kumarakom Bird Sanctuary'
                    ],
                    'highlight': 'Village canoe experience'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Alleppey Beach',
                        'Explore local markets for spices and crafts',
                        'Depart from Alleppey'
                    ],
                    'highlight': 'Beach walk and shopping'
                }
            ]
        },
        'munnar': {
            'name': 'Munnar',
            'tagline': 'Kashmir of South India',
            'duration': '4 Days',
            'image_path': 'images/munnar.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Tea Gardens',
                    'activities': [
                        'Arrive in Munnar and check into your resort',
                        'Visit Tea Museum to learn about tea processing',
                        'Walk through lush tea plantations',
                        'Evening at leisure'
                    ],
                    'highlight': 'Tea plantation walk'
                },
                {
                    'day': 2,
                    'title': 'Nature Exploration',
                    'activities': [
                        'Morning visit to Eravikulam National Park',
                        'See Attukad Waterfalls',
                        'Visit Mattupetty Dam',
                        'Evening shopping for tea and spices'
                    ],
                    'highlight': 'Spotting Nilgiri Tahr at Eravikulam'
                },
                {
                    'day': 3,
                    'title': 'Echo Point & Top Station',
                    'activities': [
                        'Visit Echo Point and Kundala Lake',
                        'Boat ride on the lake',
                        'Excursion to Top Station for panoramic views',
                        'Evening Ayurvedic massage'
                    ],
                    'highlight': 'Views from Top Station'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Pothamedu Viewpoint',
                        'Last minute shopping',
                        'Depart from Munnar'
                    ],
                    'highlight': 'Final views of tea gardens'
                }
            ]
        },
        'kochi': {
            'name': 'Kochi',
            'tagline': 'Queen of Arabian Sea',
            'duration': '3 Days',
            'image_path': 'images/kochi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Fort Kochi',
                    'activities': [
                        'Arrive in Kochi and check into your hotel',
                        'Visit Chinese fishing nets at sunset',
                        'Walk through Jew Town and spice markets',
                        'Kathakali dance performance in evening'
                    ],
                    'highlight': 'Chinese fishing nets at sunset'
                },
                {
                    'day': 2,
                    'title': 'Historical Exploration',
                    'activities': [
                        'Visit St. Francis Church and Santa Cruz Basilica',
                        'Explore Mattancherry Palace',
                        'Afternoon cruise to Bolgatty Palace',
                        'Evening at Marine Drive'
                    ],
                    'highlight': 'Jewish Synagogue visit'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Cherai Beach',
                        'Explore local art galleries',
                        'Depart from Kochi'
                    ],
                    'highlight': 'Beach relaxation'
                }
            ]
        },
        'kovalam': {
            'name': 'Kovalam',
            'tagline': 'Beach Paradise',
            'duration': '3 Days',
            'image_path': 'images/kovalam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Beach Relaxation',
                    'activities': [
                        'Arrive in Kovalam and check into beach resort',
                        'Relax at Lighthouse Beach',
                        'Evening Ayurvedic massage',
                        'Seafood dinner by the beach'
                    ],
                    'highlight': 'First sunset at Kovalam'
                },
                {
                    'day': 2,
                    'title': 'Beach Activities',
                    'activities': [
                        'Morning yoga session on the beach',
                        'Try surfing or swimming',
                        'Visit nearby Vizhinjam Fishing Harbor',
                        'Evening shopping for handicrafts'
                    ],
                    'highlight': 'Beach yoga experience'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Padmanabhaswamy Temple',
                        'Final beach walk',
                        'Depart from Kovalam'
                    ],
                    'highlight': 'Temple visit'
                }
            ]
        },
        'thekkady': {
            'name': 'Thekkady',
            'tagline': 'Wildlife Haven',
            'duration': '3 Days',
            'image_path': 'images/thekkady.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Jungle Safari',
                    'activities': [
                        'Arrive in Thekkady and check into jungle resort',
                        'Afternoon boat safari on Periyar Lake',
                        'Evening spice plantation tour',
                        'Traditional Kalaripayattu performance'
                    ],
                    'highlight': 'Boat safari spotting wildlife'
                },
                {
                    'day': 2,
                    'title': 'Nature Walk & Elephant Ride',
                    'activities': [
                        'Morning guided nature walk in the forest',
                        'Elephant ride experience',
                        'Visit to local tribal village',
                        'Evening at leisure'
                    ],
                    'highlight': 'Elephant interaction'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Chellarkovil viewpoint',
                        'Purchase spices and tea',
                        'Depart from Thekkady'
                    ],
                    'highlight': 'Final jungle views'
                }
            ]
        },
        'varkala': {
            'name': 'Varkala',
            'tagline': 'Cliffside Serenity',
            'duration': '3 Days',
            'image_path': 'images/varkala.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Cliff Walk',
                    'activities': [
                        'Arrive in Varkala and check into cliff resort',
                        'Walk along the cliffside promenade',
                        'Sunset viewing from North Cliff',
                        'Evening beachside dining'
                    ],
                    'highlight': 'Cliffside sunset'
                },
                {
                    'day': 2,
                    'title': 'Beach Day & Temple Visit',
                    'activities': [
                        'Morning yoga session on the beach',
                        'Visit Janardanaswamy Temple',
                        'Relax at Papanasam Beach',
                        'Evening Ayurvedic treatment'
                    ],
                    'highlight': 'Beach yoga'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Kappil Lake',
                        'Final beach walk',
                        'Depart from Varkala'
                    ],
                    'highlight': 'Lake views'
                }
            ]
        },
        'wayanad': {
            'name': 'Wayanad',
            'tagline': 'Green Paradise',
            'duration': '4 Days',
            'image_path': 'images/wayanad.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Nature Introduction',
                    'activities': [
                        'Arrive in Wayanad and check into eco-resort',
                        'Visit Banasura Sagar Dam',
                        'Walk through spice plantations',
                        'Evening tribal dance performance'
                    ],
                    'highlight': 'Dam views'
                },
                {
                    'day': 2,
                    'title': 'Waterfalls & Caves',
                    'activities': [
                        'Visit Soochipara Waterfalls',
                        'Explore Edakkal Caves',
                        'Afternoon at Kuruva Island',
                        'Evening at leisure'
                    ],
                    'highlight': 'Ancient cave carvings'
                },
                {
                    'day': 3,
                    'title': 'Wildlife & Plantations',
                    'activities': [
                        'Morning safari at Muthanga Wildlife Sanctuary',
                        'Visit coffee and pepper plantations',
                        'Evening visit to Pookode Lake'
                    ],
                    'highlight': 'Wildlife spotting'
                },
                {
                    'day': 4,
                    'title': 'Departure',
                    'activities': [
                        'Morning trek to Chembra Peak (optional)',
                        'Purchase organic spices',
                        'Depart from Wayanad'
                    ],
                    'highlight': 'Final mountain views'
                }
            ]
        },
        'bekal': {
            'name': 'Bekal',
            'tagline': 'Historic Seaside Fort',
            'duration': '2 Days',
            'image_path': 'images/bekal.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Fort Exploration',
                    'activities': [
                        'Arrive in Bekal and check into resort',
                        'Explore Bekal Fort with sea views',
                        'Walk along Bekal Beach',
                        'Evening cultural performance'
                    ],
                    'highlight': 'Fort views at sunset'
                },
                {
                    'day': 2,
                    'title': 'Backwater Cruise & Departure',
                    'activities': [
                        'Morning backwater cruise in Valiyaparamba',
                        'Visit nearby Kappil Beach',
                        'Depart from Bekal'
                    ],
                    'highlight': 'Backwater experience'
                }
            ]
        },
        'kumarakom': {
            'name': 'Kumarakom',
            'tagline': 'Backwater Bliss',
            'duration': '2 Days',
            'image_path': 'images/kumarakom.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Backwater Experience',
                    'activities': [
                        'Arrive in Kumarakom and check into houseboat',
                        'Backwater cruise through Vembanad Lake',
                        'Visit Kumarakom Bird Sanctuary',
                        'Evening relaxation on houseboat'
                    ],
                    'highlight': 'Bird watching'
                },
                {
                    'day': 2,
                    'title': 'Village Visit & Departure',
                    'activities': [
                        'Morning canoe ride through narrow canals',
                        'Visit local village to see coir-making',
                        'Depart from Kumarakom'
                    ],
                    'highlight': 'Village canoe experience'
                }
            ]
        },
        'trivandrum': {
            'name': 'Trivandrum',
            'tagline': 'Capital City',
            'duration': '2 Days',
            'image_path': 'images/trivandrum.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & City Tour',
                    'activities': [
                        'Arrive in Trivandrum and check into hotel',
                        'Visit Padmanabhaswamy Temple',
                        'Explore Napier Museum and Zoo',
                        'Evening at Kovalam Beach'
                    ],
                    'highlight': 'Temple visit'
                },
                {
                    'day': 2,
                    'title': 'Cultural Sites & Departure',
                    'activities': [
                        'Visit Kuthiramalika Palace',
                        'Explore Chalai Market',
                        'Depart from Trivandrum'
                    ],
                    'highlight': 'Palace tour'
                }
            ]
        },
        'athirappilly': {
            'name': 'Athirappilly',
            'tagline': 'Niagara of India',
            'duration': '2 Days',
            'image_path': 'images/athirappilly.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Waterfall Experience',
                    'activities': [
                        'Arrive in Athirappilly and check into resort',
                        'Visit Athirappilly Waterfalls',
                        'Trek to Vazhachal Waterfalls',
                        'Evening nature walk'
                    ],
                    'highlight': 'Waterfall views'
                },
                {
                    'day': 2,
                    'title': 'Jungle Safari & Departure',
                    'activities': [
                        'Morning jungle safari in Sholayar ranges',
                        'Visit tribal village',
                        'Depart from Athirappilly'
                    ],
                    'highlight': 'Wildlife spotting'
                }
            ]
        },
        'kannur': {
            'name': 'Kannur',
            'tagline': 'Land of Theyyam',
            'duration': '3 Days',
            'image_path': 'images/kannur.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Beach Exploration',
                    'activities': [
                        'Arrive in Kannur and check into hotel',
                        'Visit Payyambalam Beach',
                        'Explore St. Angelo Fort',
                        'Evening Theyyam performance (seasonal)'
                    ],
                    'highlight': 'Fort views'
                },
                {
                    'day': 2,
                    'title': 'Cultural Heritage',
                    'activities': [
                        'Visit Muzhappilangad Drive-in Beach',
                        'Explore Arakkal Museum',
                        'See traditional loom weaving',
                        'Evening at local markets'
                    ],
                    'highlight': 'Drive-in beach experience'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to Parassinikadavu Temple',
                        'Final beach walk',
                        'Depart from Kannur'
                    ],
                    'highlight': 'Temple visit'
                }
            ]
        },
        'poovar': {
            'name': 'Poovar',
            'tagline': 'Golden Island',
            'duration': '2 Days',
            'image_path': 'images/poovar.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Island Exploration',
                    'activities': [
                        'Arrive in Poovar and check into island resort',
                        'Boat cruise through backwaters to golden beach',
                        'Visit floating restaurants',
                        'Evening Ayurvedic massage'
                    ],
                    'highlight': 'Golden beach sunset'
                },
                {
                    'day': 2,
                    'title': 'Village Visit & Departure',
                    'activities': [
                        'Morning visit to fishing village',
                        'Explore local handicrafts',
                        'Depart from Poovar'
                    ],
                    'highlight': 'Village experience'
                }
            ]
        },
        'guruvayur': {
            'name': 'Guruvayur',
            'tagline': 'Temple Town',
            'duration': '2 Days',
            'image_path': 'images/guruvayur.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Temple Visit',
                    'activities': [
                        'Arrive in Guruvayur and check into hotel',
                        'Visit Guruvayur Temple',
                        'See Punnathur Kotta Elephant Sanctuary',
                        'Evening temple rituals'
                    ],
                    'highlight': 'Temple darshan'
                },
                {
                    'day': 2,
                    'title': 'Cultural Sites & Departure',
                    'activities': [
                        'Morning visit to Mammiyur Temple',
                        'Explore local markets',
                        'Depart from Guruvayur'
                    ],
                    'highlight': 'Elephant sanctuary'
                }
            ]
        },
        'idukki': {
            'name': 'Idukki',
            'tagline': 'Spice Garden of Kerala',
            'duration': '3 Days',
            'image_path': 'images/idukki.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Dam Visit',
                    'activities': [
                        'Arrive in Idukki and check into resort',
                        'Visit Idukki Arch Dam',
                        'Explore Hill View Park',
                        'Evening spice market visit'
                    ],
                    'highlight': 'Dam views'
                },
                {
                    'day': 2,
                    'title': 'Wildlife & Nature',
                    'activities': [
                        'Morning trek in Periyar National Park',
                        'Visit Thommankuthu Waterfalls',
                        'Evening campfire at resort'
                    ],
                    'highlight': 'Waterfall trek'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning visit to tea plantations',
                        'Purchase fresh spices',
                        'Depart from Idukki'
                    ],
                    'highlight': 'Plantation walk'
                }
            ]
        },
        'kollam': {
            'name': 'Kollam',
            'tagline': 'Gateway to Backwaters',
            'duration': '2 Days',
            'image_path': 'images/kollam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Backwater Cruise',
                    'activities': [
                        'Arrive in Kollam and check into houseboat',
                        'Ashtamudi Lake backwater cruise',
                        'Visit Munroe Island',
                        'Evening seafood dinner'
                    ],
                    'highlight': 'Houseboat stay'
                },
                {
                    'day': 2,
                    'title': 'Beach & Departure',
                    'activities': [
                        'Morning visit to Thangassery Beach',
                        'Explore Portuguese ruins',
                        'Depart from Kollam'
                    ],
                    'highlight': 'Beach walk'
                }
            ]
        },
        'ashtamudi': {
            'name': 'Ashtamudi',
            'tagline': 'Palm-fringed Lake',
            'duration': '2 Days',
            'image_path': 'images/ashtamudi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Lake Cruise',
                    'activities': [
                        'Arrive in Ashtamudi and check into lake resort',
                        'Boat cruise on Ashtamudi Lake',
                        'Visit coconut villages',
                        'Evening kayaking'
                    ],
                    'highlight': 'Lake sunset'
                },
                {
                    'day': 2,
                    'title': 'Village Tour & Departure',
                    'activities': [
                        'Morning village walk',
                        'See traditional fishing methods',
                        'Depart from Ashtamudi'
                    ],
                    'highlight': 'Village experience'
                }
            ]
        },
        'marari': {
            'name': 'Marari',
            'tagline': 'Quiet Fishing Village',
            'duration': '2 Days',
            'image_path': 'images/marari.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Beach Relaxation',
                    'activities': [
                        'Arrive in Marari and check into beach resort',
                        'Relax at Marari Beach',
                        'Visit local fishing village',
                        'Evening seafood dinner'
                    ],
                    'highlight': 'Beach sunset'
                },
                {
                    'day': 2,
                    'title': 'Departure',
                    'activities': [
                        'Morning yoga on the beach',
                        'Final beach walk',
                        'Depart from Marari'
                    ],
                    'highlight': 'Beach yoga'
                }
            ]
        },
        'neyyar': {
            'name': 'Neyyar',
            'tagline': 'Wildlife & Dam',
            'duration': '2 Days',
            'image_path': 'images/neyyar.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Wildlife Safari',
                    'activities': [
                        'Arrive in Neyyar and check into resort',
                        'Safari in Neyyar Wildlife Sanctuary',
                        'Visit Lion Safari Park',
                        'Evening dam views'
                    ],
                    'highlight': 'Wildlife spotting'
                },
                {
                    'day': 2,
                    'title': 'Nature Walk & Departure',
                    'activities': [
                        'Morning trek to Agasthyakoodam viewpoint',
                        'Visit crocodile farm',
                        'Depart from Neyyar'
                    ],
                    'highlight': 'Mountain views'
                }
            ]
        },
        'silent-valley': {
            'name': 'Silent Valley',
            'tagline': 'Pristine Rainforest',
            'duration': '3 Days',
            'image_path': 'images/silent-valley.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Park Introduction',
                    'activities': [
                        'Arrive near Silent Valley and check into eco-lodge',
                        'Guided nature walk in buffer zone',
                        'Evening documentary about the park'
                    ],
                    'highlight': 'First rainforest experience'
                },
                {
                    'day': 2,
                    'title': 'Deep Jungle Exploration',
                    'activities': [
                        'Full-day guided trek with packed lunch',
                        'Visit Sairandhri viewpoint',
                        'Evening discussion with naturalists'
                    ],
                    'highlight': 'Rainforest trek'
                },
                {
                    'day': 3,
                    'title': 'Departure',
                    'activities': [
                        'Morning bird watching session',
                        'Visit tribal village (if permitted)',
                        'Depart from Silent Valley'
                    ],
                    'highlight': 'Bird spotting'
                }
            ]
        },
        'ponmudi': {
            'name': 'Ponmudi',
            'tagline': 'Golden Peak',
            'duration': '2 Days',
            'image_path': 'images/ponmudi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Hill Station Tour',
                    'activities': [
                        'Arrive in Ponmudi and check into resort',
                        'Visit Golden Valley',
                        'Trek to Varayadumotta peak',
                        'Evening campfire'
                    ],
                    'highlight': 'Mountain views'
                },
                {
                    'day': 2,
                    'title': 'Nature Walk & Departure',
                    'activities': [
                        'Morning butterfly safari',
                        'Visit tea estates',
                        'Depart from Ponmudi'
                    ],
                    'highlight': 'Butterfly spotting'
                }
            ]
        },
        'cherai': {
            'name': 'Cherai',
            'tagline': 'Golden Beach',
            'duration': '2 Days',
            'image_path': 'images/cherai.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Beach Day',
                    'activities': [
                        'Arrive in Cherai and check into beach resort',
                        'Relax at Cherai Beach',
                        'Visit local fishing village',
                        'Evening seafood barbecue'
                    ],
                    'highlight': 'Beach sunset'
                },
                {
                    'day': 2,
                    'title': 'Backwater Cruise & Departure',
                    'activities': [
                        'Morning backwater cruise',
                        'Visit Munambam Harbour',
                        'Depart from Cherai'
                    ],
                    'highlight': 'Backwater experience'
                }
            ]
        },
        'thrissur': {
            'name': 'Thrissur',
            'tagline': 'Cultural Capital',
            'duration': '2 Days',
            'image_path': 'images/thrissur.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Cultural Tour',
                    'activities': [
                        'Arrive in Thrissur and check into hotel',
                        'Visit Vadakkunnathan Temple',
                        'Explore Kerala Kalamandalam',
                        'Evening cultural show'
                    ],
                    'highlight': 'Temple visit'
                },
                {
                    'day': 2,
                    'title': 'Heritage Sites & Departure',
                    'activities': [
                        'Visit Athirapally Waterfalls',
                        'See Shakthan Thampuran Palace',
                        'Depart from Thrissur'
                    ],
                    'highlight': 'Waterfall visit'
                }
            ]
        },
        'parambikulam': {
            'name': 'Parambikulam',
            'tagline': 'Tiger Reserve',
            'duration': '3 Days',
            'image_path': 'images/parambikulam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Jungle Introduction',
                    'activities': [
                        'Arrive in Parambikulam and check into forest lodge',
                        'Evening safari in buffer zone',
                        'Night campfire with naturalist talk'
                    ],
                    'highlight': 'First wildlife experience'
                },
                {
                    'day': 2,
                    'title': 'Full Day Safari',
                    'activities': [
                        'Morning and afternoon jungle safaris',
                        'Boat ride on Parambikulam Reservoir',
                        'Visit tribal colony'
                    ],
                    'highlight': 'Tiger spotting chance'
                },
                {
                    'day': 3,
                    'title': 'Nature Walk & Departure',
                    'activities': [
                        'Morning bird watching trek',
                        'Visit teak plantations',
                        'Depart from Parambikulam'
                    ],
                    'highlight': 'Bird watching'
                }
            ]
        },
        'neyyattinkara': {
            'name': 'Neyyattinkara',
            'tagline': 'Traditional Crafts',
            'duration': '1 Day',
            'image_path': 'images/neyyattinkara.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Craft Village Tour',
                    'activities': [
                        'Arrive in Neyyattinkara',
                        'Visit traditional craft workshops',
                        'See wood carving and metal work',
                        'Explore local markets'
                    ],
                    'highlight': 'Craft demonstrations'
                }
            ]
        },
        'alappuzha': {
            'name': 'Alappuzha',
            'tagline': 'Backwater Hub',
            'duration': '2 Days',
            'image_path': 'images/alappuzha.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Canal Cruise',
                    'activities': [
                        'Arrive in Alappuzha and check into houseboat',
                        'Canal cruise through backwaters',
                        'Visit Pathiramanal Island',
                        'Evening onboard relaxation'
                    ],
                    'highlight': 'Houseboat stay'
                },
                {
                    'day': 2,
                    'title': 'Beach & Departure',
                    'activities': [
                        'Morning visit to Alappuzha Beach',
                        'See lighthouse and pier',
                        'Depart from Alappuzha'
                    ],
                    'highlight': 'Beach walk'
                }
            ]
        },
        'malampuzha': {
            'name': 'Malampuzha',
            'tagline': 'Garden & Dam',
            'duration': '1 Day',
            'image_path': 'images/malampuzha.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Gardens & Dam Visit',
                    'activities': [
                        'Arrive in Malampuzha',
                        'Explore Malampuzha Gardens',
                        'Visit Rock Garden and Fantasy Park',
                        'See Malampuzha Dam'
                    ],
                    'highlight': 'Garden sculptures'
                }
            ]
        },
        'palakkad': {
            'name': 'Palakkad',
            'tagline': 'Gateway to Kerala',
            'duration': '2 Days',
            'image_path': 'images/palakkad.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Fort Visit',
                    'activities': [
                        'Arrive in Palakkad and check into hotel',
                        'Visit Palakkad Fort',
                        'Explore Jain Temple',
                        'Evening at Malampuzha Gardens'
                    ],
                    'highlight': 'Fort history'
                },
                {
                    'day': 2,
                    'title': 'Nature & Departure',
                    'activities': [
                        'Morning visit to Silent Valley viewpoint',
                        'Explore Dhoni waterfalls',
                        'Depart from Palakkad'
                    ],
                    'highlight': 'Waterfall visit'
                }
            ]
        },
        'kuttanad': {
            'name': 'Kuttanad',
            'tagline': 'Rice Bowl of Kerala',
            'duration': '2 Days',
            'image_path': 'images/kuttanad.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Backwater Experience',
                    'activities': [
                        'Arrive in Kuttanad and check into houseboat',
                        'Cruise through paddy fields',
                        'Visit local farming communities',
                        'Evening onboard relaxation'
                    ],
                    'highlight': 'Unique below-sea-level farming'
                },
                {
                    'day': 2,
                    'title': 'Village Tour & Departure',
                    'activities': [
                        'Morning canoe ride through narrow canals',
                        'See traditional farming techniques',
                        'Depart from Kuttanad'
                    ],
                    'highlight': 'Canoe experience'
                }
            ]
        },
        'sabarimala': {
            'name': 'Sabarimala',
            'tagline': 'Sacred Pilgrimage',
            'duration': '3 Days',
            'image_path': 'images/sabarimala.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Trek Preparation',
                    'activities': [
                        'Arrive at base camp and check accommodations',
                        'Complete pilgrimage formalities',
                        'Evening spiritual discourse'
                    ],
                    'highlight': 'Pilgrimage atmosphere'
                },
                {
                    'day': 2,
                    'title': 'Pilgrimage Trek',
                    'activities': [
                        'Early morning start for forest trek',
                        'Reach Sabarimala Temple by evening',
                        'Participate in temple rituals'
                    ],
                    'highlight': 'Temple darshan'
                },
                {
                    'day': 3,
                    'title': 'Return Journey',
                    'activities': [
                        'Morning rituals at temple',
                        'Begin return trek',
                        'Depart from base camp'
                    ],
                    'highlight': 'Spiritual experience'
                }
            ]
        }
    }
    
    destination = destination_data.get(destination_slug, {})
    return render(request, 'kerala/destination_kerala.html', {'destination': destination})

#karnataka

def karnataka(request):
    return render(request, 'karnataka/domestic_karnataka.html')

def all_karnataka(request):
    return render(request, 'karnataka/all_karnataka.html')

def destination_karnataka(request, destination_slug):
    # Complete destination data for all 30 Kerala destinations
  destination_data = {
    'bangalore': {
        'name': 'Bangalore',
        'tagline': 'Silicon Valley of India',
        'duration': '3 Days',
        'image_path': 'images/bangalore.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & City Tour',
                'activities': [
                    'Arrive in Bangalore and check into hotel',
                    'Visit Lalbagh Botanical Garden',
                    'Explore Cubbon Park',
                    'Evening at MG Road and Brigade Road'
                ],
                'highlight': 'Lalbagh Glass House'
            },
            {
                'day': 2,
                'title': 'Historical Exploration',
                'activities': [
                    'Visit Bangalore Palace',
                    'See Tipu Sultan\'s Summer Palace',
                    'Explore Vidhana Soudha',
                    'Evening at UB City Mall'
                ],
                'highlight': 'Bangalore Palace tour'
            },
            {
                'day': 3,
                'title': 'Technology & Departure',
                'activities': [
                    'Visit ISKCON Temple',
                    'Tour Visvesvaraya Industrial Museum',
                    'Explore Innovative Film City',
                    'Depart from Bangalore'
                ],
                'highlight': 'ISKCON Temple'
            }
        ]
    },
    'mysore': {
        'name': 'Mysore',
        'tagline': 'City of Palaces',
        'duration': '3 Days',
        'image_path': 'images/mysore.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Palace Tour',
                'activities': [
                    'Arrive in Mysore and check into hotel',
                    'Visit Mysore Palace (illuminated in evening)',
                    'Explore Devaraja Market',
                    'Evening at Brindavan Gardens'
                ],
                'highlight': 'Palace illumination'
            },
            {
                'day': 2,
                'title': 'Cultural Exploration',
                'activities': [
                    'Morning at Chamundi Hill',
                    'Visit St. Philomena\'s Church',
                    'Explore Jaganmohan Palace Art Gallery',
                    'Evening shopping for sandalwood'
                ],
                'highlight': 'Chamundi Hill view'
            },
            {
                'day': 3,
                'title': 'Nature & Departure',
                'activities': [
                    'Visit Ranganathittu Bird Sanctuary',
                    'Tour Srirangapatna historical sites',
                    'Depart from Mysore'
                ],
                'highlight': 'Bird watching'
            }
        ]
    },
    'coorg': {
        'name': 'Coorg',
        'tagline': 'Scotland of India',
        'duration': '4 Days',
        'image_path': 'images/coorg.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Plantation Tour',
                'activities': [
                    'Arrive in Coorg and check into plantation stay',
                    'Coffee plantation walk',
                    'Visit Raja\'s Seat for sunset',
                    'Evening campfire'
                ],
                'highlight': 'Coffee tasting'
            },
            {
                'day': 2,
                'title': 'Waterfalls & Nature',
                'activities': [
                    'Visit Abbey Falls',
                    'Explore Dubare Elephant Camp',
                    'Trek to Mandalpatti viewpoint',
                    'Evening local cuisine tasting'
                ],
                'highlight': 'Elephant interaction'
            },
            {
                'day': 3,
                'title': 'Cultural Sites',
                'activities': [
                    'Visit Omkareshwara Temple',
                    'Explore Madikeri Fort',
                    'Tour Tibetan Golden Temple',
                    'Evening shopping for spices'
                ],
                'highlight': 'Tibetan culture'
            },
            {
                'day': 4,
                'title': 'Departure',
                'activities': [
                    'Morning nature walk',
                    'Purchase coffee and honey',
                    'Depart from Coorg'
                ],
                'highlight': 'Final mountain views'
            }
        ]
    },
    'hampi': {
        'name': 'Hampi',
        'tagline': 'Ruins of Vijayanagara Empire',
        'duration': '3 Days',
        'image_path': 'images/hampi.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Temple Tour',
                'activities': [
                    'Arrive in Hampi and check into heritage stay',
                    'Visit Virupaksha Temple',
                    'Explore Hampi Bazaar',
                    'Sunset at Hemakuta Hill'
                ],
                'highlight': 'Temple elephant'
            },
            {
                'day': 2,
                'title': 'Royal Center Exploration',
                'activities': [
                    'Visit Vittala Temple (stone chariot)',
                    'Explore Lotus Mahal and Elephant Stables',
                    'See Queen\'s Bath and Royal Enclosure',
                    'Evening coracle ride on Tungabhadra'
                ],
                'highlight': 'Stone chariot'
            },
            {
                'day': 3,
                'title': 'Departure',
                'activities': [
                    'Morning visit to Anegundi village',
                    'See Sanapur Lake and dam',
                    'Depart from Hampi'
                ],
                'highlight': 'Village experience'
            }
        ]
    },
    'gokarna': {
        'name': 'Gokarna',
        'tagline': 'Peaceful Beach Town',
        'duration': '3 Days',
        'image_path': 'images/gokarna.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Temple Visit',
                'activities': [
                    'Arrive in Gokarna and check into beach hut',
                    'Visit Mahabaleshwara Temple',
                    'Relax at Kudle Beach',
                    'Evening seafood dinner'
                ],
                'highlight': 'Temple atmosphere'
            },
            {
                'day': 2,
                'title': 'Beach Hopping',
                'activities': [
                    'Trek to Om Beach',
                    'Visit Half Moon and Paradise Beaches',
                    'Sunset at Gokarna Beach',
                    'Evening beachside music'
                ],
                'highlight': 'Om Beach shape'
            },
            {
                'day': 3,
                'title': 'Departure',
                'activities': [
                    'Morning yoga on the beach',
                    'Final swim in the sea',
                    'Depart from Gokarna'
                ],
                'highlight': 'Beach yoga'
            }
        ]
    },
    'badami': {
        'name': 'Badami',
        'tagline': 'Ancient Cave Temples',
        'duration': '2 Days',
        'image_path': 'images/badami.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Cave Exploration',
                'activities': [
                    'Arrive in Badami and check into hotel',
                    'Explore Badami Cave Temples',
                    'Visit Bhutanatha Group of Temples',
                    'Sunset at Agastya Lake'
                ],
                'highlight': 'Cave sculptures'
            },
            {
                'day': 2,
                'title': 'Heritage Sites & Departure',
                'activities': [
                    'Visit Pattadakal temples',
                    'Explore Aihole historical site',
                    'Depart from Badami'
                ],
                'highlight': 'UNESCO sites'
            }
        ]
    },
    'chikmagalur': {
        'name': 'Chikmagalur',
        'tagline': 'Coffee Land of Karnataka',
        'duration': '3 Days',
        'image_path': 'images/chikmagalur.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Plantation Stay',
                'activities': [
                    'Arrive in Chikmagalur and check into coffee estate',
                    'Coffee plantation walk',
                    'Visit Hirekolale Lake',
                    'Evening campfire'
                ],
                'highlight': 'Coffee tasting'
            },
            {
                'day': 2,
                'title': 'Mountain Exploration',
                'activities': [
                    'Trek to Mullayanagiri peak',
                    'Visit Baba Budangiri shrines',
                    'See Hebbe Falls',
                    'Evening local cuisine tasting'
                ],
                'highlight': 'Highest peak in Karnataka'
            },
            {
                'day': 3,
                'title': 'Departure',
                'activities': [
                    'Morning nature walk',
                    'Purchase coffee and spices',
                    'Depart from Chikmagalur'
                ],
                'highlight': 'Final mountain views'
            }
        ]
    },
    'udupi': {
        'name': 'Udupi',
        'tagline': 'Temple & Cuisine Hub',
        'duration': '2 Days',
        'image_path': 'images/udupi.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Temple Tour',
                'activities': [
                    'Arrive in Udupi and check into hotel',
                    'Visit Sri Krishna Temple',
                    'Explore Malpe Beach',
                    'Evening temple rituals'
                ],
                'highlight': 'Temple kitchen'
            },
            {
                'day': 2,
                'title': 'Beaches & Departure',
                'activities': [
                    'Visit St. Mary\'s Island',
                    'Explore Kapu Beach and lighthouse',
                    'Taste local Udupi cuisine',
                    'Depart from Udupi'
                ],
                'highlight': 'Basalt rock formations'
            }
        ]
    },
    'bandipur': {
        'name': 'Bandipur',
        'tagline': 'Wildlife Sanctuary',
        'duration': '3 Days',
        'image_path': 'images/bandipur.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Jungle Safari',
                'activities': [
                    'Arrive in Bandipur and check into jungle lodge',
                    'Afternoon jungle safari',
                    'Evening nature walk',
                    'Night campfire'
                ],
                'highlight': 'First wildlife spotting'
            },
            {
                'day': 2,
                'title': 'Full Day Safari',
                'activities': [
                    'Morning and afternoon jungle safaris',
                    'Visit Himavad Gopalaswamy Temple',
                    'Evening documentary about wildlife'
                ],
                'highlight': 'Tiger spotting chance'
            },
            {
                'day': 3,
                'title': 'Nature Walk & Departure',
                'activities': [
                    'Morning bird watching',
                    'Visit nearby tribal village',
                    'Depart from Bandipur'
                ],
                'highlight': 'Bird watching'
            }
        ]
    },
    'murudeshwar': {
        'name': 'Murudeshwar',
        'tagline': 'Coastal Temple Town',
        'duration': '2 Days',
        'image_path': 'images/murudeshwar.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Temple Visit',
                'activities': [
                    'Arrive in Murudeshwar and check into beach hotel',
                    'Visit Murudeshwar Temple and giant Shiva statue',
                    'Climb to viewpoint for sunset',
                    'Evening beach walk'
                ],
                'highlight': 'Giant Shiva statue'
            },
            {
                'day': 2,
                'title': 'Beach & Departure',
                'activities': [
                    'Morning visit to Netrani Island (optional snorkeling)',
                    'Explore local fish market',
                    'Depart from Murudeshwar'
                ],
                'highlight': 'Island views'
            }
        ]
    },
    'shimoga': {
        'name': 'Shimoga',
        'tagline': 'Land of Waterfalls',
        'duration': '3 Days',
        'image_path': 'images/shimoga.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Waterfall Tour',
                'activities': [
                    'Arrive in Shimoga and check into hotel',
                    'Visit Jog Falls (highest in Karnataka)',
                    'See Linganamakki Dam',
                    'Evening at local markets'
                ],
                'highlight': 'Jog Falls view'
            },
            {
                'day': 2,
                'title': 'Nature Exploration',
                'activities': [
                    'Visit Honnemaradu for water sports',
                    'Explore Tunga Anicut Dam',
                    'See Sakrebailu Elephant Camp',
                    'Evening river cruise'
                ],
                'highlight': 'Elephant interaction'
            },
            {
                'day': 3,
                'title': 'Departure',
                'activities': [
                    'Morning visit to Tyavarekoppa Lion Safari',
                    'See Gudavi Bird Sanctuary',
                    'Depart from Shimoga'
                ],
                'highlight': 'Wildlife spotting'
            }
        ]
    },
    'bijapur': {
        'name': 'Bijapur',
        'tagline': 'City of Dome',
        'duration': '2 Days',
        'image_path': 'images/bijapur.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Historical Tour',
                'activities': [
                    'Arrive in Bijapur and check into hotel',
                    'Visit Gol Gumbaz (whispering gallery)',
                    'Explore Ibrahim Rauza',
                    'Evening light show at Gol Gumbaz'
                ],
                'highlight': 'Whispering gallery'
            },
            {
                'day': 2,
                'title': 'More Heritage & Departure',
                'activities': [
                    'Visit Jama Masjid',
                    'See Malik-e-Maidan cannon',
                    'Explore Bijapur Fort',
                    'Depart from Bijapur'
                ],
                'highlight': 'Massive cannon'
            }
        ]
    },
    'nandi-hills': {
        'name': 'Nandi Hills',
        'tagline': 'Popular Hill Station',
        'duration': '1 Day',
        'image_path': 'images/nandi-hills.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Hill Station Tour',
                'activities': [
                    'Early morning arrival at Nandi Hills',
                    'Sunrise viewing from hilltop',
                    'Visit Tipu Sultan\'s Summer Palace',
                    'Explore Bhoga Nandeeshwara Temple',
                    'See Brahmashram caves'
                ],
                'highlight': 'Sunrise views'
            }
        ]
    },
    'sakleshpur': {
        'name': 'Sakleshpur',
        'tagline': 'Emerald Green Hills',
        'duration': '2 Days',
        'image_path': 'images/sakleshpur.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Nature Walk',
                'activities': [
                    'Arrive in Sakleshpur and check into homestay',
                    'Visit Manjarabad Fort',
                    'Walk through coffee and cardamom plantations',
                    'Evening campfire'
                ],
                'highlight': 'Fort views'
            },
            {
                'day': 2,
                'title': 'Adventure & Departure',
                'activities': [
                    'Trek to Bisle View Point',
                    'Visit Magajahalli Waterfalls',
                    'Depart from Sakleshpur'
                ],
                'highlight': 'Western Ghats views'
            }
        ]
    },
    'belur-halebid': {
        'name': 'Belur & Halebid',
        'tagline': 'Temple Architecture Marvels',
        'duration': '2 Days',
        'image_path': 'images/belur-halebid.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Belur Temple',
                'activities': [
                    'Arrive near Belur and check into hotel',
                    'Visit Chennakesava Temple (Belur)',
                    'See Hoysala architecture details',
                    'Evening local craft shopping'
                ],
                'highlight': 'Intricate carvings'
            },
            {
                'day': 2,
                'title': 'Halebid & Departure',
                'activities': [
                    'Visit Hoysaleswara Temple (Halebid)',
                    'See Kedareswara Temple',
                    'Explore archaeological museum',
                    'Depart from Belur/Halebid'
                ],
                'highlight': 'Temple sculptures'
            }
        ]
    },
    'karwar': {
        'name': 'Karwar',
        'tagline': 'Port Town with Beaches',
        'duration': '2 Days',
        'image_path': 'images/karwar.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Beach Relaxation',
                'activities': [
                    'Arrive in Karwar and check into beach resort',
                    'Relax at Rabindranath Tagore Beach',
                    'Visit Sadashivgad Fort',
                    'Evening seafood dinner'
                ],
                'highlight': 'Beach sunset'
            },
            {
                'day': 2,
                'title': 'Island Visit & Departure',
                'activities': [
                    'Boat ride to Devbagh Island',
                    'Visit Karwar Naval Base Museum',
                    'Depart from Karwar'
                ],
                'highlight': 'Island experience'
            }
        ]
    },
    'dandeli': {
        'name': 'Dandeli',
        'tagline': 'Adventure Destination',
        'duration': '3 Days',
        'image_path': 'images/dandeli.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Jungle Introduction',
                'activities': [
                    'Arrive in Dandeli and check into resort',
                    'Afternoon jungle safari',
                    'Evening coracle ride on Kali River',
                    'Night campfire'
                ],
                'highlight': 'First wildlife spotting'
            },
            {
                'day': 2,
                'title': 'Adventure Activities',
                'activities': [
                    'White water rafting on Kali River',
                    'Jungle ziplining',
                    'Visit Syntheri Rocks',
                    'Evening bird watching'
                ],
                'highlight': 'River rafting'
            },
            {
                'day': 3,
                'title': 'Nature Walk & Departure',
                'activities': [
                    'Morning nature trek',
                    'Visit nearby tribal village',
                    'Depart from Dandeli'
                ],
                'highlight': 'Tribal culture'
            }
        ]
    },
    'bidar': {
        'name': 'Bidar',
        'tagline': 'Land of Bidriware',
        'duration': '2 Days',
        'image_path': 'images/bidar.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Fort Tour',
                'activities': [
                    'Arrive in Bidar and check into hotel',
                    'Visit Bidar Fort',
                    'See Bahmani Tombs',
                    'Evening Bidriware shopping'
                ],
                'highlight': 'Fort architecture'
            },
            {
                'day': 2,
                'title': 'Heritage & Departure',
                'activities': [
                    'Visit Gurudwara Nanak Jhira Sahib',
                    'Explore Rangin Mahal',
                    'See Papnash Shiva Temple',
                    'Depart from Bidar'
                ],
                'highlight': 'Bidriware craft'
            }
        ]
    },
    'chitradurga': {
        'name': 'Chitradurga',
        'tagline': 'Land of Stones',
        'duration': '2 Days',
        'image_path': 'images/chitradurga.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Fort Exploration',
                'activities': [
                    'Arrive in Chitradurga and check into hotel',
                    'Explore Chitradurga Fort',
                    'See Hidimbeshwara Temple',
                    'Evening light show at fort'
                ],
                'highlight': 'Fort boulders'
            },
            {
                'day': 2,
                'title': 'Historical Sites & Departure',
                'activities': [
                    'Visit Chandravalli Caves',
                    'See Ankali Mutt',
                    'Explore Vani Vilas Sagar Dam',
                    'Depart from Chitradurga'
                ],
                'highlight': 'Ancient caves'
            }
        ]
    },
    'bellary': {
        'name': 'Bellary',
        'tagline': 'Land of Forts',
        'duration': '2 Days',
        'image_path': 'images/bellary.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Fort Tour',
                'activities': [
                    'Arrive in Bellary and check into hotel',
                    'Visit Bellary Fort',
                    'Explore Hampi (nearby)',
                    'Evening at local markets'
                ],
                'highlight': 'Fort views'
            },
            {
                'day': 2,
                'title': 'More Heritage & Departure',
                'activities': [
                    'Visit Tungabhadra Dam',
                    'See Kuntegadda Park',
                    'Depart from Bellary'
                ],
                'highlight': 'Dam visit'
            }
        ]
    },
    'mangalore': {
        'name': 'Mangalore',
        'tagline': 'Port City with Beaches',
        'duration': '2 Days',
        'image_path': 'images/mangalore.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & City Tour',
                'activities': [
                    'Arrive in Mangalore and check into hotel',
                    'Visit Kadri Manjunath Temple',
                    'Explore Sultan Battery',
                    'Evening at Panambur Beach'
                ],
                'highlight': 'Temple architecture'
            },
            {
                'day': 2,
                'title': 'Beaches & Departure',
                'activities': [
                    'Visit Ullal Beach',
                    'See St. Aloysius Chapel',
                    'Taste local Mangalorean cuisine',
                    'Depart from Mangalore'
                ],
                'highlight': 'Beach relaxation'
            }
        ]
    },
    'shravanabelagola': {
        'name': 'Shravanabelagola',
        'tagline': 'Jain Pilgrimage Center',
        'duration': '1 Day',
        'image_path': 'images/shravanabelagola.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Pilgrimage Tour',
                'activities': [
                    'Arrive in Shravanabelagola',
                    'Climb to Gommateshwara Statue',
                    'Visit Chandragiri and Vindhyagiri Hills',
                    'Explore Jain basadis',
                    'Learn about Jain culture'
                ],
                'highlight': 'Monolithic statue'
            }
        ]
    },
    'kabini': {
        'name': 'Kabini',
        'tagline': 'Wildlife & Backwaters',
        'duration': '3 Days',
        'image_path': 'images/kabini.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Jungle Safari',
                'activities': [
                    'Arrive in Kabini and check into resort',
                    'Afternoon jungle safari',
                    'Evening boat ride on Kabini River',
                    'Night campfire'
                ],
                'highlight': 'First wildlife spotting'
            },
            {
                'day': 2,
                'title': 'Full Day Wildlife',
                'activities': [
                    'Morning and afternoon safaris',
                    'Visit tribal village',
                    'Evening nature documentary'
                ],
                'highlight': 'Tiger spotting chance'
            },
            {
                'day': 3,
                'title': 'Nature Walk & Departure',
                'activities': [
                    'Morning bird watching',
                    'Visit nearby coffee plantation',
                    'Depart from Kabini'
                ],
                'highlight': 'Bird watching'
            }
        ]
    },
    'srirangapatna': {
        'name': 'Srirangapatna',
        'tagline': 'Island Town of History',
        'duration': '1 Day',
        'image_path': 'images/srirangapatna.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Historical Tour',
                'activities': [
                    'Arrive in Srirangapatna',
                    'Visit Ranganathaswamy Temple',
                    'See Tipu Sultan\'s Summer Palace',
                    'Explore Daria Daulat Bagh',
                    'Visit Gumbaz (Tipu\'s tomb)'
                ],
                'highlight': 'Historical significance'
            }
        ]
    },
    'madikeri': {
        'name': 'Madikeri',
        'tagline': 'Heart of Coorg',
        'duration': '2 Days',
        'image_path': 'images/madikeri.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Town Tour',
                'activities': [
                    'Arrive in Madikeri and check into homestay',
                    'Visit Madikeri Fort',
                    'See Raja\'s Seat viewpoint',
                    'Evening at Abbey Falls'
                ],
                'highlight': 'Hill station views'
            },
            {
                'day': 2,
                'title': 'Nature & Departure',
                'activities': [
                    'Visit Omkareshwara Temple',
                    'Explore coffee plantations',
                    'Depart from Madikeri'
                ],
                'highlight': 'Coffee culture'
            }
        ]
    },
    'jog-falls': {
        'name': 'Jog Falls',
        'tagline': 'Highest Waterfall in Karnataka',
        'duration': '1 Day',
        'image_path': 'images/jog-falls.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Waterfall Tour',
                'activities': [
                    'Arrive at Jog Falls',
                    'View waterfall from multiple viewpoints',
                    'Visit nearby Linganamakki Dam',
                    'See Tunga Anicut',
                    'Enjoy local cuisine'
                ],
                'highlight': 'Waterfall majesty'
            }
        ]
    },
    'bylakuppe': {
        'name': 'Bylakuppe',
        'tagline': 'Tibetan Settlement',
        'duration': '1 Day',
        'image_path': 'images/bylakuppe.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Tibetan Culture Tour',
                'activities': [
                    'Arrive in Bylakuppe',
                    'Visit Namdroling Monastery (Golden Temple)',
                    'Explore Tibetan markets',
                    'Attend prayer ceremony',
                    'Taste Tibetan cuisine'
                ],
                'highlight': 'Monastery grandeur'
            }
        ]
    },
    'agumbe': {
        'name': 'Agumbe',
        'tagline': 'Cherrapunji of South India',
        'duration': '2 Days',
        'image_path': 'images/agumbe.jpg',
        'itinerary': [
            {
                'day': 1,
                'title': 'Arrival & Rainforest Experience',
                'activities': [
                    'Arrive in Agumbe and check into homestay',
                    'Visit Agumbe Rainforest Research Station',
                    'Sunset at Sunset View Point',
                    'Evening nature walk'
                ],
                'highlight': 'Rainforest atmosphere'
            },
            {
                'day': 2,
                'title': 'Waterfalls & Departure',
                'activities': [
                    'Trek to Barkana Falls',
                    'Visit Onake Abbi Falls',
                    'Depart from Agumbe'
                ],
                'highlight': 'Waterfall trek'
            }
        ]
    },
  }  

    
  destination = destination_data.get(destination_slug, {})
  return render(request, 'karnataka/destination_karnataka.html',{'destination': destination})


#andra


def andra(request):
    return render(request, 'andra/domestic_andra.html')

def all_andra(request):
    return render(request, 'andra/all_andra.html')
def destination_andhra(request, destination_slug):
    destination_data = {
        'hyderabad': {
            'name': 'Hyderabad',
            'tagline': 'City of Pearls and Biryani',
            'duration': '3 Days',
            'image_path': 'images/hyderabad.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Heritage Tour',
                    'activities': [
                        'Arrive in Hyderabad and check into hotel',
                        'Visit Charminar and Laad Bazaar',
                        'Explore Golconda Fort',
                        'Evening at Hussain Sagar Lake'
                    ],
                    'highlight': 'Golconda Fort sound and light show'
                },
                {
                    'day': 2,
                    'title': 'Modern Hyderabad',
                    'activities': [
                        'Visit Ramoji Film City',
                        'Explore Hi-Tech City',
                        'Shopping at Inorbit Mall',
                        'Dinner at Paradise for Biryani'
                    ],
                    'highlight': 'Ramoji Film City tour'
                },
                {
                    'day': 3,
                    'title': 'Cultural Exploration',
                    'activities': [
                        'Visit Salar Jung Museum',
                        'See Chowmahalla Palace',
                        'Explore Qutub Shahi Tombs',
                        'Depart from Hyderabad'
                    ],
                    'highlight': 'Salar Jung Museum collections'
                }
            ]
        },
        'visakhapatnam': {
            'name': 'Visakhapatnam',
            'tagline': 'Jewel of the East Coast',
            'duration': '3 Days',
            'image_path': 'images/vizag.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Beach Tour',
                    'activities': [
                        'Arrive in Visakhapatnam and check into hotel',
                        'Visit RK Beach',
                        'Explore Submarine Museum',
                        'Evening at Tenneti Park'
                    ],
                    'highlight': 'Submarine Museum visit'
                },
                {
                    'day': 2,
                    'title': 'Nature & Culture',
                    'activities': [
                        'Excursion to Araku Valley',
                        'Visit Borra Caves',
                        'Explore Tribal Museum',
                        'Return to Vizag in evening'
                    ],
                    'highlight': 'Borra Caves exploration'
                },
                {
                    'day': 3,
                    'title': 'Spiritual & Departure',
                    'activities': [
                        'Visit Simhachalam Temple',
                        'Tour INS Kursura Museum',
                        'Visit Kailasagiri Hill Park',
                        'Depart from Visakhapatnam'
                    ],
                    'highlight': 'Kailasagiri ropeway ride'
                }
            ]
        },
        'tirupati': {
            'name': 'Tirupati',
            'tagline': 'Home to Lord Venkateswara Temple',
            'duration': '2 Days',
            'image_path': 'images/tirupati.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Visit',
                    'activities': [
                        'Arrive in Tirupati and check into hotel',
                        'Darshan at Tirumala Temple',
                        'Visit Srivari Mettu',
                        'Evening at Silathoranam'
                    ],
                    'highlight': 'Tirumala Temple darshan'
                },
                {
                    'day': 2,
                    'title': 'Local Exploration',
                    'activities': [
                        'Visit Kapila Theertham',
                        'See Chandragiri Fort',
                        'Explore Sri Venkateswara Museum',
                        'Depart from Tirupati'
                    ],
                    'highlight': 'Chandragiri Fort view'
                }
            ]
        },
        'warangal': {
            'name': 'Warangal',
            'tagline': 'Ancient Kakatiya capital',
            'duration': '2 Days',
            'image_path': 'images/warangal.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Historical Tour',
                    'activities': [
                        'Arrive in Warangal and check into hotel',
                        'Visit Warangal Fort',
                        'Explore Thousand Pillar Temple',
                        'Evening at Bhadrakali Lake'
                    ],
                    'highlight': 'Thousand Pillar Temple'
                },
                {
                    'day': 2,
                    'title': 'Nature & Departure',
                    'activities': [
                        'Visit Pakhal Lake',
                        'Explore Ramappa Temple',
                        'See Eturnagaram Wildlife Sanctuary',
                        'Depart from Warangal'
                    ],
                    'highlight': 'Ramappa Temple UNESCO site'
                }
            ]
        },
        'araku_valley': {
            'name': 'Araku Valley',
            'tagline': 'Scenic hill station with coffee plantations',
            'duration': '2 Days',
            'image_path': 'images/araku.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Arrival & Exploration',
                    'activities': [
                        'Arrive in Araku Valley and check into hotel',
                        'Visit Tribal Museum',
                        'Explore Coffee Plantations',
                        'Evening campfire'
                    ],
                    'highlight': 'Coffee plantation tour'
                },
                {
                    'day': 2,
                    'title': 'Nature & Departure',
                    'activities': [
                        'Visit Borra Caves',
                        'See Katiki Waterfalls',
                        'Train ride through hills',
                        'Depart from Araku'
                    ],
                    'highlight': 'Borra Caves exploration'
                }
            ]
        },
        'vijayawada': {
            'name': 'Vijayawada',
            'tagline': 'Commercial hub on the Krishna River',
            'duration': '2 Days',
            'image_path': 'images/vijayawada.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'City Tour',
                    'activities': [
                        'Arrive in Vijayawada and check into hotel',
                        'Visit Kanaka Durga Temple',
                        'Explore Prakasam Barrage',
                        'Evening at Bhavani Island'
                    ],
                    'highlight': 'Kanaka Durga Temple darshan'
                },
                {
                    'day': 2,
                    'title': 'Historical Sites',
                    'activities': [
                        'Visit Undavalli Caves',
                        'See Amaravati Stupa',
                        'Explore Kondapalli Fort',
                        'Depart from Vijayawada'
                    ],
                    'highlight': 'Undavalli rock-cut caves'
                }
            ]
        },
        'nagarjuna_sagar': {
            'name': 'Nagarjuna Sagar',
            'tagline': 'Ancient Buddhist site and dam',
            'duration': '1 Day',
            'image_path': 'images/nagarjunasagar.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Full Day Exploration',
                    'activities': [
                        'Arrive at Nagarjuna Sagar',
                        'Visit Nagarjuna Konda Island',
                        'See Nagarjuna Sagar Dam',
                        'Explore Ethipothala Falls',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Buddhist ruins on the island'
                }
            ]
        },
        'srisailam': {
            'name': 'Srisailam',
            'tagline': 'Famous Shiva temple on Nallamala hills',
            'duration': '1 Day',
            'image_path': 'images/srisailam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple & Nature',
                    'activities': [
                        'Arrive at Srisailam',
                        'Darshan at Mallikarjuna Temple',
                        'Visit Sakshi Ganapati Temple',
                        'Explore Srisailam Dam',
                        'See Pathala Ganga'
                    ],
                    'highlight': 'Mallikarjuna Temple darshan'
                }
            ]
        },
        'lepakshi': {
            'name': 'Lepakshi',
            'tagline': 'Ancient Vijayanagara-era temple',
            'duration': '1 Day',
            'image_path': 'images/lepakshi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Heritage Tour',
                    'activities': [
                        'Arrive at Lepakshi',
                        'Explore Veerabhadra Temple',
                        'See Nandi Statue',
                        'View hanging pillar',
                        'Return to Bangalore/Hyderabad'
                    ],
                    'highlight': 'Hanging pillar marvel'
                }
            ]
        },
        'kurnool': {
            'name': 'Kurnool',
            'tagline': 'Historical city with ancient forts',
            'duration': '1 Day',
            'image_path': 'images/kurnool.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Historical Exploration',
                    'activities': [
                        'Arrive in Kurnool',
                        'Visit Kurnool Fort',
                        'See Oravakallu Rock Garden',
                        'Explore Belum Caves',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Belum Caves exploration'
                }
            ]
        },
        'anantapur': {
            'name': 'Anantapur',
            'tagline': 'Land of temples and forts',
            'duration': '1 Day',
            'image_path': 'images/anantapur.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Cultural Tour',
                    'activities': [
                        'Arrive in Anantapur',
                        'Visit Lepakshi Temple',
                        'Explore Penukonda Fort',
                        'See Puttaparthi',
                        'Return to Bangalore'
                    ],
                    'highlight': 'Lepakshi Temple architecture'
                }
            ]
        },
        'gandikota': {
            'name': 'Gandikota',
            'tagline': 'Grand Canyon of India',
            'duration': '1 Day',
            'image_path': 'images/gandikota.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Canyon Exploration',
                    'activities': [
                        'Arrive at Gandikota',
                        'Explore Gandikota Fort',
                        'See Pennar River gorge',
                        'Visit Madhavaraya Temple',
                        'Camping by the canyon'
                    ],
                    'highlight': 'Canyon sunset views'
                }
            ]
        },
        'amaravati': {
            'name': 'Amaravati',
            'tagline': 'Ancient Buddhist site and new capital',
            'duration': '1 Day',
            'image_path': 'images/amaravati.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Heritage Tour',
                    'activities': [
                        'Arrive at Amaravati',
                        'Visit Amaravati Stupa',
                        'Explore Buddhist Museum',
                        'See new capital buildings',
                        'Return to Vijayawada'
                    ],
                    'highlight': 'Ancient Buddhist stupa'
                }
            ]
        },
        'nellore': {
            'name': 'Nellore',
            'tagline': 'Famous for rice production and temples',
            'duration': '1 Day',
            'image_path': 'images/nellore.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Local Exploration',
                    'activities': [
                        'Arrive in Nellore',
                        'Visit Ranganatha Temple',
                        'See Pulicat Lake',
                        'Explore Udayagiri Fort',
                        'Return to Chennai'
                    ],
                    'highlight': 'Pulicat Lake birdwatching'
                }
            ]
        },
        'rajahmundry': {
            'name': 'Rajahmundry',
            'tagline': 'Cultural capital of Andhra on Godavari',
            'duration': '2 Days',
            'image_path': 'images/rajahmundry.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'City Tour',
                    'activities': [
                        'Arrive in Rajahmundry and check into hotel',
                        'Visit Godavari Bridge',
                        'Explore ISKCON Temple',
                        'Evening boat ride on Godavari'
                    ],
                    'highlight': 'Godavari boat cruise'
                },
                {
                    'day': 2,
                    'title': 'Nature & Departure',
                    'activities': [
                        'Visit Pattiseema',
                        'See Papikondalu',
                        'Explore Maredumilli forests',
                        'Depart from Rajahmundry'
                    ],
                    'highlight': 'Papikondalu boat trip'
                }
            ]
        },
        'kakinada': {
            'name': 'Kakinada',
            'tagline': 'Port city with beautiful beaches',
            'duration': '2 Days',
            'image_path': 'images/kakinada.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Beach Tour',
                    'activities': [
                        'Arrive in Kakinada and check into hotel',
                        'Visit Kakinada Beach',
                        'Explore Uppada Beach',
                        'Evening at Coringa Wildlife Sanctuary'
                    ],
                    'highlight': 'Coringa mangrove forest'
                },
                {
                    'day': 2,
                    'title': 'Local Exploration',
                    'activities': [
                        'Visit Hope Island',
                        'See Draksharama Temple',
                        'Explore Annavaram Temple',
                        'Depart from Kakinada'
                    ],
                    'highlight': 'Draksharama Temple visit'
                }
            ]
        },
        'bhadrachalam': {
            'name': 'Bhadrachalam',
            'tagline': 'Famous Rama temple on Godavari',
            'duration': '1 Day',
            'image_path': 'images/bhadrachalam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Tour',
                    'activities': [
                        'Arrive at Bhadrachalam',
                        'Darshan at Sita Ramachandra Swamy Temple',
                        'Visit Parnasala',
                        'Explore Godavari riverfront',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Temple darshan'
                }
            ]
        },
        'khammam': {
            'name': 'Khammam',
            'tagline': 'Historical fort and temples',
            'duration': '1 Day',
            'image_path': 'images/khammam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Fort & Temples',
                    'activities': [
                        'Arrive in Khammam',
                        'Visit Khammam Fort',
                        'See Lakshmi Narasimha Temple',
                        'Explore Nelakondapalli ruins',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Khammam Fort views'
                }
            ]
        },
        'nizamabad': {
            'name': 'Nizamabad',
            'tagline': 'Historical city with ancient temples',
            'duration': '1 Day',
            'image_path': 'images/nizamabad.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Cultural Tour',
                    'activities': [
                        'Arrive in Nizamabad',
                        'Visit Nizamabad Fort',
                        'See Dichpally Ramalayam',
                        'Explore Alisagar Reservoir',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Dichpally temple architecture'
                }
            ]
        },
        'adilabad': {
            'name': 'Adilabad',
            'tagline': 'Land of waterfalls and forests',
            'duration': '1 Day',
            'image_path': 'images/adilabad.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Nature Tour',
                    'activities': [
                        'Arrive in Adilabad',
                        'Visit Kuntala Waterfall',
                        'Explore Kawal Wildlife Sanctuary',
                        'See Basar Saraswati Temple',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Kuntala Waterfall visit'
                }
            ]
        },
        'karimnagar': {
            'name': 'Karimnagar',
            'tagline': 'Historical temples and forts',
            'duration': '1 Day',
            'image_path': 'images/karimnagar.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Heritage Tour',
                    'activities': [
                        'Arrive in Karimnagar',
                        'Visit Elgandal Fort',
                        'See Kondagattu Temple',
                        'Explore Lower Manair Dam',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Elgandal Fort exploration'
                }
            ]
        },
        'ramagundam': {
            'name': 'Ramagundam',
            'tagline': 'Power hub of Telangana',
            'duration': '1 Day',
            'image_path': 'images/ramagundam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Industrial Tour',
                    'activities': [
                        'Arrive in Ramagundam',
                        'Visit Ramagundam Thermal Plant',
                        'Explore Kaleshwaram Temple',
                        'See Godavari barrage',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Kaleshwaram Temple visit'
                }
            ]
        },
        'mahbubnagar': {
            'name': 'Mahbubnagar',
            'tagline': 'Historical sites and temples',
            'duration': '1 Day',
            'image_path': 'images/mahbubnagar.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Cultural Tour',
                    'activities': [
                        'Arrive in Mahbubnagar',
                        'Visit Pillalamarri Banyan Tree',
                        'See Alampur Temples',
                        'Explore Koilsagar Dam',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Ancient banyan tree'
                }
            ]
        },
        'medak': {
            'name': 'Medak',
            'tagline': 'Famous cathedral and fort',
            'duration': '1 Day',
            'image_path': 'images/medak.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Historical Tour',
                    'activities': [
                        'Arrive in Medak',
                        'Visit Medak Cathedral',
                        'Explore Medak Fort',
                        'See Pocharam Wildlife Sanctuary',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Medak Cathedral architecture'
                }
            ]
        },
        'nalgonda': {
            'name': 'Nalgonda',
            'tagline': 'Historical forts and temples',
            'duration': '1 Day',
            'image_path': 'images/nalgonda.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Heritage Tour',
                    'activities': [
                        'Arrive in Nalgonda',
                        'Visit Nagarjuna Sagar Dam',
                        'Explore Yadagirigutta Temple',
                        'See Bhongir Fort',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Bhongir Fort climb'
                }
            ]
        },
        'yadadri': {
            'name': 'Yadadri',
            'tagline': 'Renovated Lakshmi Narasimha Temple',
            'duration': '1 Day',
            'image_path': 'images/yadadri.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Tour',
                    'activities': [
                        'Arrive at Yadadri',
                        'Darshan at Lakshmi Narasimha Temple',
                        'Explore temple complex',
                        'Visit nearby Narasimha Konda',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Temple darshan'
                }
            ]
        },
        'basar': {
            'name': 'Basar',
            'tagline': 'Famous Saraswati Temple',
            'duration': '1 Day',
            'image_path': 'images/basar.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Visit',
                    'activities': [
                        'Arrive at Basar',
                        'Visit Gnana Saraswati Temple',
                        'Participate in Akshara Abhyasam',
                        'Explore nearby attractions',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Akshara Abhyasam ritual'
                }
            ]
        },
        'alampur': {
            'name': 'Alampur',
            'tagline': 'Nava Brahma Temples on Tungabhadra',
            'duration': '1 Day',
            'image_path': 'images/alampur.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Tour',
                    'activities': [
                        'Arrive at Alampur',
                        'Visit all nine Nava Brahma Temples',
                        'See Jogulamba Temple',
                        'Explore Sangameshwara Temple',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Ancient temple architecture'
                }
            ]
        },
        'nagarjunakonda': {
            'name': 'Nagarjunakonda',
            'tagline': 'Ancient Buddhist island museum',
            'duration': '1 Day',
            'image_path': 'images/nagarjunakonda.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Buddhist Heritage',
                    'activities': [
                        'Arrive at Nagarjunakonda',
                        'Visit island museum by boat',
                        'Explore Buddhist stupas and relics',
                        'See reconstructed monuments',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Island museum visit'
                }
            ]
        },
        'mantralayam': {
            'name': 'Mantralayam',
            'tagline': 'Famous Raghavendra Swamy Mutt',
            'duration': '1 Day',
            'image_path': 'images/mantralayam.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Temple Visit',
                    'activities': [
                        'Arrive at Mantralayam',
                        'Darshan at Raghavendra Swamy Mutt',
                        'Visit Panchamukhi Anjaneya Temple',
                        'Take holy dip in Tungabhadra',
                        'Return to Hyderabad'
                    ],
                    'highlight': 'Mutt darshan'
                }
            ]
        },
        'puttaparthi': {
            'name': 'Puttaparthi',
            'tagline': 'Home of Sri Sathya Sai Baba',
            'duration': '1 Day',
            'image_path': 'images/puttaparthi.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Spiritual Tour',
                    'activities': [
                        'Arrive at Puttaparthi',
                        'Visit Prasanthi Nilayam',
                        'See Chaitanya Jyoti Museum',
                        'Explore Sai Kulwant Hall',
                        'Return to Bangalore'
                    ],
                    'highlight': 'Prasanthi Nilayam darshan'
                }
            ]
        },
        'horsley_hills': {
            'name': 'Horsley Hills',
            'tagline': "Andhra's Ooty with scenic views",
            'duration': '1 Day',
            'image_path': 'images/horsley_hills.jpg',
            'itinerary': [
                {
                    'day': 1,
                    'title': 'Hill Station Tour',
                    'activities': [
                        'Arrive at Horsley Hills',
                        'Visit Kalyani viewpoint',
                        'Explore Mallamma Temple',
                        'See Environmental Park',
                        'Return to Tirupati'
                    ],
                    'highlight': 'Scenic viewpoints'
                }
            ]
        }
    }

    destination = destination_data.get(destination_slug, {})
    return render(request, 'andra/destination_andra.html', {'destination': destination})


