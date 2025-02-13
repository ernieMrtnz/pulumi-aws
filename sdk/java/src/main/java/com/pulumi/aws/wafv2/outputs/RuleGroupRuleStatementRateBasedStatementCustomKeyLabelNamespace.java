// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.wafv2.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class RuleGroupRuleStatementRateBasedStatementCustomKeyLabelNamespace {
    /**
     * @return The namespace to use for aggregation
     * 
     */
    private String namespace;

    private RuleGroupRuleStatementRateBasedStatementCustomKeyLabelNamespace() {}
    /**
     * @return The namespace to use for aggregation
     * 
     */
    public String namespace() {
        return this.namespace;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(RuleGroupRuleStatementRateBasedStatementCustomKeyLabelNamespace defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String namespace;
        public Builder() {}
        public Builder(RuleGroupRuleStatementRateBasedStatementCustomKeyLabelNamespace defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.namespace = defaults.namespace;
        }

        @CustomType.Setter
        public Builder namespace(String namespace) {
            this.namespace = Objects.requireNonNull(namespace);
            return this;
        }
        public RuleGroupRuleStatementRateBasedStatementCustomKeyLabelNamespace build() {
            final var o = new RuleGroupRuleStatementRateBasedStatementCustomKeyLabelNamespace();
            o.namespace = namespace;
            return o;
        }
    }
}
