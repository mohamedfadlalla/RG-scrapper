

def InsertProfile(profile, cur):

	cur.execute('''INSERT OR REPLACE INTO Profile
	  (name, country, degree, email, citation, reads, publications, most_p, aff, department, url)
	  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',profile)

def ProfileID(cur, user):
	cur.execute('SELECT id FROM Profile WHERE name = ?', (user, ))
	# Call fetchone() method to query db
	profile_id = cur.fetchone()[0]
	return profile_id

def InsertSkill(skills, cur, profile_id):
	for skill in skills:
		cur.execute('''
		      INSERT OR REPLACE INTO Skill (title)
		      VALUES (?)''', (skill,))

		cur.execute('SELECT id FROM Skill WHERE title = ?', (skill, ))
		# Call fetchone() method to query db
		skill_id = cur.fetchone()[0]

		cur.execute('''
		INSERT OR REPLACE INTO Skilled (profile_id, skill_id)
		VALUES (?, ?)''', (profile_id, skill_id))

def InsertAffilations(aff_l, cur, profile_id):
	if aff_l == None:
		pass
	else:
		for aff in aff_l:
			cur.execute('''
			INSERT OR REPLACE INTO Institute (name)
			VALUES (?)''', (aff['aff'],))

			#skilled
			cur.execute('SELECT id FROM Institute WHERE name = ?', (aff['aff'], ))
			# Call fetchone() method to query db
			institue_id = cur.fetchone()[0]

			cur.execute('''
			  INSERT OR REPLACE INTO Affiliation (profile_id, institue_id, started, ended, position)
			  VALUES (?, ?, ?, ?, ?)''', (profile_id, institue_id, aff['period'][0], aff['period'][1], aff['postion']))

def InsertPublications(pub_l, cur, profile_id):
	if pub_l == None:
		pass
	else:
		for pub in pub_l:
			cur.execute('''
			INSERT OR REPLACE INTO Publication (title, url)
			VALUES (?, ?)''', (pub['title'],pub['url']))

			#skilled
			cur.execute('SELECT id FROM Publication WHERE title = ?', (pub['title'], ))
			# Call fetchone() method to query db
			pub_id = cur.fetchone()[0]

			cur.execute('''
			INSERT OR REPLACE INTO Published (profile_id, publication_id)
			VALUES (?, ?)''', (profile_id, pub_id))

def InsertProjects(proj_l, cur, profile_id):
	if proj_l == None:
		pass
	else:
		for proj in proj_l:
			cur.execute('''
			INSERT OR REPLACE INTO Projects (project, url)
			VALUES (?, ?)''', (proj['title'],proj['url']))

			#skilled
			cur.execute('SELECT id FROM Projects WHERE project = ?', (proj['title'], ))
			# Call fetchone() method to query db
			proj_id = cur.fetchone()[0]

			cur.execute('''
			INSERT OR REPLACE INTO Projected (profile_id, project_id)
			VALUES (?, ?)''', (profile_id, proj_id))

def InsertNetwork(network, cur, profile_id):
	if network == None:
		pass
	else:
		for net in network:
			cur.execute('''INSERT OR REPLACE INTO Globe (url, status) VALUES (?, 1)''',(net,))

			cur.execute('SELECT id FROM Globe WHERE url = ?', (net, ))
			# Call fetchone() method to query db
			net_id = cur.fetchone()[0]

			cur.execute('''
			INSERT OR REPLACE INTO Network (profile_id, net_id)
			VALUES (?, ?)''', (profile_id, net_id))

def InsertError(cur, url):
	cur.execute('UPDATE Globe SET status=? WHERE url=?', (2, url) )
