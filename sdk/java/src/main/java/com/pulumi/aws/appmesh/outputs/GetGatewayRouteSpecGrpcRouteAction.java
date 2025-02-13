// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.appmesh.outputs;

import com.pulumi.aws.appmesh.outputs.GetGatewayRouteSpecGrpcRouteActionTarget;
import com.pulumi.core.annotations.CustomType;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetGatewayRouteSpecGrpcRouteAction {
    private List<GetGatewayRouteSpecGrpcRouteActionTarget> targets;

    private GetGatewayRouteSpecGrpcRouteAction() {}
    public List<GetGatewayRouteSpecGrpcRouteActionTarget> targets() {
        return this.targets;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetGatewayRouteSpecGrpcRouteAction defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<GetGatewayRouteSpecGrpcRouteActionTarget> targets;
        public Builder() {}
        public Builder(GetGatewayRouteSpecGrpcRouteAction defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.targets = defaults.targets;
        }

        @CustomType.Setter
        public Builder targets(List<GetGatewayRouteSpecGrpcRouteActionTarget> targets) {
            this.targets = Objects.requireNonNull(targets);
            return this;
        }
        public Builder targets(GetGatewayRouteSpecGrpcRouteActionTarget... targets) {
            return targets(List.of(targets));
        }
        public GetGatewayRouteSpecGrpcRouteAction build() {
            final var o = new GetGatewayRouteSpecGrpcRouteAction();
            o.targets = targets;
            return o;
        }
    }
}
