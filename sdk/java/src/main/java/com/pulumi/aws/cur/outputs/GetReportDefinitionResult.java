// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.cur.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetReportDefinitionResult {
    /**
     * @return A list of additional artifacts.
     * 
     */
    private List<String> additionalArtifacts;
    /**
     * @return A list of schema elements.
     * 
     */
    private List<String> additionalSchemaElements;
    /**
     * @return Preferred format for report.
     * 
     */
    private String compression;
    /**
     * @return Preferred compression format for report.
     * 
     */
    private String format;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return If true reports are updated after they have been finalized.
     * 
     */
    private Boolean refreshClosedReports;
    private String reportName;
    /**
     * @return Overwrite the previous version of each report or to deliver the report in addition to the previous versions.
     * 
     */
    private String reportVersioning;
    /**
     * @return Name of customer S3 bucket.
     * 
     */
    private String s3Bucket;
    /**
     * @return Preferred report path prefix.
     * 
     */
    private String s3Prefix;
    /**
     * @return Region of customer S3 bucket.
     * 
     */
    private String s3Region;
    /**
     * @return Frequency on which report data are measured and displayed.
     * 
     */
    private String timeUnit;

    private GetReportDefinitionResult() {}
    /**
     * @return A list of additional artifacts.
     * 
     */
    public List<String> additionalArtifacts() {
        return this.additionalArtifacts;
    }
    /**
     * @return A list of schema elements.
     * 
     */
    public List<String> additionalSchemaElements() {
        return this.additionalSchemaElements;
    }
    /**
     * @return Preferred format for report.
     * 
     */
    public String compression() {
        return this.compression;
    }
    /**
     * @return Preferred compression format for report.
     * 
     */
    public String format() {
        return this.format;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return If true reports are updated after they have been finalized.
     * 
     */
    public Boolean refreshClosedReports() {
        return this.refreshClosedReports;
    }
    public String reportName() {
        return this.reportName;
    }
    /**
     * @return Overwrite the previous version of each report or to deliver the report in addition to the previous versions.
     * 
     */
    public String reportVersioning() {
        return this.reportVersioning;
    }
    /**
     * @return Name of customer S3 bucket.
     * 
     */
    public String s3Bucket() {
        return this.s3Bucket;
    }
    /**
     * @return Preferred report path prefix.
     * 
     */
    public String s3Prefix() {
        return this.s3Prefix;
    }
    /**
     * @return Region of customer S3 bucket.
     * 
     */
    public String s3Region() {
        return this.s3Region;
    }
    /**
     * @return Frequency on which report data are measured and displayed.
     * 
     */
    public String timeUnit() {
        return this.timeUnit;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetReportDefinitionResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<String> additionalArtifacts;
        private List<String> additionalSchemaElements;
        private String compression;
        private String format;
        private String id;
        private Boolean refreshClosedReports;
        private String reportName;
        private String reportVersioning;
        private String s3Bucket;
        private String s3Prefix;
        private String s3Region;
        private String timeUnit;
        public Builder() {}
        public Builder(GetReportDefinitionResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.additionalArtifacts = defaults.additionalArtifacts;
    	      this.additionalSchemaElements = defaults.additionalSchemaElements;
    	      this.compression = defaults.compression;
    	      this.format = defaults.format;
    	      this.id = defaults.id;
    	      this.refreshClosedReports = defaults.refreshClosedReports;
    	      this.reportName = defaults.reportName;
    	      this.reportVersioning = defaults.reportVersioning;
    	      this.s3Bucket = defaults.s3Bucket;
    	      this.s3Prefix = defaults.s3Prefix;
    	      this.s3Region = defaults.s3Region;
    	      this.timeUnit = defaults.timeUnit;
        }

        @CustomType.Setter
        public Builder additionalArtifacts(List<String> additionalArtifacts) {
            this.additionalArtifacts = Objects.requireNonNull(additionalArtifacts);
            return this;
        }
        public Builder additionalArtifacts(String... additionalArtifacts) {
            return additionalArtifacts(List.of(additionalArtifacts));
        }
        @CustomType.Setter
        public Builder additionalSchemaElements(List<String> additionalSchemaElements) {
            this.additionalSchemaElements = Objects.requireNonNull(additionalSchemaElements);
            return this;
        }
        public Builder additionalSchemaElements(String... additionalSchemaElements) {
            return additionalSchemaElements(List.of(additionalSchemaElements));
        }
        @CustomType.Setter
        public Builder compression(String compression) {
            this.compression = Objects.requireNonNull(compression);
            return this;
        }
        @CustomType.Setter
        public Builder format(String format) {
            this.format = Objects.requireNonNull(format);
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        @CustomType.Setter
        public Builder refreshClosedReports(Boolean refreshClosedReports) {
            this.refreshClosedReports = Objects.requireNonNull(refreshClosedReports);
            return this;
        }
        @CustomType.Setter
        public Builder reportName(String reportName) {
            this.reportName = Objects.requireNonNull(reportName);
            return this;
        }
        @CustomType.Setter
        public Builder reportVersioning(String reportVersioning) {
            this.reportVersioning = Objects.requireNonNull(reportVersioning);
            return this;
        }
        @CustomType.Setter
        public Builder s3Bucket(String s3Bucket) {
            this.s3Bucket = Objects.requireNonNull(s3Bucket);
            return this;
        }
        @CustomType.Setter
        public Builder s3Prefix(String s3Prefix) {
            this.s3Prefix = Objects.requireNonNull(s3Prefix);
            return this;
        }
        @CustomType.Setter
        public Builder s3Region(String s3Region) {
            this.s3Region = Objects.requireNonNull(s3Region);
            return this;
        }
        @CustomType.Setter
        public Builder timeUnit(String timeUnit) {
            this.timeUnit = Objects.requireNonNull(timeUnit);
            return this;
        }
        public GetReportDefinitionResult build() {
            final var o = new GetReportDefinitionResult();
            o.additionalArtifacts = additionalArtifacts;
            o.additionalSchemaElements = additionalSchemaElements;
            o.compression = compression;
            o.format = format;
            o.id = id;
            o.refreshClosedReports = refreshClosedReports;
            o.reportName = reportName;
            o.reportVersioning = reportVersioning;
            o.s3Bucket = s3Bucket;
            o.s3Prefix = s3Prefix;
            o.s3Region = s3Region;
            o.timeUnit = timeUnit;
            return o;
        }
    }
}
