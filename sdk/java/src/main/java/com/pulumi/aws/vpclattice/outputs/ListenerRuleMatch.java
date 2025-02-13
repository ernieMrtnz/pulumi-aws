// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.vpclattice.outputs;

import com.pulumi.aws.vpclattice.outputs.ListenerRuleMatchHttpMatch;
import com.pulumi.core.annotations.CustomType;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class ListenerRuleMatch {
    /**
     * @return The HTTP criteria that a rule must match.
     * 
     */
    private @Nullable ListenerRuleMatchHttpMatch httpMatch;

    private ListenerRuleMatch() {}
    /**
     * @return The HTTP criteria that a rule must match.
     * 
     */
    public Optional<ListenerRuleMatchHttpMatch> httpMatch() {
        return Optional.ofNullable(this.httpMatch);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ListenerRuleMatch defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable ListenerRuleMatchHttpMatch httpMatch;
        public Builder() {}
        public Builder(ListenerRuleMatch defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.httpMatch = defaults.httpMatch;
        }

        @CustomType.Setter
        public Builder httpMatch(@Nullable ListenerRuleMatchHttpMatch httpMatch) {
            this.httpMatch = httpMatch;
            return this;
        }
        public ListenerRuleMatch build() {
            final var o = new ListenerRuleMatch();
            o.httpMatch = httpMatch;
            return o;
        }
    }
}
