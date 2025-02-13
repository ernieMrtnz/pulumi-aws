// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.aws.budgets.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetBudgetPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetBudgetPlainArgs Empty = new GetBudgetPlainArgs();

    /**
     * The ID of the target account for budget. Will use current user&#39;s account_id by default if omitted.
     * 
     */
    @Import(name="accountId")
    private @Nullable String accountId;

    /**
     * @return The ID of the target account for budget. Will use current user&#39;s account_id by default if omitted.
     * 
     */
    public Optional<String> accountId() {
        return Optional.ofNullable(this.accountId);
    }

    /**
     * The name of a budget. Unique within accounts.
     * 
     * The following arguments are optional:
     * 
     */
    @Import(name="name", required=true)
    private String name;

    /**
     * @return The name of a budget. Unique within accounts.
     * 
     * The following arguments are optional:
     * 
     */
    public String name() {
        return this.name;
    }

    /**
     * The prefix of the name of a budget. Unique within accounts.
     * 
     */
    @Import(name="namePrefix")
    private @Nullable String namePrefix;

    /**
     * @return The prefix of the name of a budget. Unique within accounts.
     * 
     */
    public Optional<String> namePrefix() {
        return Optional.ofNullable(this.namePrefix);
    }

    private GetBudgetPlainArgs() {}

    private GetBudgetPlainArgs(GetBudgetPlainArgs $) {
        this.accountId = $.accountId;
        this.name = $.name;
        this.namePrefix = $.namePrefix;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetBudgetPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetBudgetPlainArgs $;

        public Builder() {
            $ = new GetBudgetPlainArgs();
        }

        public Builder(GetBudgetPlainArgs defaults) {
            $ = new GetBudgetPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param accountId The ID of the target account for budget. Will use current user&#39;s account_id by default if omitted.
         * 
         * @return builder
         * 
         */
        public Builder accountId(@Nullable String accountId) {
            $.accountId = accountId;
            return this;
        }

        /**
         * @param name The name of a budget. Unique within accounts.
         * 
         * The following arguments are optional:
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            $.name = name;
            return this;
        }

        /**
         * @param namePrefix The prefix of the name of a budget. Unique within accounts.
         * 
         * @return builder
         * 
         */
        public Builder namePrefix(@Nullable String namePrefix) {
            $.namePrefix = namePrefix;
            return this;
        }

        public GetBudgetPlainArgs build() {
            $.name = Objects.requireNonNull($.name, "expected parameter 'name' to be non-null");
            return $;
        }
    }

}
