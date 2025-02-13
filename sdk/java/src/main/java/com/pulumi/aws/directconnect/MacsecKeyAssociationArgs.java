// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.directconnect;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class MacsecKeyAssociationArgs extends com.pulumi.resources.ResourceArgs {

    public static final MacsecKeyAssociationArgs Empty = new MacsecKeyAssociationArgs();

    /**
     * The MAC Security (MACsec) CAK to associate with the dedicated connection. The valid values are 64 hexadecimal characters (0-9, A-E). Required if using `ckn`.
     * 
     */
    @Import(name="cak")
    private @Nullable Output<String> cak;

    /**
     * @return The MAC Security (MACsec) CAK to associate with the dedicated connection. The valid values are 64 hexadecimal characters (0-9, A-E). Required if using `ckn`.
     * 
     */
    public Optional<Output<String>> cak() {
        return Optional.ofNullable(this.cak);
    }

    /**
     * The MAC Security (MACsec) CKN to associate with the dedicated connection. The valid values are 64 hexadecimal characters (0-9, A-E). Required if using `cak`.
     * 
     */
    @Import(name="ckn")
    private @Nullable Output<String> ckn;

    /**
     * @return The MAC Security (MACsec) CKN to associate with the dedicated connection. The valid values are 64 hexadecimal characters (0-9, A-E). Required if using `cak`.
     * 
     */
    public Optional<Output<String>> ckn() {
        return Optional.ofNullable(this.ckn);
    }

    /**
     * The ID of the dedicated Direct Connect connection. The connection must be a dedicated connection in the `AVAILABLE` state.
     * 
     */
    @Import(name="connectionId", required=true)
    private Output<String> connectionId;

    /**
     * @return The ID of the dedicated Direct Connect connection. The connection must be a dedicated connection in the `AVAILABLE` state.
     * 
     */
    public Output<String> connectionId() {
        return this.connectionId;
    }

    /**
     * The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key to associate with the dedicated connection.
     * 
     * &gt; **Note:** `ckn` and `cak` are mutually exclusive with `secret_arn` - these arguments cannot be used together. If you use `ckn` and `cak`, you should not use `secret_arn`. If you use the `secret_arn` argument to reference an existing MAC Security (MACSec) secret key, you should not use `ckn` or `cak`.
     * 
     */
    @Import(name="secretArn")
    private @Nullable Output<String> secretArn;

    /**
     * @return The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key to associate with the dedicated connection.
     * 
     * &gt; **Note:** `ckn` and `cak` are mutually exclusive with `secret_arn` - these arguments cannot be used together. If you use `ckn` and `cak`, you should not use `secret_arn`. If you use the `secret_arn` argument to reference an existing MAC Security (MACSec) secret key, you should not use `ckn` or `cak`.
     * 
     */
    public Optional<Output<String>> secretArn() {
        return Optional.ofNullable(this.secretArn);
    }

    private MacsecKeyAssociationArgs() {}

    private MacsecKeyAssociationArgs(MacsecKeyAssociationArgs $) {
        this.cak = $.cak;
        this.ckn = $.ckn;
        this.connectionId = $.connectionId;
        this.secretArn = $.secretArn;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(MacsecKeyAssociationArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private MacsecKeyAssociationArgs $;

        public Builder() {
            $ = new MacsecKeyAssociationArgs();
        }

        public Builder(MacsecKeyAssociationArgs defaults) {
            $ = new MacsecKeyAssociationArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param cak The MAC Security (MACsec) CAK to associate with the dedicated connection. The valid values are 64 hexadecimal characters (0-9, A-E). Required if using `ckn`.
         * 
         * @return builder
         * 
         */
        public Builder cak(@Nullable Output<String> cak) {
            $.cak = cak;
            return this;
        }

        /**
         * @param cak The MAC Security (MACsec) CAK to associate with the dedicated connection. The valid values are 64 hexadecimal characters (0-9, A-E). Required if using `ckn`.
         * 
         * @return builder
         * 
         */
        public Builder cak(String cak) {
            return cak(Output.of(cak));
        }

        /**
         * @param ckn The MAC Security (MACsec) CKN to associate with the dedicated connection. The valid values are 64 hexadecimal characters (0-9, A-E). Required if using `cak`.
         * 
         * @return builder
         * 
         */
        public Builder ckn(@Nullable Output<String> ckn) {
            $.ckn = ckn;
            return this;
        }

        /**
         * @param ckn The MAC Security (MACsec) CKN to associate with the dedicated connection. The valid values are 64 hexadecimal characters (0-9, A-E). Required if using `cak`.
         * 
         * @return builder
         * 
         */
        public Builder ckn(String ckn) {
            return ckn(Output.of(ckn));
        }

        /**
         * @param connectionId The ID of the dedicated Direct Connect connection. The connection must be a dedicated connection in the `AVAILABLE` state.
         * 
         * @return builder
         * 
         */
        public Builder connectionId(Output<String> connectionId) {
            $.connectionId = connectionId;
            return this;
        }

        /**
         * @param connectionId The ID of the dedicated Direct Connect connection. The connection must be a dedicated connection in the `AVAILABLE` state.
         * 
         * @return builder
         * 
         */
        public Builder connectionId(String connectionId) {
            return connectionId(Output.of(connectionId));
        }

        /**
         * @param secretArn The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key to associate with the dedicated connection.
         * 
         * &gt; **Note:** `ckn` and `cak` are mutually exclusive with `secret_arn` - these arguments cannot be used together. If you use `ckn` and `cak`, you should not use `secret_arn`. If you use the `secret_arn` argument to reference an existing MAC Security (MACSec) secret key, you should not use `ckn` or `cak`.
         * 
         * @return builder
         * 
         */
        public Builder secretArn(@Nullable Output<String> secretArn) {
            $.secretArn = secretArn;
            return this;
        }

        /**
         * @param secretArn The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key to associate with the dedicated connection.
         * 
         * &gt; **Note:** `ckn` and `cak` are mutually exclusive with `secret_arn` - these arguments cannot be used together. If you use `ckn` and `cak`, you should not use `secret_arn`. If you use the `secret_arn` argument to reference an existing MAC Security (MACSec) secret key, you should not use `ckn` or `cak`.
         * 
         * @return builder
         * 
         */
        public Builder secretArn(String secretArn) {
            return secretArn(Output.of(secretArn));
        }

        public MacsecKeyAssociationArgs build() {
            $.connectionId = Objects.requireNonNull($.connectionId, "expected parameter 'connectionId' to be non-null");
            return $;
        }
    }

}
