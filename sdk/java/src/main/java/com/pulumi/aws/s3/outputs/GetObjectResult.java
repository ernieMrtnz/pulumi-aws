// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.s3.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetObjectResult {
    /**
     * @return Object data (see **limitations above** to understand cases in which this field is actually available)
     * 
     */
    private String body;
    private String bucket;
    /**
     * @return (Optional) Whether or not to use [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html) for SSE-KMS.
     * 
     */
    private Boolean bucketKeyEnabled;
    /**
     * @return Caching behavior along the request/reply chain.
     * 
     */
    private String cacheControl;
    /**
     * @return The base64-encoded, 32-bit CRC32 checksum of the object.
     * 
     */
    private String checksumCrc32;
    /**
     * @return The base64-encoded, 32-bit CRC32C checksum of the object.
     * 
     */
    private String checksumCrc32c;
    private @Nullable String checksumMode;
    /**
     * @return The base64-encoded, 160-bit SHA-1 digest of the object.
     * 
     */
    private String checksumSha1;
    /**
     * @return The base64-encoded, 256-bit SHA-256 digest of the object.
     * 
     */
    private String checksumSha256;
    /**
     * @return Presentational information for the object.
     * 
     */
    private String contentDisposition;
    /**
     * @return What content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
     * 
     */
    private String contentEncoding;
    /**
     * @return Language the content is in.
     * 
     */
    private String contentLanguage;
    /**
     * @return Size of the body in bytes.
     * 
     */
    private Integer contentLength;
    /**
     * @return Standard MIME type describing the format of the object data.
     * 
     */
    private String contentType;
    /**
     * @return [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) generated for the object (an MD5 sum of the object content in case it&#39;s not encrypted)
     * 
     */
    private String etag;
    /**
     * @return If the object expiration is configured (see [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html)), the field includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
     * 
     */
    private String expiration;
    /**
     * @return Date and time at which the object is no longer cacheable.
     * 
     */
    private String expires;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    private String key;
    /**
     * @return Last modified date of the object in RFC1123 format (e.g., `Mon, 02 Jan 2006 15:04:05 MST`)
     * 
     */
    private String lastModified;
    /**
     * @return Map of metadata stored with the object in S3. Keys are always returned in lowercase.
     * 
     */
    private Map<String,String> metadata;
    /**
     * @return Indicates whether this object has an active [legal hold](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-legal-holds). This field is only returned if you have permission to view an object&#39;s legal hold status.
     * 
     */
    private String objectLockLegalHoldStatus;
    /**
     * @return Object lock [retention mode](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-modes) currently in place for this object.
     * 
     */
    private String objectLockMode;
    /**
     * @return The date and time when this object&#39;s object lock will expire.
     * 
     */
    private String objectLockRetainUntilDate;
    private @Nullable String range;
    /**
     * @return If the object is stored using server-side encryption (KMS or Amazon S3-managed encryption key), this field includes the chosen encryption and algorithm used.
     * 
     */
    private String serverSideEncryption;
    /**
     * @return If present, specifies the ID of the Key Management Service (KMS) master encryption key that was used for the object.
     * 
     */
    private String sseKmsKeyId;
    /**
     * @return [Storage class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) information of the object. Available for all objects except for `Standard` storage class objects.
     * 
     */
    private String storageClass;
    /**
     * @return Map of tags assigned to the object.
     * 
     */
    private Map<String,String> tags;
    /**
     * @return Latest version ID of the object returned.
     * 
     */
    private String versionId;
    /**
     * @return If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
     * 
     */
    private String websiteRedirectLocation;

    private GetObjectResult() {}
    /**
     * @return Object data (see **limitations above** to understand cases in which this field is actually available)
     * 
     */
    public String body() {
        return this.body;
    }
    public String bucket() {
        return this.bucket;
    }
    /**
     * @return (Optional) Whether or not to use [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html) for SSE-KMS.
     * 
     */
    public Boolean bucketKeyEnabled() {
        return this.bucketKeyEnabled;
    }
    /**
     * @return Caching behavior along the request/reply chain.
     * 
     */
    public String cacheControl() {
        return this.cacheControl;
    }
    /**
     * @return The base64-encoded, 32-bit CRC32 checksum of the object.
     * 
     */
    public String checksumCrc32() {
        return this.checksumCrc32;
    }
    /**
     * @return The base64-encoded, 32-bit CRC32C checksum of the object.
     * 
     */
    public String checksumCrc32c() {
        return this.checksumCrc32c;
    }
    public Optional<String> checksumMode() {
        return Optional.ofNullable(this.checksumMode);
    }
    /**
     * @return The base64-encoded, 160-bit SHA-1 digest of the object.
     * 
     */
    public String checksumSha1() {
        return this.checksumSha1;
    }
    /**
     * @return The base64-encoded, 256-bit SHA-256 digest of the object.
     * 
     */
    public String checksumSha256() {
        return this.checksumSha256;
    }
    /**
     * @return Presentational information for the object.
     * 
     */
    public String contentDisposition() {
        return this.contentDisposition;
    }
    /**
     * @return What content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
     * 
     */
    public String contentEncoding() {
        return this.contentEncoding;
    }
    /**
     * @return Language the content is in.
     * 
     */
    public String contentLanguage() {
        return this.contentLanguage;
    }
    /**
     * @return Size of the body in bytes.
     * 
     */
    public Integer contentLength() {
        return this.contentLength;
    }
    /**
     * @return Standard MIME type describing the format of the object data.
     * 
     */
    public String contentType() {
        return this.contentType;
    }
    /**
     * @return [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) generated for the object (an MD5 sum of the object content in case it&#39;s not encrypted)
     * 
     */
    public String etag() {
        return this.etag;
    }
    /**
     * @return If the object expiration is configured (see [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html)), the field includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
     * 
     */
    public String expiration() {
        return this.expiration;
    }
    /**
     * @return Date and time at which the object is no longer cacheable.
     * 
     */
    public String expires() {
        return this.expires;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    public String key() {
        return this.key;
    }
    /**
     * @return Last modified date of the object in RFC1123 format (e.g., `Mon, 02 Jan 2006 15:04:05 MST`)
     * 
     */
    public String lastModified() {
        return this.lastModified;
    }
    /**
     * @return Map of metadata stored with the object in S3. Keys are always returned in lowercase.
     * 
     */
    public Map<String,String> metadata() {
        return this.metadata;
    }
    /**
     * @return Indicates whether this object has an active [legal hold](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-legal-holds). This field is only returned if you have permission to view an object&#39;s legal hold status.
     * 
     */
    public String objectLockLegalHoldStatus() {
        return this.objectLockLegalHoldStatus;
    }
    /**
     * @return Object lock [retention mode](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-modes) currently in place for this object.
     * 
     */
    public String objectLockMode() {
        return this.objectLockMode;
    }
    /**
     * @return The date and time when this object&#39;s object lock will expire.
     * 
     */
    public String objectLockRetainUntilDate() {
        return this.objectLockRetainUntilDate;
    }
    public Optional<String> range() {
        return Optional.ofNullable(this.range);
    }
    /**
     * @return If the object is stored using server-side encryption (KMS or Amazon S3-managed encryption key), this field includes the chosen encryption and algorithm used.
     * 
     */
    public String serverSideEncryption() {
        return this.serverSideEncryption;
    }
    /**
     * @return If present, specifies the ID of the Key Management Service (KMS) master encryption key that was used for the object.
     * 
     */
    public String sseKmsKeyId() {
        return this.sseKmsKeyId;
    }
    /**
     * @return [Storage class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html) information of the object. Available for all objects except for `Standard` storage class objects.
     * 
     */
    public String storageClass() {
        return this.storageClass;
    }
    /**
     * @return Map of tags assigned to the object.
     * 
     */
    public Map<String,String> tags() {
        return this.tags;
    }
    /**
     * @return Latest version ID of the object returned.
     * 
     */
    public String versionId() {
        return this.versionId;
    }
    /**
     * @return If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.
     * 
     */
    public String websiteRedirectLocation() {
        return this.websiteRedirectLocation;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetObjectResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String body;
        private String bucket;
        private Boolean bucketKeyEnabled;
        private String cacheControl;
        private String checksumCrc32;
        private String checksumCrc32c;
        private @Nullable String checksumMode;
        private String checksumSha1;
        private String checksumSha256;
        private String contentDisposition;
        private String contentEncoding;
        private String contentLanguage;
        private Integer contentLength;
        private String contentType;
        private String etag;
        private String expiration;
        private String expires;
        private String id;
        private String key;
        private String lastModified;
        private Map<String,String> metadata;
        private String objectLockLegalHoldStatus;
        private String objectLockMode;
        private String objectLockRetainUntilDate;
        private @Nullable String range;
        private String serverSideEncryption;
        private String sseKmsKeyId;
        private String storageClass;
        private Map<String,String> tags;
        private String versionId;
        private String websiteRedirectLocation;
        public Builder() {}
        public Builder(GetObjectResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.body = defaults.body;
    	      this.bucket = defaults.bucket;
    	      this.bucketKeyEnabled = defaults.bucketKeyEnabled;
    	      this.cacheControl = defaults.cacheControl;
    	      this.checksumCrc32 = defaults.checksumCrc32;
    	      this.checksumCrc32c = defaults.checksumCrc32c;
    	      this.checksumMode = defaults.checksumMode;
    	      this.checksumSha1 = defaults.checksumSha1;
    	      this.checksumSha256 = defaults.checksumSha256;
    	      this.contentDisposition = defaults.contentDisposition;
    	      this.contentEncoding = defaults.contentEncoding;
    	      this.contentLanguage = defaults.contentLanguage;
    	      this.contentLength = defaults.contentLength;
    	      this.contentType = defaults.contentType;
    	      this.etag = defaults.etag;
    	      this.expiration = defaults.expiration;
    	      this.expires = defaults.expires;
    	      this.id = defaults.id;
    	      this.key = defaults.key;
    	      this.lastModified = defaults.lastModified;
    	      this.metadata = defaults.metadata;
    	      this.objectLockLegalHoldStatus = defaults.objectLockLegalHoldStatus;
    	      this.objectLockMode = defaults.objectLockMode;
    	      this.objectLockRetainUntilDate = defaults.objectLockRetainUntilDate;
    	      this.range = defaults.range;
    	      this.serverSideEncryption = defaults.serverSideEncryption;
    	      this.sseKmsKeyId = defaults.sseKmsKeyId;
    	      this.storageClass = defaults.storageClass;
    	      this.tags = defaults.tags;
    	      this.versionId = defaults.versionId;
    	      this.websiteRedirectLocation = defaults.websiteRedirectLocation;
        }

        @CustomType.Setter
        public Builder body(String body) {
            this.body = Objects.requireNonNull(body);
            return this;
        }
        @CustomType.Setter
        public Builder bucket(String bucket) {
            this.bucket = Objects.requireNonNull(bucket);
            return this;
        }
        @CustomType.Setter
        public Builder bucketKeyEnabled(Boolean bucketKeyEnabled) {
            this.bucketKeyEnabled = Objects.requireNonNull(bucketKeyEnabled);
            return this;
        }
        @CustomType.Setter
        public Builder cacheControl(String cacheControl) {
            this.cacheControl = Objects.requireNonNull(cacheControl);
            return this;
        }
        @CustomType.Setter
        public Builder checksumCrc32(String checksumCrc32) {
            this.checksumCrc32 = Objects.requireNonNull(checksumCrc32);
            return this;
        }
        @CustomType.Setter
        public Builder checksumCrc32c(String checksumCrc32c) {
            this.checksumCrc32c = Objects.requireNonNull(checksumCrc32c);
            return this;
        }
        @CustomType.Setter
        public Builder checksumMode(@Nullable String checksumMode) {
            this.checksumMode = checksumMode;
            return this;
        }
        @CustomType.Setter
        public Builder checksumSha1(String checksumSha1) {
            this.checksumSha1 = Objects.requireNonNull(checksumSha1);
            return this;
        }
        @CustomType.Setter
        public Builder checksumSha256(String checksumSha256) {
            this.checksumSha256 = Objects.requireNonNull(checksumSha256);
            return this;
        }
        @CustomType.Setter
        public Builder contentDisposition(String contentDisposition) {
            this.contentDisposition = Objects.requireNonNull(contentDisposition);
            return this;
        }
        @CustomType.Setter
        public Builder contentEncoding(String contentEncoding) {
            this.contentEncoding = Objects.requireNonNull(contentEncoding);
            return this;
        }
        @CustomType.Setter
        public Builder contentLanguage(String contentLanguage) {
            this.contentLanguage = Objects.requireNonNull(contentLanguage);
            return this;
        }
        @CustomType.Setter
        public Builder contentLength(Integer contentLength) {
            this.contentLength = Objects.requireNonNull(contentLength);
            return this;
        }
        @CustomType.Setter
        public Builder contentType(String contentType) {
            this.contentType = Objects.requireNonNull(contentType);
            return this;
        }
        @CustomType.Setter
        public Builder etag(String etag) {
            this.etag = Objects.requireNonNull(etag);
            return this;
        }
        @CustomType.Setter
        public Builder expiration(String expiration) {
            this.expiration = Objects.requireNonNull(expiration);
            return this;
        }
        @CustomType.Setter
        public Builder expires(String expires) {
            this.expires = Objects.requireNonNull(expires);
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        @CustomType.Setter
        public Builder key(String key) {
            this.key = Objects.requireNonNull(key);
            return this;
        }
        @CustomType.Setter
        public Builder lastModified(String lastModified) {
            this.lastModified = Objects.requireNonNull(lastModified);
            return this;
        }
        @CustomType.Setter
        public Builder metadata(Map<String,String> metadata) {
            this.metadata = Objects.requireNonNull(metadata);
            return this;
        }
        @CustomType.Setter
        public Builder objectLockLegalHoldStatus(String objectLockLegalHoldStatus) {
            this.objectLockLegalHoldStatus = Objects.requireNonNull(objectLockLegalHoldStatus);
            return this;
        }
        @CustomType.Setter
        public Builder objectLockMode(String objectLockMode) {
            this.objectLockMode = Objects.requireNonNull(objectLockMode);
            return this;
        }
        @CustomType.Setter
        public Builder objectLockRetainUntilDate(String objectLockRetainUntilDate) {
            this.objectLockRetainUntilDate = Objects.requireNonNull(objectLockRetainUntilDate);
            return this;
        }
        @CustomType.Setter
        public Builder range(@Nullable String range) {
            this.range = range;
            return this;
        }
        @CustomType.Setter
        public Builder serverSideEncryption(String serverSideEncryption) {
            this.serverSideEncryption = Objects.requireNonNull(serverSideEncryption);
            return this;
        }
        @CustomType.Setter
        public Builder sseKmsKeyId(String sseKmsKeyId) {
            this.sseKmsKeyId = Objects.requireNonNull(sseKmsKeyId);
            return this;
        }
        @CustomType.Setter
        public Builder storageClass(String storageClass) {
            this.storageClass = Objects.requireNonNull(storageClass);
            return this;
        }
        @CustomType.Setter
        public Builder tags(Map<String,String> tags) {
            this.tags = Objects.requireNonNull(tags);
            return this;
        }
        @CustomType.Setter
        public Builder versionId(String versionId) {
            this.versionId = Objects.requireNonNull(versionId);
            return this;
        }
        @CustomType.Setter
        public Builder websiteRedirectLocation(String websiteRedirectLocation) {
            this.websiteRedirectLocation = Objects.requireNonNull(websiteRedirectLocation);
            return this;
        }
        public GetObjectResult build() {
            final var o = new GetObjectResult();
            o.body = body;
            o.bucket = bucket;
            o.bucketKeyEnabled = bucketKeyEnabled;
            o.cacheControl = cacheControl;
            o.checksumCrc32 = checksumCrc32;
            o.checksumCrc32c = checksumCrc32c;
            o.checksumMode = checksumMode;
            o.checksumSha1 = checksumSha1;
            o.checksumSha256 = checksumSha256;
            o.contentDisposition = contentDisposition;
            o.contentEncoding = contentEncoding;
            o.contentLanguage = contentLanguage;
            o.contentLength = contentLength;
            o.contentType = contentType;
            o.etag = etag;
            o.expiration = expiration;
            o.expires = expires;
            o.id = id;
            o.key = key;
            o.lastModified = lastModified;
            o.metadata = metadata;
            o.objectLockLegalHoldStatus = objectLockLegalHoldStatus;
            o.objectLockMode = objectLockMode;
            o.objectLockRetainUntilDate = objectLockRetainUntilDate;
            o.range = range;
            o.serverSideEncryption = serverSideEncryption;
            o.sseKmsKeyId = sseKmsKeyId;
            o.storageClass = storageClass;
            o.tags = tags;
            o.versionId = versionId;
            o.websiteRedirectLocation = websiteRedirectLocation;
            return o;
        }
    }
}
