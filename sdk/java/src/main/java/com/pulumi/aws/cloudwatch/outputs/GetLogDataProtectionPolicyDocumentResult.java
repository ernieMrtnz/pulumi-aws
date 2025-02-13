// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.cloudwatch.outputs;

import com.pulumi.aws.cloudwatch.outputs.GetLogDataProtectionPolicyDocumentStatement;
import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetLogDataProtectionPolicyDocumentResult {
    private @Nullable String description;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return Standard JSON policy document rendered based on the arguments above.
     * 
     */
    private String json;
    private String name;
    private List<GetLogDataProtectionPolicyDocumentStatement> statements;
    private @Nullable String version;

    private GetLogDataProtectionPolicyDocumentResult() {}
    public Optional<String> description() {
        return Optional.ofNullable(this.description);
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Standard JSON policy document rendered based on the arguments above.
     * 
     */
    public String json() {
        return this.json;
    }
    public String name() {
        return this.name;
    }
    public List<GetLogDataProtectionPolicyDocumentStatement> statements() {
        return this.statements;
    }
    public Optional<String> version() {
        return Optional.ofNullable(this.version);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetLogDataProtectionPolicyDocumentResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String description;
        private String id;
        private String json;
        private String name;
        private List<GetLogDataProtectionPolicyDocumentStatement> statements;
        private @Nullable String version;
        public Builder() {}
        public Builder(GetLogDataProtectionPolicyDocumentResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.description = defaults.description;
    	      this.id = defaults.id;
    	      this.json = defaults.json;
    	      this.name = defaults.name;
    	      this.statements = defaults.statements;
    	      this.version = defaults.version;
        }

        @CustomType.Setter
        public Builder description(@Nullable String description) {
            this.description = description;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        @CustomType.Setter
        public Builder json(String json) {
            this.json = Objects.requireNonNull(json);
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            this.name = Objects.requireNonNull(name);
            return this;
        }
        @CustomType.Setter
        public Builder statements(List<GetLogDataProtectionPolicyDocumentStatement> statements) {
            this.statements = Objects.requireNonNull(statements);
            return this;
        }
        public Builder statements(GetLogDataProtectionPolicyDocumentStatement... statements) {
            return statements(List.of(statements));
        }
        @CustomType.Setter
        public Builder version(@Nullable String version) {
            this.version = version;
            return this;
        }
        public GetLogDataProtectionPolicyDocumentResult build() {
            final var o = new GetLogDataProtectionPolicyDocumentResult();
            o.description = description;
            o.id = id;
            o.json = json;
            o.name = name;
            o.statements = statements;
            o.version = version;
            return o;
        }
    }
}
