// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.S3.Inputs
{

    public sealed class BucketAclV2AccessControlPolicyGrantArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration block for the person being granted permissions. See below.
        /// </summary>
        [Input("grantee")]
        public Input<Inputs.BucketAclV2AccessControlPolicyGrantGranteeArgs>? Grantee { get; set; }

        /// <summary>
        /// Logging permissions assigned to the grantee for the bucket.
        /// </summary>
        [Input("permission", required: true)]
        public Input<string> Permission { get; set; } = null!;

        public BucketAclV2AccessControlPolicyGrantArgs()
        {
        }
        public static new BucketAclV2AccessControlPolicyGrantArgs Empty => new BucketAclV2AccessControlPolicyGrantArgs();
    }
}
