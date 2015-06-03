#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup
import re
import collections
import json
import HTMLParser
from pymongo import MongoClient
html = HTMLParser.HTMLParser()
conn = MongoClient()
db = conn['comments']
cardInfoDB = db.cardData

cards = [7, 8, 9, 12, 21, 22, 23, 28, 30, 31, 32, 34, 36, 37, 41, 45, 48, 51, 52, 54, 59, 60, 61, 63, 64, 67, 68, 69, 70, 75, 76, 77, 86, 90, 95, 99, 100, 102, 113, 132, 134, 137, 138, 140, 141, 145, 146, 147, 149, 151, 157, 158, 163, 172, 175, 178, 179, 180, 182, 186, 189, 191, 192, 195, 196, 201, 204, 205, 209, 211, 213, 216, 217, 220, 226, 227, 229, 232, 233, 237, 238, 239, 242, 250, 251, 253, 254, 257, 262, 268, 272, 274, 279, 281, 282, 284, 285, 286, 287, 289, 290, 291, 292, 296, 298, 299, 300, 301, 304, 306, 308, 311, 313, 315, 317, 318, 321, 325, 329, 332, 336, 338, 339, 340, 344, 345, 348, 351, 352, 358, 363, 364, 365, 366, 374, 376, 378, 381, 383, 389, 391, 394, 395, 397, 400, 401, 404, 405, 411, 413, 415, 420, 421, 424, 430, 435, 436, 437, 440, 443, 445, 447, 451, 453, 455, 456, 457, 458, 459, 460, 461, 462, 466, 467, 468, 469, 471, 472, 475, 476, 479, 481, 482, 485, 488, 489, 490, 492, 493, 496, 503, 505, 510, 511, 512, 513, 517, 519, 523, 525, 526, 530, 531, 533, 537, 538, 545, 546, 548, 555, 556, 559, 564, 567, 570, 573, 577, 578, 581, 582, 584, 585, 587, 592, 594, 596, 600, 601, 602, 605, 606, 608, 609, 613, 614, 618, 621, 622, 629, 630, 631, 635, 636, 637, 640, 641, 642, 643, 648, 654, 658, 662, 667, 670, 671, 672, 678, 679, 680, 687, 690, 692, 699, 700, 708, 710, 712, 715, 724, 725, 727, 730, 734, 736, 739, 742, 748, 749, 753, 754, 755, 756, 757, 759, 762, 763, 764, 765, 766, 767, 768, 773, 774, 777, 778, 783, 784, 785, 790, 791, 796, 797, 801, 804, 807, 808, 810, 811, 812, 813, 814, 818, 823, 825, 830, 834, 835, 836, 841, 846, 847, 850, 854, 855, 858, 859, 860, 864, 866, 877, 878, 886, 887, 890, 891, 893, 896, 903, 904, 906, 912, 914, 915, 919, 920, 921, 922, 926, 928, 930, 932, 940, 943, 950, 959, 960, 962, 968, 969, 971, 974, 976, 979, 982, 985, 987, 988, 990, 993, 994, 995, 997, 999, 1003, 1004, 1006, 1007, 1008, 1009, 1014, 1016, 1019, 1022, 1023, 1026, 1029, 1035, 1037, 1047, 1050, 1063, 1064, 1066, 1068, 1073, 1074, 1077, 1078, 1080, 1084, 1086, 1087, 1090, 1091, 1092, 1093, 1098, 1099, 1100, 1108, 1109, 1117, 1122, 1123, 1124, 1133, 1135, 1140, 1141, 1142, 1143, 1144, 1145, 1147, 1155, 1158, 1161, 1167, 1171, 1174, 1178, 1182, 1186, 1189, 1190, 1221, 1241, 1243, 1261, 1281, 1301, 1321, 1322, 1323, 1324, 1325, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1382, 1401, 1481, 1501, 1522, 1541, 1602, 1603, 1622, 1623, 1624, 1634, 1636, 1637, 1638, 1639, 1640, 1642, 1643, 1650, 1651, 1652, 1653, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1667, 1669, 1671, 1672, 1673, 1674, 1677, 1681, 1682, 1683, 1686, 1687, 1688, 1693, 1694, 1707, 1715, 1720, 1721, 1723, 1725, 1730, 1733, 1737, 1746, 1748, 1751, 1753, 1754, 1761, 1762, 1763, 1764, 1765, 1766, 1767, 1768, 1769, 1770, 1771, 1772, 1773, 1774, 1775, 1776, 1777, 1781, 1782, 1783, 1784, 1785, 1786, 1787, 1788, 1789, 1790, 1791, 1792, 1793, 1794, 1795, 1796, 1797, 1798, 1799, 1800, 1801, 1802, 1803, 1804, 1805, 1806, 1807, 1808, 1809, 1810, 1817, 1818, 1819, 1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1830, 1831, 1832, 1837, 1840, 1842, 1843, 1844, 1845, 1846, 1848, 1849, 1850, 1854, 1855, 1858, 1860, 1861, 1862, 1864, 1865, 1867, 1868, 1869, 1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1888, 1889, 1891, 1892, 1893, 1897, 1899, 1900, 1901, 1903, 1904, 1905, 1906, 1907, 1910, 1912, 1913, 1914, 1915, 1925, 1927, 1928, 1929, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1960, 1976, 1982, 1985, 1986, 1988, 1989, 1990, 1991, 1992, 1993, 1995, 1997, 1998, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2093, 2094, 2095, 2096, 2101, 2102, 2103, 2104, 2105, 2106, 2107, 2113, 2114, 2115, 2116, 2117, 2118, 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2140, 2141, 2142, 2143, 2144, 2145, 2146, 2147, 2148, 2149, 2150, 2151, 2152, 2153, 2154, 2155, 2156, 2157, 2162, 2172, 2176, 2177, 2195, 2197, 2199, 2221, 2225, 2226, 2227, 2230, 2232, 2233, 2234, 2235, 2240, 2249, 2257, 2258, 2260, 2261, 2262, 2263, 2270, 2274, 2275, 2277, 2278, 2279, 2280, 2281, 2283, 2284, 2286, 2287, 2288, 2289, 2290, 2291, 2292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2301, 2304, 2306, 2308, 2310, 2311, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322]

for card in cards:
	webpage = urllib2.urlopen('http://www.hearthhead.com/card=' + str(card))
	contents = webpage.read()
	imgUrl = "http:" + html.unescape(re.findall('<meta property="twitter&#x3A;image&#x3A;src" content="(.*?\\b)"', contents)[0])
	print imgUrl
	try:
		cardName = html.unescape(re.findall('<meta property="og&#x3A;title" content="(.*?\\b)"', contents)[0])
		print cardName
		comments = re.findall('(\[{commentv2:1.*?\]}\])', contents)
	except:
		print 'card has no data'
		
	try:
		for comment in comments:
	#			myJson = json.loads(comment)
	#			 myJson = json.loads(comment)
				body = re.findall("body:(.*?)',", comment.lower())
				body2 = re.findall("\"body\":(.*?)\",", comment.lower())
				allComments = body + body2
				print len(allComments)
				full_string = ""
				for aComment in allComments:
					if aComment[-1] == "\\":
						print "fixing string"
						aComment = aComment[:-1]
						
					full_string += aComment.decode('string_escape')
					
				words = re.findall("\w{4,}(?!http)", full_string)
				commentCount = collections.Counter(words).most_common(65)
				cardInfo = {"cardName": cardName, "img": imgUrl, "comments": commentCount}
				totalComments = len(allComments)
#				cardInfoID = cardInfoDB.insert_one(cardInfo)
				cardInfoDB.update({'cardName': cardName},{'$set': {'commentCount': totalComments}})
				print "insert " + str(card)
				print "==========================================="
	except:
		print str(card) + ' failed'
#	print soup.prettify()
#	print comments