// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.sesv2.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetEmailIdentityMailFromAttributesResult {
    /**
     * @return The action to take if the required MX record isn&#39;t found when you send an email. Valid values: `USE_DEFAULT_VALUE`, `REJECT_MESSAGE`.
     * 
     */
    private String behaviorOnMxFailure;
    private String emailIdentity;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return The custom MAIL FROM domain that you want the verified identity to use.
     * 
     */
    private String mailFromDomain;

    private GetEmailIdentityMailFromAttributesResult() {}
    /**
     * @return The action to take if the required MX record isn&#39;t found when you send an email. Valid values: `USE_DEFAULT_VALUE`, `REJECT_MESSAGE`.
     * 
     */
    public String behaviorOnMxFailure() {
        return this.behaviorOnMxFailure;
    }
    public String emailIdentity() {
        return this.emailIdentity;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return The custom MAIL FROM domain that you want the verified identity to use.
     * 
     */
    public String mailFromDomain() {
        return this.mailFromDomain;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetEmailIdentityMailFromAttributesResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String behaviorOnMxFailure;
        private String emailIdentity;
        private String id;
        private String mailFromDomain;
        public Builder() {}
        public Builder(GetEmailIdentityMailFromAttributesResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.behaviorOnMxFailure = defaults.behaviorOnMxFailure;
    	      this.emailIdentity = defaults.emailIdentity;
    	      this.id = defaults.id;
    	      this.mailFromDomain = defaults.mailFromDomain;
        }

        @CustomType.Setter
        public Builder behaviorOnMxFailure(String behaviorOnMxFailure) {
            this.behaviorOnMxFailure = Objects.requireNonNull(behaviorOnMxFailure);
            return this;
        }
        @CustomType.Setter
        public Builder emailIdentity(String emailIdentity) {
            this.emailIdentity = Objects.requireNonNull(emailIdentity);
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            this.id = Objects.requireNonNull(id);
            return this;
        }
        @CustomType.Setter
        public Builder mailFromDomain(String mailFromDomain) {
            this.mailFromDomain = Objects.requireNonNull(mailFromDomain);
            return this;
        }
        public GetEmailIdentityMailFromAttributesResult build() {
            final var o = new GetEmailIdentityMailFromAttributesResult();
            o.behaviorOnMxFailure = behaviorOnMxFailure;
            o.emailIdentity = emailIdentity;
            o.id = id;
            o.mailFromDomain = mailFromDomain;
            return o;
        }
    }
}
