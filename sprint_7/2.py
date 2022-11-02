import sys


class TrainingSession:
    __slots__ = ("start", "end")

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __gt__(self, other):
        return (
            self.end > other.end
            if self.end != other.end
            else self.start > other.start
        )

    def __lt__(self, other):
        return not self.__gt__(other)


def convert_time(time):
    if time > int(time):
        return time
    return int(time)


n = int(input())
training_sessions = []
for i in range(n):
    s, e = sys.stdin.readline().rstrip().split()
    training_sessions.append(
        TrainingSession(
            start=float(s),
            end=float(e),
        )
    )

training_sessions.sort()
result = [training_sessions[0]]

for i, v in enumerate(training_sessions[1:]):
    if v.start >= result[-1].end:
        result.append(v)
print(len(result))
for session in result:
    print(convert_time(session.start), convert_time(session.end))
