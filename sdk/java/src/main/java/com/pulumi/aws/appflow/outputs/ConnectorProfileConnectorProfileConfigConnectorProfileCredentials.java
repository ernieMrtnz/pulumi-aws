// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.appflow.outputs;

import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva;
import com.pulumi.aws.appflow.outputs.ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk;
import com.pulumi.core.annotations.CustomType;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class ConnectorProfileConnectorProfileConfigConnectorProfileCredentials {
    /**
     * @return The connector-specific credentials required when using Amplitude. See Amplitude Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude amplitude;
    /**
     * @return The connector-specific profile credentials required when using the custom connector. See Custom Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector customConnector;
    /**
     * @return Connector-specific credentials required when using Datadog. See Datadog Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog datadog;
    /**
     * @return The connector-specific credentials required when using Dynatrace. See Dynatrace Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace dynatrace;
    /**
     * @return The connector-specific credentials required when using Google Analytics. See Google Analytics Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics googleAnalytics;
    /**
     * @return The connector-specific credentials required when using Amazon Honeycode. See Honeycode Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode honeycode;
    /**
     * @return The connector-specific credentials required when using Infor Nexus. See Infor Nexus Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus inforNexus;
    /**
     * @return Connector-specific credentials required when using Marketo. See Marketo Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo marketo;
    /**
     * @return Connector-specific credentials required when using Amazon Redshift. See Redshift Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift redshift;
    /**
     * @return The connector-specific credentials required when using Salesforce. See Salesforce Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce salesforce;
    /**
     * @return The connector-specific credentials required when using SAPOData. See SAPOData Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData sapoData;
    /**
     * @return The connector-specific credentials required when using ServiceNow. See ServiceNow Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow serviceNow;
    /**
     * @return Connector-specific credentials required when using Singular. See Singular Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular singular;
    /**
     * @return Connector-specific credentials required when using Slack. See Slack Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack slack;
    /**
     * @return The connector-specific credentials required when using Snowflake. See Snowflake Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake snowflake;
    /**
     * @return The connector-specific credentials required when using Trend Micro. See Trend Micro Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro trendmicro;
    /**
     * @return Connector-specific credentials required when using Veeva. See Veeva Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva veeva;
    /**
     * @return Connector-specific credentials required when using Zendesk. See Zendesk Connector Profile Credentials for more details.
     * 
     */
    private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk zendesk;

    private ConnectorProfileConnectorProfileConfigConnectorProfileCredentials() {}
    /**
     * @return The connector-specific credentials required when using Amplitude. See Amplitude Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude> amplitude() {
        return Optional.ofNullable(this.amplitude);
    }
    /**
     * @return The connector-specific profile credentials required when using the custom connector. See Custom Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector> customConnector() {
        return Optional.ofNullable(this.customConnector);
    }
    /**
     * @return Connector-specific credentials required when using Datadog. See Datadog Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog> datadog() {
        return Optional.ofNullable(this.datadog);
    }
    /**
     * @return The connector-specific credentials required when using Dynatrace. See Dynatrace Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace> dynatrace() {
        return Optional.ofNullable(this.dynatrace);
    }
    /**
     * @return The connector-specific credentials required when using Google Analytics. See Google Analytics Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics> googleAnalytics() {
        return Optional.ofNullable(this.googleAnalytics);
    }
    /**
     * @return The connector-specific credentials required when using Amazon Honeycode. See Honeycode Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode> honeycode() {
        return Optional.ofNullable(this.honeycode);
    }
    /**
     * @return The connector-specific credentials required when using Infor Nexus. See Infor Nexus Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus> inforNexus() {
        return Optional.ofNullable(this.inforNexus);
    }
    /**
     * @return Connector-specific credentials required when using Marketo. See Marketo Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo> marketo() {
        return Optional.ofNullable(this.marketo);
    }
    /**
     * @return Connector-specific credentials required when using Amazon Redshift. See Redshift Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift> redshift() {
        return Optional.ofNullable(this.redshift);
    }
    /**
     * @return The connector-specific credentials required when using Salesforce. See Salesforce Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce> salesforce() {
        return Optional.ofNullable(this.salesforce);
    }
    /**
     * @return The connector-specific credentials required when using SAPOData. See SAPOData Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData> sapoData() {
        return Optional.ofNullable(this.sapoData);
    }
    /**
     * @return The connector-specific credentials required when using ServiceNow. See ServiceNow Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow> serviceNow() {
        return Optional.ofNullable(this.serviceNow);
    }
    /**
     * @return Connector-specific credentials required when using Singular. See Singular Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular> singular() {
        return Optional.ofNullable(this.singular);
    }
    /**
     * @return Connector-specific credentials required when using Slack. See Slack Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack> slack() {
        return Optional.ofNullable(this.slack);
    }
    /**
     * @return The connector-specific credentials required when using Snowflake. See Snowflake Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake> snowflake() {
        return Optional.ofNullable(this.snowflake);
    }
    /**
     * @return The connector-specific credentials required when using Trend Micro. See Trend Micro Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro> trendmicro() {
        return Optional.ofNullable(this.trendmicro);
    }
    /**
     * @return Connector-specific credentials required when using Veeva. See Veeva Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva> veeva() {
        return Optional.ofNullable(this.veeva);
    }
    /**
     * @return Connector-specific credentials required when using Zendesk. See Zendesk Connector Profile Credentials for more details.
     * 
     */
    public Optional<ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk> zendesk() {
        return Optional.ofNullable(this.zendesk);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ConnectorProfileConnectorProfileConfigConnectorProfileCredentials defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude amplitude;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector customConnector;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog datadog;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace dynatrace;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics googleAnalytics;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode honeycode;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus inforNexus;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo marketo;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift redshift;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce salesforce;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData sapoData;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow serviceNow;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular singular;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack slack;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake snowflake;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro trendmicro;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva veeva;
        private @Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk zendesk;
        public Builder() {}
        public Builder(ConnectorProfileConnectorProfileConfigConnectorProfileCredentials defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.amplitude = defaults.amplitude;
    	      this.customConnector = defaults.customConnector;
    	      this.datadog = defaults.datadog;
    	      this.dynatrace = defaults.dynatrace;
    	      this.googleAnalytics = defaults.googleAnalytics;
    	      this.honeycode = defaults.honeycode;
    	      this.inforNexus = defaults.inforNexus;
    	      this.marketo = defaults.marketo;
    	      this.redshift = defaults.redshift;
    	      this.salesforce = defaults.salesforce;
    	      this.sapoData = defaults.sapoData;
    	      this.serviceNow = defaults.serviceNow;
    	      this.singular = defaults.singular;
    	      this.slack = defaults.slack;
    	      this.snowflake = defaults.snowflake;
    	      this.trendmicro = defaults.trendmicro;
    	      this.veeva = defaults.veeva;
    	      this.zendesk = defaults.zendesk;
        }

        @CustomType.Setter
        public Builder amplitude(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsAmplitude amplitude) {
            this.amplitude = amplitude;
            return this;
        }
        @CustomType.Setter
        public Builder customConnector(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsCustomConnector customConnector) {
            this.customConnector = customConnector;
            return this;
        }
        @CustomType.Setter
        public Builder datadog(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDatadog datadog) {
            this.datadog = datadog;
            return this;
        }
        @CustomType.Setter
        public Builder dynatrace(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsDynatrace dynatrace) {
            this.dynatrace = dynatrace;
            return this;
        }
        @CustomType.Setter
        public Builder googleAnalytics(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsGoogleAnalytics googleAnalytics) {
            this.googleAnalytics = googleAnalytics;
            return this;
        }
        @CustomType.Setter
        public Builder honeycode(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsHoneycode honeycode) {
            this.honeycode = honeycode;
            return this;
        }
        @CustomType.Setter
        public Builder inforNexus(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsInforNexus inforNexus) {
            this.inforNexus = inforNexus;
            return this;
        }
        @CustomType.Setter
        public Builder marketo(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsMarketo marketo) {
            this.marketo = marketo;
            return this;
        }
        @CustomType.Setter
        public Builder redshift(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsRedshift redshift) {
            this.redshift = redshift;
            return this;
        }
        @CustomType.Setter
        public Builder salesforce(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSalesforce salesforce) {
            this.salesforce = salesforce;
            return this;
        }
        @CustomType.Setter
        public Builder sapoData(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSapoData sapoData) {
            this.sapoData = sapoData;
            return this;
        }
        @CustomType.Setter
        public Builder serviceNow(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsServiceNow serviceNow) {
            this.serviceNow = serviceNow;
            return this;
        }
        @CustomType.Setter
        public Builder singular(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSingular singular) {
            this.singular = singular;
            return this;
        }
        @CustomType.Setter
        public Builder slack(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSlack slack) {
            this.slack = slack;
            return this;
        }
        @CustomType.Setter
        public Builder snowflake(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsSnowflake snowflake) {
            this.snowflake = snowflake;
            return this;
        }
        @CustomType.Setter
        public Builder trendmicro(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsTrendmicro trendmicro) {
            this.trendmicro = trendmicro;
            return this;
        }
        @CustomType.Setter
        public Builder veeva(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsVeeva veeva) {
            this.veeva = veeva;
            return this;
        }
        @CustomType.Setter
        public Builder zendesk(@Nullable ConnectorProfileConnectorProfileConfigConnectorProfileCredentialsZendesk zendesk) {
            this.zendesk = zendesk;
            return this;
        }
        public ConnectorProfileConnectorProfileConfigConnectorProfileCredentials build() {
            final var o = new ConnectorProfileConnectorProfileConfigConnectorProfileCredentials();
            o.amplitude = amplitude;
            o.customConnector = customConnector;
            o.datadog = datadog;
            o.dynatrace = dynatrace;
            o.googleAnalytics = googleAnalytics;
            o.honeycode = honeycode;
            o.inforNexus = inforNexus;
            o.marketo = marketo;
            o.redshift = redshift;
            o.salesforce = salesforce;
            o.sapoData = sapoData;
            o.serviceNow = serviceNow;
            o.singular = singular;
            o.slack = slack;
            o.snowflake = snowflake;
            o.trendmicro = trendmicro;
            o.veeva = veeva;
            o.zendesk = zendesk;
            return o;
        }
    }
}
