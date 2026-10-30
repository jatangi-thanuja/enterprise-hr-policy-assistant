import re


def create_chunks(pages):

    all_chunks = []

    heading_pattern = (
        r"(?m)(?=^[ \t]*(?:\d+\.[ \t]+\S.*|\([A-G]\)[ \t]+\S.*)[ \t]*$)"
    )

    for page in pages:

        sections = re.split(heading_pattern, page["text"])

        for section in sections:

            content = section.strip()

            if content:

                all_chunks.append({
                    "text": content,
                    "source": page["source"],
                    "page": page["page"]
                })

    return all_chunks