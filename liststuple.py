# lists
s3_buckets_lists = ["abhishek_demo_bucket","ramu_demo_bucket", "tim_demo_bucket","john_demo_bucket"]
print(len(s3_buckets_lists)) 

s3_buckets_lists.append("new_s3_bucket")
print(len(s3_buckets_lists))

s3_buckets_lists.remove("abhishek_demo_bucket")
s3_buckets_lists.remove("ramu_demo_bucket")
print(len(s3_buckets_lists))

