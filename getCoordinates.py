from xml.dom.minidom import parseString
from bs4 import BeautifulSoup
import os
import re
import string


def main():
    for filename in os.listdir("arena_defs_decoded"):
        readxml(filename)


def readxml(filename):
    file = open('arena_defs_decoded/' + filename, 'r')
    data = file.read()
    file.close()

    filenum = filename[-6:-4]
    filename = filenum + '_' + filename[:-7]
    print filename

    soup = BeautifulSoup(data, 'xml')

    bottomLeft = soup.find("bottomLeft")
    upperRight = soup.find("upperRight")
    bottomLeft = bottomLeft.contents[0]
    upperRight = upperRight.contents[0]

    # Bounding box: top left (x1,y1), bottom right (x2,y2)
    x1, y2 = string.split(bottomLeft)
    x2, y1 = string.split(upperRight)
    x1, y2 = float(x1), float(y2)
    x2, y1 = float(x2), float(y1)

    print "bottomLeft:\t" + str(x1) + "\t" + str(y2)
    print "upperRight:\t" + str(x2) + "\t" + str(y1)

    ctf = soup.find("ctf")
    ass = soup.find("assault")
    dom = soup.find("domination")
    if ctf != None:
        print "CTF"
        teamBasePositions = ctf.find("teamBasePositions")
        team1 = teamBasePositions.find("team1")
        team2 = teamBasePositions.find("team2")
        team1Position = team1.find(re.compile("^position"))
        team2Position = team2.find(re.compile("^position"))

        print "team positions:"
        x, y = getCoords(team1Position.contents[0]);
        print "team 1:\t" + str(x) + "\t" + str(y) + "\t" + "converted:\t" + str(getConvertedXY(team1Position.contents[0], x1, y1, x2, y2))
        x, y = getCoords(team2Position.contents[0])
        print "team 2:\t" + str(x) + "\t" + str(y) + "\t" + "converted:\t" + str(getConvertedXY(team2Position.contents[0], x1, y1, x2, y2))

        teamSpawnPoints = ctf.find("teamSpawnPoints")
        if teamSpawnPoints != None:
            team1 = teamSpawnPoints.find("team1")
            team2 = teamSpawnPoints.find("team2")
            team1SpawnPoint = team1.find_all("position")
            team2SpawnPoint = team2.find_all("position")

            print "spawn points:"
            for spawn in team1SpawnPoint:
                x, y = getCoords(spawn.contents[0]);
                print "team 1:\t" + str(x) + "\t" + str(y) + "\t" + "converted:\t" + str(getConvertedXY(spawn.contents[0], x1, y1, x2, y2))
            for spawn in team2SpawnPoint:
                x, y = getCoords(spawn.contents[0]);
                print "team 2:\t" + str(x) + "\t" + str(y) + "\t" + "converted:\t" + str(getConvertedXY(spawn.contents[0], x1, y1, x2, y2))

    if ass != None:
        print "ASS"
        BasePosition = ass.find("teamBasePositions").find("team1").find(re.compile("^position"))
        x, y = getCoords(BasePosition.contents[0]);
        print "base:\t" + str(x) + "\t" + str(y) + "\t" + "converted:\t" + str(getConvertedXY(BasePosition.contents[0], x1, y1, x2, y2))

        teamSpawnPoints = ass.find("teamSpawnPoints")
        if teamSpawnPoints != None:
            team1 = teamSpawnPoints.find("team1")
            team2 = teamSpawnPoints.find("team2")
            team1SpawnPoint = team1.find_all("position")
            team2SpawnPoint = team2.find_all("position")

            print "spawn points:"
            for spawn in team1SpawnPoint:
                x, y = getCoords(spawn.contents[0]);
                print "team 1:\t" + str(x) + "\t" + str(y) + "\t" + "converted:\t" + str(getConvertedXY(spawn.contents[0], x1, y1, x2, y2))
            for spawn in team2SpawnPoint:
                x, y = getCoords(spawn.contents[0]);
                print "team 2:\t" + str(x) + "\t" + str(y) + "\t" + "converted:\t" + str(getConvertedXY(spawn.contents[0], x1, y1, x2, y2))

    if dom != None:
        print "DOM"
        controlPoint = dom.find("controlPoint")
        x, y = getCoords(controlPoint.contents[0]);
        print "base:\t" + str(x) + "\t" + str(y) + "\t" + "converted:\t" + str(getConvertedXY(controlPoint.contents[0], x1, y1, x2, y2))
        teamSpawnPoints = dom.find("teamSpawnPoints")
        team1 = teamSpawnPoints.find("team1")
        team2 = teamSpawnPoints.find("team2")
        team1SpawnPoint = team1.find_all("position")
        team2SpawnPoint = team2.find_all("position")

        print "spawn points:"
        for spawn in team1SpawnPoint:
            x, y = getCoords(spawn.contents[0]);
            print "team 1:\t" + str(x) + "\t" + str(y) + "\t" + "converted:\t" + str(getConvertedXY(spawn.contents[0], x1, y1, x2, y2))
        for spawn in team2SpawnPoint:
            x, y = getCoords(spawn.contents[0]);
            print "team 2:\t" + str(x) + "\t" + str(y) + "\t" + "converted:\t" + str(getConvertedXY(spawn.contents[0], x1, y1, x2, y2))

    print "\n"


def getCoords(input):
    inx, iny = string.split(input)
    x, y = float(inx.replace(',', '.')), float(iny.replace(',', '.'))
    return x, y


def getConvertedXY(input, x1, y1, x2, y2):
    inx, iny = string.split(input)
    inx, iny = float(inx.replace(',', '.')), float(iny.replace(',', '.'))

    maxX = x2 - min(x1,x2) # X and Y axis should be equals in length

    # move coordinates to start from (0,0)
    inx = inx - min(x1,x2)
    iny = iny - min(y1,y2)

    inx, iny = scaleCoordinates(inx, iny, maxX, 500.0)
    inx, iny = int(round(inx)), int(round(iny))

    # set icon center at coordinates (icons 64x64)
    #inx -= 24
    #iny += 24

    return inx, iny


def scaleCoordinates(x, y, oldMax, newMax):
    x = x / oldMax * newMax
    y = y / oldMax * newMax
    return x, y

if __name__ == '__main__':
    main()
