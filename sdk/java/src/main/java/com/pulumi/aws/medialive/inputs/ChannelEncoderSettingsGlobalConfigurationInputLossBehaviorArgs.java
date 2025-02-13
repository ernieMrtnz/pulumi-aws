// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.medialive.inputs;

import com.pulumi.aws.medialive.inputs.ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs extends com.pulumi.resources.ResourceArgs {

    public static final ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs Empty = new ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs();

    @Import(name="blackFrameMsec")
    private @Nullable Output<Integer> blackFrameMsec;

    public Optional<Output<Integer>> blackFrameMsec() {
        return Optional.ofNullable(this.blackFrameMsec);
    }

    @Import(name="inputLossImageColor")
    private @Nullable Output<String> inputLossImageColor;

    public Optional<Output<String>> inputLossImageColor() {
        return Optional.ofNullable(this.inputLossImageColor);
    }

    @Import(name="inputLossImageSlate")
    private @Nullable Output<ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgs> inputLossImageSlate;

    public Optional<Output<ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgs>> inputLossImageSlate() {
        return Optional.ofNullable(this.inputLossImageSlate);
    }

    @Import(name="inputLossImageType")
    private @Nullable Output<String> inputLossImageType;

    public Optional<Output<String>> inputLossImageType() {
        return Optional.ofNullable(this.inputLossImageType);
    }

    @Import(name="repeatFrameMsec")
    private @Nullable Output<Integer> repeatFrameMsec;

    public Optional<Output<Integer>> repeatFrameMsec() {
        return Optional.ofNullable(this.repeatFrameMsec);
    }

    private ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs() {}

    private ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs(ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs $) {
        this.blackFrameMsec = $.blackFrameMsec;
        this.inputLossImageColor = $.inputLossImageColor;
        this.inputLossImageSlate = $.inputLossImageSlate;
        this.inputLossImageType = $.inputLossImageType;
        this.repeatFrameMsec = $.repeatFrameMsec;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs $;

        public Builder() {
            $ = new ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs();
        }

        public Builder(ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs defaults) {
            $ = new ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs(Objects.requireNonNull(defaults));
        }

        public Builder blackFrameMsec(@Nullable Output<Integer> blackFrameMsec) {
            $.blackFrameMsec = blackFrameMsec;
            return this;
        }

        public Builder blackFrameMsec(Integer blackFrameMsec) {
            return blackFrameMsec(Output.of(blackFrameMsec));
        }

        public Builder inputLossImageColor(@Nullable Output<String> inputLossImageColor) {
            $.inputLossImageColor = inputLossImageColor;
            return this;
        }

        public Builder inputLossImageColor(String inputLossImageColor) {
            return inputLossImageColor(Output.of(inputLossImageColor));
        }

        public Builder inputLossImageSlate(@Nullable Output<ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgs> inputLossImageSlate) {
            $.inputLossImageSlate = inputLossImageSlate;
            return this;
        }

        public Builder inputLossImageSlate(ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorInputLossImageSlateArgs inputLossImageSlate) {
            return inputLossImageSlate(Output.of(inputLossImageSlate));
        }

        public Builder inputLossImageType(@Nullable Output<String> inputLossImageType) {
            $.inputLossImageType = inputLossImageType;
            return this;
        }

        public Builder inputLossImageType(String inputLossImageType) {
            return inputLossImageType(Output.of(inputLossImageType));
        }

        public Builder repeatFrameMsec(@Nullable Output<Integer> repeatFrameMsec) {
            $.repeatFrameMsec = repeatFrameMsec;
            return this;
        }

        public Builder repeatFrameMsec(Integer repeatFrameMsec) {
            return repeatFrameMsec(Output.of(repeatFrameMsec));
        }

        public ChannelEncoderSettingsGlobalConfigurationInputLossBehaviorArgs build() {
            return $;
        }
    }

}
