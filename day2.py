reports = []

with open('input.txt', 'r') as file:
    for line in file:
        report = list(map(int, line.split()))
        reports.append(report)

def isReportSafe(report):
    isIncreasing = None
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if isIncreasing is None:
            isIncreasing = diff > 0
        elif isIncreasing != (diff > 0):
            return False
        diff = abs(diff)
        if diff < 1 or diff > 3:
            return False
    return True

def isReportSafeWithDampening(report):
    return any(isReportSafe(report[:i] + report[i+1:]) for i in range(len(report)))

safeReports = 0
for report in reports:
    safe = isReportSafe(report)
    if safe:
        safeReports += 1

print("Safe Reports:", safeReports)

safeReports = 0
for report in reports:
    safe = isReportSafeWithDampening(report)
    if safe:
        safeReports += 1

print("Safe Reports with Dampening:", safeReports)