from crawler import Crawler 

print(Crawler)
sub_urls = [
    '/caisBYIS/search/byjjecgeomsaek.do?menu_id=m_m6_1'
]
cr = Crawler('http://work.mma.go.kr', sub_urls)