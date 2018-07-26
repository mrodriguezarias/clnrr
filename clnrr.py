#!/usr/bin/env python3

import os, sys, datetime

LOG_PATH = '/tmp/clnrr.log'

def keyVal(key, value):
	return {'key': key, 'value': value}

def printInfo(m):
	for e in m:
		print('   ', e['key'], '=', e['value'])

def radarrOnDownload():
	m = []

	m.append(keyVal('ID', os.getenv('radarr_Movie_Id')))
	m.append(keyVal('Title', os.getenv('radarr_Movie_Title')))
	m.append(keyVal('Path', os.getenv('radarr_Movie_Path')))
	m.append(keyVal('IMDB', os.getenv('radarr_Movie_ImdbId')))
	m.append(keyVal('File ID', os.getenv('radarr_MovieFile_Id')))
	m.append(keyVal('File Relative Path', os.getenv('radarr_MovieFile_RelativePath')))
	filePath = os.getenv('radarr_MovieFile_Path')
	m.append(keyVal('File Path', filePath))
	m.append(keyVal('File Quality', os.getenv('radarr_MovieFile_Quality')))
	m.append(keyVal('Quality Version', os.getenv('radarr_MovieFile_QualityVersion')))
	m.append(keyVal('Release Group', os.getenv('radarr_MovieFile_ReleaseGroup')))
	m.append(keyVal('Scene Name', os.getenv('radarr_MovieFile_SceneName')))
	sourcePath = os.getenv('radarr_MovieFile_SourcePath')
	m.append(keyVal('Source Path', sourcePath))
	m.append(keyVal('Source Folder', os.getenv('radarr_MovieFile_SourceFolder')))

	# Check if Source Path still exists
	sourcePathExists = os.path.exists(sourcePath)
	if sourcePathExists:
		m.append(keyVal('Source Exists', 'true'))
	else:
		m.append(keyVal('Source Exists', 'false'))

	# Check if Destination Path exists
	destinationPathExists = os.path.exists(filePath)
	if destinationPathExists:
		m.append(keyVal('Destination Exists', 'true'))
	else:
		m.append(keyVal('Destination Exists', 'false'))

	if sourcePathExists and destinationPathExists:
		os.remove(sourcePath)
		m.append(keyVal('Source Deleted', 'true'))
	else:
		m.append(keyVal('Source Deleted', 'false'))

	printInfo(m)

def sonarrOnDownload():
	m = []

	m.append(keyVal('IsUpgrade', os.getenv('sonarr_IsUpgrade')))
	m.append(keyVal('ID', os.getenv('sonarr_Series_Id')))
	m.append(keyVal('Title', os.getenv('sonarr_series_title')))
	m.append(keyVal('Path', os.getenv('sonarr_Series_Path')))
	m.append(keyVal('TvdbId', os.getenv('sonarr_Series_TvdbId')))
	m.append(keyVal('TvMazeId', os.getenv('sonarr_Series_TvMazeId')))
	m.append(keyVal('IMDB', os.getenv('sonarr_Series_Imdb')))
	m.append(keyVal('Series Type', os.getenv('sonarr_Series_Type')))
	m.append(keyVal('Episode File ID', os.getenv('sonarr_EpisodeFile_Id')))
	m.append(keyVal('Relative Path', os.getenv('sonarr_EpisodeFile_RelativePath')))
	filePath = os.getenv('sonarr_EpisodeFile_Path')
	m.append(keyVal('File Path', filePath))
	m.append(keyVal('Episode Count', os.getenv('sonarr_EpisodeFile_EpisodeCount')))
	m.append(keyVal('Season Number', os.getenv('sonarr_EpisodeFile_SeasonNumber')))
	m.append(keyVal('Episode Number', os.getenv('sonarr_EpisodeFile_EpisodeNumbers')))
	m.append(keyVal('Episode Air Dates', os.getenv('sonarr_EpisodeFile_EpisodeAirDates')))
	m.append(keyVal('Episode Air Dates UTC', os.getenv('sonarr_EpisodeFile_EpisodeAirDatesUtc')))
	m.append(keyVal('Episode Title', os.getenv('sonarr_EpisodeFile_EpisodeTitles')))
	m.append(keyVal('File Quality', os.getenv('sonarr_EpisodeFile_Quality')))
	m.append(keyVal('File Quality Version', os.getenv('sonarr_EpisodeFile_QualityVersion')))
	m.append(keyVal('Release Group', os.getenv('sonarr_EpisodeFile_ReleaseGroup')))
	m.append(keyVal('Scene Name', os.getenv('sonarr_EpisodeFile_SceneName')))
	sourcePath = os.getenv('sonarr_EpisodeFile_SourcePath')
	m.append(keyVal('Source Path', sourcePath))
	m.append(keyVal('Source Folder', os.getenv('sonarr_EpisodeFile_SourceFolder')))
	m.append(keyVal('Deleted Relative Paths', os.getenv('sonarr_DeletedRelativePaths')))
	m.append(keyVal('Deleted Paths', os.getenv('sonarr_DeletedPaths')))

	# Check if Source Path still exists
	sourcePathExists = os.path.exists(sourcePath)
	if sourcePathExists:
		m.append(keyVal('Source Exists', 'true'))
	else:
		m.append(keyVal('Source Exists', 'false'))

	# Check if Destination Path exists
	destinationPathExists = os.path.exists(filePath)
	if destinationPathExists:
		m.append(keyVal('Destination Exists', 'true'))
	else:
		m.append(keyVal('Destination Exists', 'false'))

	if sourcePathExists and destinationPathExists:
		os.remove(sourcePath)
		m.append(keyVal('Source Deleted', 'true'))
	else:
		m.append(keyVal('Source Deleted', 'false'))

	printInfo(m)

def main():
	sys.stdout = open(LOG_PATH, 'a')

	print(datetime.datetime.now(), end=' ')
	if os.getenv('radarr_eventtype') == 'Download':
		print('Cleaning up downloaded movie from Radarr')
		radarrOnDownload()
	elif os.getenv('sonarr_eventtype') == 'Download':
		print('Cleaning up downloaded episode from Sonarr')
		sonarrOnDownload()
	else:
		print('Nothing to clean up')


if __name__ == '__main__':
	main()
