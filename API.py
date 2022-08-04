import db.insert as db 
import extraction as ex
import util

def Collect(soup, cur, url):

	profile = ex.extract_profile(soup)
	profile = profile + (url,) 
	db.InsertProfile(profile, cur)
	user = profile[0]

	profile_id = db.ProfileID(cur, user)

	# ##insert skills
	skills = ex.extract_skills(soup)
	db.InsertSkill(skills,cur, profile_id)

	# #insert affilations
	aff_l = ex.extract_aff(soup)
	db.InsertAffilations(aff_l,cur, profile_id)

	# ##insert publication
	pub_l = ex.extract_publication(soup)
	db.InsertPublications(pub_l, cur, profile_id)

	# ##insert Projects
	# proj_l =ex.extract_projects(soup)
	# db.InsertProjects(proj_l, cur, profile_id)

	# ##Insert network
	network = ex.extract_network(soup)
	db.InsertNetwork(network, cur, profile_id)

def Collect_Email(soup):
  try: 
    util.download_paper(doi, name)
    util.get_email(name)
  except:  
    doi = ex.extract_doi(soup)
    name =  'file' + '.pdf'
    util.download_paper(doi, name)
    util.get_email(name)

