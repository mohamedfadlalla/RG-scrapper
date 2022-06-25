from util import to_str

def extract_projects(soup):
    projs = []
    projects = soup.select_one('#lite-page > main > section.lite-page__content > div:nth-child(4) > div > div.nova-legacy-c-card__body.nova-legacy-c-card__body--spacing-none > div')
    
    if projects == None:
        return None
    else:
        for project in projects:
            dic={}
            proj = project.find('div', class_='nova-legacy-e-text nova-legacy-e-text--size-l nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-v-project-item__title')
            dic['url'] = proj.a['href']
            dic['title'] = proj.text
            projs.append(dic)
        return projs

def extract_publication(soup):
    pub = []
    matches = soup.select_one('#research-items > div > div > div.nova-legacy-c-card__body.nova-legacy-c-card__body--spacing-none > div')
    if matches == None:
        return None
    else:
        for match in matches:
            dic = {}
            title = match.find('div', class_='nova-legacy-e-text nova-legacy-e-text--size-l nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-v-publication-item__title').text
            url = match.find('div', class_='nova-legacy-e-text nova-legacy-e-text--size-l nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-v-publication-item__title').a['href']
            dic['title'] = title
            dic['url'] = url
            pub.append(dic)

        return pub

def extract_aff(soup):
    affs = soup.select_one('#lite-page > main > section.lite-page__content > div:nth-child(1) > div:nth-child(4) > div.nova-legacy-c-card__body.nova-legacy-c-card__body--spacing-inherit > div')    
    if affs == None:
        return None
    else:
        matches = affs.find_all('div', class_='nova-legacy-c-card nova-legacy-c-card--spacing-s nova-legacy-c-card--elevation-none')

        affs_l = []
        for match in matches:
            dic = {}
            aff = match.find('div', class_='nova-legacy-e-text nova-legacy-e-text--size-l nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-v-job-item__title').text
            department = match.find( class_='nova-legacy-e-list nova-legacy-e-list--size-m nova-legacy-e-list--type-inline nova-legacy-e-list--spacing-none nova-legacy-v-job-item__meta-data')
            try:
                department_str = list(x.text for x in department.find_all('span'))
                period = match.find('div', class_='nova-legacy-e-text nova-legacy-e-text--size-m nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-c-qualifier__label')
                period_str = list(x.text for x in period.find_all('span'))
                postion = match.find('div', class_='nova-legacy-e-text nova-legacy-e-text--size-m nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit').text
                dic['aff'] = aff
                dic['department'] = to_str(department_str)
                dic['postion'] = postion
                dic['aff'] = aff
                dic['period'] = period_str
            except AttributeError:
                dic['aff'] = 'Null'
                dic['department'] = 'Null'
                dic['postion'] = 'Null'
                dic['aff'] = 'Null'
                dic['period'] = 'Null'
            affs_l.append(dic)

        return affs_l

def extract_profile(soup):
    user = soup.select_one('#lite-page > main > section.lite-page__content-header > div > div.content-grid__full > div > div > div > div:nth-child(2) > div > div.nova-legacy-l-flex__item.nova-legacy-l-flex__item--grow > div > div:nth-child(2) > h1 > div > div:nth-child(1) > div').text
    country = 'Null'
    email = 'Null'
    matches = soup.find_all('div', class_='nova-legacy-e-text nova-legacy-e-text--size-xl nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit')
    publicaton = matches[0].text
    reads = matches[1].text
    citation = matches[2].text
    try:
        projects = soup.select_one('#lite-page > main > section.lite-page__header-navigation.lite-page__header-navigation--with-ad > div > div > div > nav > div > div.nova-legacy-c-nav__items > button:nth-child(4) > div > div > a > span').text
        degree = soup.find('div', class_='nova-legacy-e-text nova-legacy-e-text--size-m nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-grey-600 title').text
        department = soup.select_one('#lite-page > main > aside > div.nova-legacy-o-stack.nova-legacy-o-stack--gutter-m.nova-legacy-o-stack--spacing-none.nova-legacy-o-stack--no-gutter-outside > div:nth-child(1) > div > div.nova-legacy-c-card__body.nova-legacy-c-card__body--spacing-inherit > div > div > div > div > div > div:nth-child(3) > div > div > ul > li:nth-child(1) > span').text
        aff = soup.select_one('#lite-page > main > aside > div.nova-legacy-o-stack.nova-legacy-o-stack--gutter-m.nova-legacy-o-stack--spacing-none.nova-legacy-o-stack--no-gutter-outside > div:nth-child(1) > div > div.nova-legacy-c-card__body.nova-legacy-c-card__body--spacing-inherit > div > div > div > div > div > div:nth-child(2) > div > a').text        
    except AttributeError:
        projects = 0
        degree = 'Null'
        aff = 'Null'
        department = 'Null'
        
    most_p = 'Null'
    return (user, country , degree, email, citation, reads, publicaton, projects, most_p, aff, department)

def extract_skills(soup):
    matches = soup.find_all('a', class_='nova-legacy-e-badge nova-legacy-e-badge--color-grey nova-legacy-e-badge--display-inline nova-legacy-e-badge--luminosity-medium nova-legacy-e-badge--size-l nova-legacy-e-badge--theme-ghost nova-legacy-e-badge--radius-full profile-about__badge')
    skills = []
    for match in matches:
        skills.append(match.text)
    return skills

def extract_network(soup):
    network = []
    match = soup.find_all('a', class_='nova-legacy-e-link nova-legacy-e-link--color-inherit nova-legacy-e-link--theme-bare')
    if match == None:
        return None
    else:
        for i in match:
            if i['href'].startswith('https://www.researchgate.net/profile'):
                network.append(i['href'])
        return list(set(network))