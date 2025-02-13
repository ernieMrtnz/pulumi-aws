// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.rds.outputs;

import com.pulumi.aws.rds.outputs.GetInstancesFilter;
import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import javax.annotation.Nullable;

@CustomType
public final class GetInstancesResult {
    private @Nullable List<GetInstancesFilter> filters;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return ARNs of the matched RDS instances.
     * 
     */
    private List<String> instanceArns;
    /**
     * @return Identifiers of the matched RDS instances.
     * 
     */
    private List<String> instanceIdentifiers;
    private Map<String,String> tags;

    private GetInstancesResult() {}
    public List<GetInstancesFilter> filters() {
        return this.filters == null ? List.of() : this.filters;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return ARNs of the matched RDS instances.
     * 
     */
    public List<String> instanceArns() {
        return this.instanceArns;
    }
    /**
     * @return Identifiers of the matched RDS instances.
     * 
     */
    public List<String> instanceIdentifiers() {
        return this.instanceIdentifiers;
    }
    public Map<String,String> tags() {
        return this.tags;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetInstancesResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable List<GetInstancesFilter> filters;
        private String id;
        private List<String> instanceArns;
        private List<String> instanceIdentifiers;
        private Map<String,String> tags;
        public Builder() {}
        public Builder(GetInstancesResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.filters = defaults.filters;
    	      this.id = defaults.id;
    	      this.instanceArns = defaults.instanceArns;
    	      this.instanceIdentifiers = defaults.instanceIdentifiers;
    	      this.tags = defaults.tags;
        }

        @CustomType.Setter
        public Builder filters(@Nullable List<GetInstancesFilter> filters) {
            this.filters = filters;
            return this;
        }
        public Builder filters(GetInstancesFilter... filters) {
            return filters(List.of(filters));
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        @CustomType.Setter
        public Builder instanceArns(List<String> instanceArns) {
            this.instanceArns = Objects.requireNonNull(instanceArns);
            return this;
        }
        public Builder instanceArns(String... instanceArns) {
            return instanceArns(List.of(instanceArns));
        }
        @CustomType.Setter
        public Builder instanceIdentifiers(List<String> instanceIdentifiers) {
            this.instanceIdentifiers = Objects.requireNonNull(instanceIdentifiers);
            return this;
        }
        public Builder instanceIdentifiers(String... instanceIdentifiers) {
            return instanceIdentifiers(List.of(instanceIdentifiers));
        }
        @CustomType.Setter
        public Builder tags(Map<String,String> tags) {
            this.tags = Objects.requireNonNull(tags);
            return this;
        }
        public GetInstancesResult build() {
            final var o = new GetInstancesResult();
            o.filters = filters;
            o.id = id;
            o.instanceArns = instanceArns;
            o.instanceIdentifiers = instanceIdentifiers;
            o.tags = tags;
            return o;
        }
    }
}
