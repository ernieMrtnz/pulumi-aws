// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.fms.outputs;

import com.pulumi.aws.fms.outputs.PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicy;
import com.pulumi.aws.fms.outputs.PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicy;
import com.pulumi.core.annotations.CustomType;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class PolicySecurityServicePolicyDataPolicyOption {
    /**
     * @return Defines the deployment model to use for the firewall policy. Documented below.
     * 
     */
    private @Nullable PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicy networkFirewallPolicy;
    private @Nullable PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicy thirdPartyFirewallPolicy;

    private PolicySecurityServicePolicyDataPolicyOption() {}
    /**
     * @return Defines the deployment model to use for the firewall policy. Documented below.
     * 
     */
    public Optional<PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicy> networkFirewallPolicy() {
        return Optional.ofNullable(this.networkFirewallPolicy);
    }
    public Optional<PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicy> thirdPartyFirewallPolicy() {
        return Optional.ofNullable(this.thirdPartyFirewallPolicy);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(PolicySecurityServicePolicyDataPolicyOption defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicy networkFirewallPolicy;
        private @Nullable PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicy thirdPartyFirewallPolicy;
        public Builder() {}
        public Builder(PolicySecurityServicePolicyDataPolicyOption defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.networkFirewallPolicy = defaults.networkFirewallPolicy;
    	      this.thirdPartyFirewallPolicy = defaults.thirdPartyFirewallPolicy;
        }

        @CustomType.Setter
        public Builder networkFirewallPolicy(@Nullable PolicySecurityServicePolicyDataPolicyOptionNetworkFirewallPolicy networkFirewallPolicy) {
            this.networkFirewallPolicy = networkFirewallPolicy;
            return this;
        }
        @CustomType.Setter
        public Builder thirdPartyFirewallPolicy(@Nullable PolicySecurityServicePolicyDataPolicyOptionThirdPartyFirewallPolicy thirdPartyFirewallPolicy) {
            this.thirdPartyFirewallPolicy = thirdPartyFirewallPolicy;
            return this;
        }
        public PolicySecurityServicePolicyDataPolicyOption build() {
            final var o = new PolicySecurityServicePolicyDataPolicyOption();
            o.networkFirewallPolicy = networkFirewallPolicy;
            o.thirdPartyFirewallPolicy = thirdPartyFirewallPolicy;
            return o;
        }
    }
}
