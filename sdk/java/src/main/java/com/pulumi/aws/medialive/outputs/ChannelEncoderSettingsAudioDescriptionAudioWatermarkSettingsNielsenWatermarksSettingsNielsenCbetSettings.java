// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.medialive.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettings {
    private String cbetCheckDigitString;
    /**
     * @return Determines the method of CBET insertion mode when prior encoding is detected on the same layer.
     * 
     */
    private String cbetStepaside;
    /**
     * @return CBET source ID to use in the watermark.
     * 
     */
    private String csid;

    private ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettings() {}
    public String cbetCheckDigitString() {
        return this.cbetCheckDigitString;
    }
    /**
     * @return Determines the method of CBET insertion mode when prior encoding is detected on the same layer.
     * 
     */
    public String cbetStepaside() {
        return this.cbetStepaside;
    }
    /**
     * @return CBET source ID to use in the watermark.
     * 
     */
    public String csid() {
        return this.csid;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettings defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String cbetCheckDigitString;
        private String cbetStepaside;
        private String csid;
        public Builder() {}
        public Builder(ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettings defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cbetCheckDigitString = defaults.cbetCheckDigitString;
    	      this.cbetStepaside = defaults.cbetStepaside;
    	      this.csid = defaults.csid;
        }

        @CustomType.Setter
        public Builder cbetCheckDigitString(String cbetCheckDigitString) {
            this.cbetCheckDigitString = Objects.requireNonNull(cbetCheckDigitString);
            return this;
        }
        @CustomType.Setter
        public Builder cbetStepaside(String cbetStepaside) {
            this.cbetStepaside = Objects.requireNonNull(cbetStepaside);
            return this;
        }
        @CustomType.Setter
        public Builder csid(String csid) {
            this.csid = Objects.requireNonNull(csid);
            return this;
        }
        public ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettings build() {
            final var o = new ChannelEncoderSettingsAudioDescriptionAudioWatermarkSettingsNielsenWatermarksSettingsNielsenCbetSettings();
            o.cbetCheckDigitString = cbetCheckDigitString;
            o.cbetStepaside = cbetStepaside;
            o.csid = csid;
            return o;
        }
    }
}
