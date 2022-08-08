from exercice6.q1 import InfoRadiusLog, WarnRadiusLog, WarnAuditLog
from exercice6.q2 import XmlParser, User, PATH_TO_XML_FILE
from exercice6.q3 import LogStats
from exercice6.q4 import LogGraph
from pprint import pprint


def main():
    print("\n# Question 1 :")
    # Can we boost performance by reading line by line ???
    info_radius = InfoRadiusLog()
    print(f"InfoRadiusLog --> {len(info_radius.logs)} lines found !")
    warn_radius = WarnRadiusLog()
    print(f"WarnRadiusLog --> {len(warn_radius.logs)} lines found !")
    warn_audit = WarnAuditLog()
    print(f"WarnAuditLog --> {len(warn_audit.logs)} lines found !")

    print("\n# Question 2 :")
    xml_parser = XmlParser(PATH_TO_XML_FILE, User)
    users = xml_parser.create_dataclass()
    pprint(users)

    print("\n# Question 3 :")
    stats = LogStats(info_radius, warn_radius, warn_audit)
    stats.print_stats()
    print(f"stats.logs_stats --> {stats.logs_stats}")

    print("\n# Question 4 :")
    graph_stats = LogGraph(info_radius, warn_radius, warn_audit)
    graph_stats.display()

if __name__ == '__main__':
    main()