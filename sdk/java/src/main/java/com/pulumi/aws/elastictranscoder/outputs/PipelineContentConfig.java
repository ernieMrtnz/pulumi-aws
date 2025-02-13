// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.elastictranscoder.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class PipelineContentConfig {
    /**
     * @return The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.
     * 
     */
    private @Nullable String bucket;
    /**
     * @return The Amazon S3 storage class, `Standard` or `ReducedRedundancy`, that you want Elastic Transcoder to assign to the files and playlists that it stores in your Amazon S3 bucket.
     * 
     */
    private @Nullable String storageClass;

    private PipelineContentConfig() {}
    /**
     * @return The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.
     * 
     */
    public Optional<String> bucket() {
        return Optional.ofNullable(this.bucket);
    }
    /**
     * @return The Amazon S3 storage class, `Standard` or `ReducedRedundancy`, that you want Elastic Transcoder to assign to the files and playlists that it stores in your Amazon S3 bucket.
     * 
     */
    public Optional<String> storageClass() {
        return Optional.ofNullable(this.storageClass);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(PipelineContentConfig defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String bucket;
        private @Nullable String storageClass;
        public Builder() {}
        public Builder(PipelineContentConfig defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.bucket = defaults.bucket;
    	      this.storageClass = defaults.storageClass;
        }

        @CustomType.Setter
        public Builder bucket(@Nullable String bucket) {
            this.bucket = bucket;
            return this;
        }
        @CustomType.Setter
        public Builder storageClass(@Nullable String storageClass) {
            this.storageClass = storageClass;
            return this;
        }
        public PipelineContentConfig build() {
            final var o = new PipelineContentConfig();
            o.bucket = bucket;
            o.storageClass = storageClass;
            return o;
        }
    }
}
