// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.chime;

import com.pulumi.aws.Utilities;
import com.pulumi.aws.chime.SdkvoiceSipRuleArgs;
import com.pulumi.aws.chime.inputs.SdkvoiceSipRuleState;
import com.pulumi.aws.chime.outputs.SdkvoiceSipRuleTargetApplication;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * A SIP rule associates your SIP media application with a phone number or a Request URI hostname. You can associate a SIP rule with more than one SIP media application. Each application then runs only that rule.
 * 
 * ## Example Usage
 * ### Basic Usage
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.aws.chime.SdkvoiceSipRule;
 * import com.pulumi.aws.chime.SdkvoiceSipRuleArgs;
 * import com.pulumi.aws.chime.inputs.SdkvoiceSipRuleTargetApplicationArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var example = new SdkvoiceSipRule(&#34;example&#34;, SdkvoiceSipRuleArgs.builder()        
 *             .triggerType(&#34;RequestUriHostname&#34;)
 *             .triggerValue(aws_chime_voice_connector.example-voice-connector().outbound_host_name())
 *             .targetApplications(SdkvoiceSipRuleTargetApplicationArgs.builder()
 *                 .priority(1)
 *                 .sipMediaApplicationId(aws_chimesdkvoice_sip_media_application.example-sma().id())
 *                 .awsRegion(&#34;us-east-1&#34;)
 *                 .build())
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 * ## Import
 * 
 * Using `pulumi import`, import a ChimeSDKVoice SIP Rule using the `id`. For example:
 * 
 * ```sh
 *  $ pulumi import aws:chime/sdkvoiceSipRule:SdkvoiceSipRule example abcdef123456
 * ```
 * 
 */
@ResourceType(type="aws:chime/sdkvoiceSipRule:SdkvoiceSipRule")
public class SdkvoiceSipRule extends com.pulumi.resources.CustomResource {
    /**
     * Enables or disables a rule. You must disable rules before you can delete them.
     * 
     */
    @Export(name="disabled", refs={Boolean.class}, tree="[0]")
    private Output</* @Nullable */ Boolean> disabled;

    /**
     * @return Enables or disables a rule. You must disable rules before you can delete them.
     * 
     */
    public Output<Optional<Boolean>> disabled() {
        return Codegen.optional(this.disabled);
    }
    /**
     * The name of the SIP rule.
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return The name of the SIP rule.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * List of SIP media applications with priority and AWS Region. Only one SIP application per AWS Region can be used. See `target_applications`.
     * 
     */
    @Export(name="targetApplications", refs={List.class,SdkvoiceSipRuleTargetApplication.class}, tree="[0,1]")
    private Output<List<SdkvoiceSipRuleTargetApplication>> targetApplications;

    /**
     * @return List of SIP media applications with priority and AWS Region. Only one SIP application per AWS Region can be used. See `target_applications`.
     * 
     */
    public Output<List<SdkvoiceSipRuleTargetApplication>> targetApplications() {
        return this.targetApplications;
    }
    /**
     * The type of trigger assigned to the SIP rule in `trigger_value`. Valid values are `RequestUriHostname` or `ToPhoneNumber`.
     * 
     */
    @Export(name="triggerType", refs={String.class}, tree="[0]")
    private Output<String> triggerType;

    /**
     * @return The type of trigger assigned to the SIP rule in `trigger_value`. Valid values are `RequestUriHostname` or `ToPhoneNumber`.
     * 
     */
    public Output<String> triggerType() {
        return this.triggerType;
    }
    /**
     * If `trigger_type` is `RequestUriHostname`, the value can be the outbound host name of an Amazon Chime Voice Connector. If `trigger_type` is `ToPhoneNumber`, the value can be a customer-owned phone number in the E164 format. The Sip Media Application specified in the Sip Rule is triggered if the request URI in an incoming SIP request matches the `RequestUriHostname`, or if the &#34;To&#34; header in the incoming SIP request matches the `ToPhoneNumber` value.
     * 
     * The following arguments are optional:
     * 
     */
    @Export(name="triggerValue", refs={String.class}, tree="[0]")
    private Output<String> triggerValue;

    /**
     * @return If `trigger_type` is `RequestUriHostname`, the value can be the outbound host name of an Amazon Chime Voice Connector. If `trigger_type` is `ToPhoneNumber`, the value can be a customer-owned phone number in the E164 format. The Sip Media Application specified in the Sip Rule is triggered if the request URI in an incoming SIP request matches the `RequestUriHostname`, or if the &#34;To&#34; header in the incoming SIP request matches the `ToPhoneNumber` value.
     * 
     * The following arguments are optional:
     * 
     */
    public Output<String> triggerValue() {
        return this.triggerValue;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public SdkvoiceSipRule(String name) {
        this(name, SdkvoiceSipRuleArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public SdkvoiceSipRule(String name, SdkvoiceSipRuleArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public SdkvoiceSipRule(String name, SdkvoiceSipRuleArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("aws:chime/sdkvoiceSipRule:SdkvoiceSipRule", name, args == null ? SdkvoiceSipRuleArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private SdkvoiceSipRule(String name, Output<String> id, @Nullable SdkvoiceSipRuleState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("aws:chime/sdkvoiceSipRule:SdkvoiceSipRule", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static SdkvoiceSipRule get(String name, Output<String> id, @Nullable SdkvoiceSipRuleState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new SdkvoiceSipRule(name, id, state, options);
    }
}
