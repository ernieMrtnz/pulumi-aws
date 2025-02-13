// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.opensearch.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;


public final class GetServerlessSecurityPolicyArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetServerlessSecurityPolicyArgs Empty = new GetServerlessSecurityPolicyArgs();

    /**
     * Name of the policy
     * 
     */
    @Import(name="name", required=true)
    private Output<String> name;

    /**
     * @return Name of the policy
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    /**
     * Type of security policy. One of `encryption` or `network`.
     * 
     */
    @Import(name="type", required=true)
    private Output<String> type;

    /**
     * @return Type of security policy. One of `encryption` or `network`.
     * 
     */
    public Output<String> type() {
        return this.type;
    }

    private GetServerlessSecurityPolicyArgs() {}

    private GetServerlessSecurityPolicyArgs(GetServerlessSecurityPolicyArgs $) {
        this.name = $.name;
        this.type = $.type;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetServerlessSecurityPolicyArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetServerlessSecurityPolicyArgs $;

        public Builder() {
            $ = new GetServerlessSecurityPolicyArgs();
        }

        public Builder(GetServerlessSecurityPolicyArgs defaults) {
            $ = new GetServerlessSecurityPolicyArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param name Name of the policy
         * 
         * @return builder
         * 
         */
        public Builder name(Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of the policy
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param type Type of security policy. One of `encryption` or `network`.
         * 
         * @return builder
         * 
         */
        public Builder type(Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type Type of security policy. One of `encryption` or `network`.
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        public GetServerlessSecurityPolicyArgs build() {
            $.name = Objects.requireNonNull($.name, "expected parameter 'name' to be non-null");
            $.type = Objects.requireNonNull($.type, "expected parameter 'type' to be non-null");
            return $;
        }
    }

}
