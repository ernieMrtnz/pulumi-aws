// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.finspace.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class KxClusterCodeArgs extends com.pulumi.resources.ResourceArgs {

    public static final KxClusterCodeArgs Empty = new KxClusterCodeArgs();

    /**
     * Unique name for the S3 bucket.
     * 
     */
    @Import(name="s3Bucket", required=true)
    private Output<String> s3Bucket;

    /**
     * @return Unique name for the S3 bucket.
     * 
     */
    public Output<String> s3Bucket() {
        return this.s3Bucket;
    }

    /**
     * Full S3 path (excluding bucket) to the .zip file that contains the code to be loaded onto the cluster when it’s started.
     * 
     */
    @Import(name="s3Key", required=true)
    private Output<String> s3Key;

    /**
     * @return Full S3 path (excluding bucket) to the .zip file that contains the code to be loaded onto the cluster when it’s started.
     * 
     */
    public Output<String> s3Key() {
        return this.s3Key;
    }

    /**
     * Version of an S3 Object.
     * 
     */
    @Import(name="s3ObjectVersion")
    private @Nullable Output<String> s3ObjectVersion;

    /**
     * @return Version of an S3 Object.
     * 
     */
    public Optional<Output<String>> s3ObjectVersion() {
        return Optional.ofNullable(this.s3ObjectVersion);
    }

    private KxClusterCodeArgs() {}

    private KxClusterCodeArgs(KxClusterCodeArgs $) {
        this.s3Bucket = $.s3Bucket;
        this.s3Key = $.s3Key;
        this.s3ObjectVersion = $.s3ObjectVersion;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(KxClusterCodeArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private KxClusterCodeArgs $;

        public Builder() {
            $ = new KxClusterCodeArgs();
        }

        public Builder(KxClusterCodeArgs defaults) {
            $ = new KxClusterCodeArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param s3Bucket Unique name for the S3 bucket.
         * 
         * @return builder
         * 
         */
        public Builder s3Bucket(Output<String> s3Bucket) {
            $.s3Bucket = s3Bucket;
            return this;
        }

        /**
         * @param s3Bucket Unique name for the S3 bucket.
         * 
         * @return builder
         * 
         */
        public Builder s3Bucket(String s3Bucket) {
            return s3Bucket(Output.of(s3Bucket));
        }

        /**
         * @param s3Key Full S3 path (excluding bucket) to the .zip file that contains the code to be loaded onto the cluster when it’s started.
         * 
         * @return builder
         * 
         */
        public Builder s3Key(Output<String> s3Key) {
            $.s3Key = s3Key;
            return this;
        }

        /**
         * @param s3Key Full S3 path (excluding bucket) to the .zip file that contains the code to be loaded onto the cluster when it’s started.
         * 
         * @return builder
         * 
         */
        public Builder s3Key(String s3Key) {
            return s3Key(Output.of(s3Key));
        }

        /**
         * @param s3ObjectVersion Version of an S3 Object.
         * 
         * @return builder
         * 
         */
        public Builder s3ObjectVersion(@Nullable Output<String> s3ObjectVersion) {
            $.s3ObjectVersion = s3ObjectVersion;
            return this;
        }

        /**
         * @param s3ObjectVersion Version of an S3 Object.
         * 
         * @return builder
         * 
         */
        public Builder s3ObjectVersion(String s3ObjectVersion) {
            return s3ObjectVersion(Output.of(s3ObjectVersion));
        }

        public KxClusterCodeArgs build() {
            $.s3Bucket = Objects.requireNonNull($.s3Bucket, "expected parameter 's3Bucket' to be non-null");
            $.s3Key = Objects.requireNonNull($.s3Key, "expected parameter 's3Key' to be non-null");
            return $;
        }
    }

}
