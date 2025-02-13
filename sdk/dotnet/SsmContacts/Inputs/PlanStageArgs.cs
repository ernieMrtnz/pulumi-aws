// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.SsmContacts.Inputs
{

    public sealed class PlanStageArgs : global::Pulumi.ResourceArgs
    {
        [Input("durationInMinutes", required: true)]
        public Input<int> DurationInMinutes { get; set; } = null!;

        [Input("targets")]
        private InputList<Inputs.PlanStageTargetArgs>? _targets;
        public InputList<Inputs.PlanStageTargetArgs> Targets
        {
            get => _targets ?? (_targets = new InputList<Inputs.PlanStageTargetArgs>());
            set => _targets = value;
        }

        public PlanStageArgs()
        {
        }
        public static new PlanStageArgs Empty => new PlanStageArgs();
    }
}
