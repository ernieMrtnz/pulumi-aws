// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.ec2.outputs;

import com.pulumi.aws.ec2.outputs.SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecification;
import com.pulumi.aws.ec2.outputs.SpotFleetRequestLaunchTemplateConfigOverride;
import com.pulumi.core.annotations.CustomType;
import java.util.List;
import java.util.Objects;
import javax.annotation.Nullable;

@CustomType
public final class SpotFleetRequestLaunchTemplateConfig {
    /**
     * @return Launch template specification. See Launch Template Specification below for more details.
     * 
     */
    private SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecification launchTemplateSpecification;
    /**
     * @return One or more override configurations. See Overrides below for more details.
     * 
     */
    private @Nullable List<SpotFleetRequestLaunchTemplateConfigOverride> overrides;

    private SpotFleetRequestLaunchTemplateConfig() {}
    /**
     * @return Launch template specification. See Launch Template Specification below for more details.
     * 
     */
    public SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecification launchTemplateSpecification() {
        return this.launchTemplateSpecification;
    }
    /**
     * @return One or more override configurations. See Overrides below for more details.
     * 
     */
    public List<SpotFleetRequestLaunchTemplateConfigOverride> overrides() {
        return this.overrides == null ? List.of() : this.overrides;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(SpotFleetRequestLaunchTemplateConfig defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecification launchTemplateSpecification;
        private @Nullable List<SpotFleetRequestLaunchTemplateConfigOverride> overrides;
        public Builder() {}
        public Builder(SpotFleetRequestLaunchTemplateConfig defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.launchTemplateSpecification = defaults.launchTemplateSpecification;
    	      this.overrides = defaults.overrides;
        }

        @CustomType.Setter
        public Builder launchTemplateSpecification(SpotFleetRequestLaunchTemplateConfigLaunchTemplateSpecification launchTemplateSpecification) {
            this.launchTemplateSpecification = Objects.requireNonNull(launchTemplateSpecification);
            return this;
        }
        @CustomType.Setter
        public Builder overrides(@Nullable List<SpotFleetRequestLaunchTemplateConfigOverride> overrides) {
            this.overrides = overrides;
            return this;
        }
        public Builder overrides(SpotFleetRequestLaunchTemplateConfigOverride... overrides) {
            return overrides(List.of(overrides));
        }
        public SpotFleetRequestLaunchTemplateConfig build() {
            final var o = new SpotFleetRequestLaunchTemplateConfig();
            o.launchTemplateSpecification = launchTemplateSpecification;
            o.overrides = overrides;
            return o;
        }
    }
}
