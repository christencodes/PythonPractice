import csv

stream_data = []
bad_data = []


def per_hour(super_chat, minutes):
    if not minutes:
        return 0
    return round(super_chat / (minutes / 60), 2)


def get_rating(peak, strong=50, average=20):
    if peak >= strong:
        return "Strong"
    if peak >= average:
        return "Average"
    return "Slow"


def stream_report(data, data_issues):
    total_minutes_streamed = 0
    total_super_chat = 0
    highest_super_chat = 0
    highest_super_chat_title = ""
    total_peak_viewers = 0
    ratings = {"Strong": 0, "Average": 0, "Slow": 0}

    if not data:
        print("No stream data")
    else:
        for row in data:
            print(
                f"{row['title']}: {row['peak_viewers']} peak viewers, ${row['per_hour']:.2f}/hr, ({row['rating']})"
            )
            total_minutes_streamed += row["minutes"]
            total_super_chat += row["super_chat"]
            if highest_super_chat < row["super_chat"]:
                highest_super_chat = row["super_chat"]
                highest_super_chat_title = row["title"]
            total_peak_viewers += row["peak_viewers"]
            ratings[row["rating"]] += 1

        print(f"Total hours streamed: {total_minutes_streamed / 60}")
        print(f"Total super chat: ${total_super_chat}")
        print(f"Average peak viewers: {round(total_peak_viewers / len(data),2)}")
        print(
            f"Ratings: {ratings['Strong']} Strong, {ratings['Average']} Average, {ratings['Slow']} Slow"
        )
        print(f"Best Stream: {highest_super_chat_title} ${highest_super_chat:.2f}")

    print()
    print("-----Data Issues-----")
    print(f"{len(data_issues)} rows skipped")
    for row in data_issues:
        print(f"{row}")


with open("checkpoint1/streams.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            row["title"] = row["title"].strip()
            row["minutes"] = int(row["minutes"])
            row["peak_viewers"] = int(row["peak_viewers"])
            row["super_chat"] = float(row["super_chat"])
            row["per_hour"] = per_hour(row["super_chat"], row["minutes"])
            row["rating"] = get_rating(row["peak_viewers"])

            stream_data.append(row)
        except ValueError as error:
            bad_data.append(f"{row['title']} : {error}")


stream_report(stream_data, bad_data)

with open("checkpoint1/stream_report.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "title",
            "minutes",
            "peak_viewers",
            "super_chat",
            "per_hour",
            "rating",
        ],
    )
    writer.writeheader()
    writer.writerows(stream_data)

with open("checkpoint1/stream_issues.txt", "w") as file:
    if not bad_data:
        file.write("No Data issues")
    else:
        file.write("-----Data Issues-----\n")
        file.write(f"{len(bad_data)} rows skipped\n")
        for row in bad_data:
            file.write(f"{row}\n")
