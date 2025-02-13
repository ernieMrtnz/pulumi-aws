// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Provides a Glue Data Catalog Encryption Settings resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/glue"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := glue.NewDataCatalogEncryptionSettings(ctx, "example", &glue.DataCatalogEncryptionSettingsArgs{
//				DataCatalogEncryptionSettings: &glue.DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsArgs{
//					ConnectionPasswordEncryption: &glue.DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsConnectionPasswordEncryptionArgs{
//						AwsKmsKeyId:                       pulumi.Any(aws_kms_key.Test.Arn),
//						ReturnConnectionPasswordEncrypted: pulumi.Bool(true),
//					},
//					EncryptionAtRest: &glue.DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsEncryptionAtRestArgs{
//						CatalogEncryptionMode: pulumi.String("SSE-KMS"),
//						SseAwsKmsKeyId:        pulumi.Any(aws_kms_key.Test.Arn),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Using `pulumi import`, import Glue Data Catalog Encryption Settings using `CATALOG-ID` (AWS account ID if not custom). For example:
//
// ```sh
//
//	$ pulumi import aws:glue/dataCatalogEncryptionSettings:DataCatalogEncryptionSettings example 123456789012
//
// ```
type DataCatalogEncryptionSettings struct {
	pulumi.CustomResourceState

	// The ID of the Data Catalog to set the security configuration for. If none is provided, the AWS account ID is used by default.
	CatalogId pulumi.StringOutput `pulumi:"catalogId"`
	// The security configuration to set. see Data Catalog Encryption Settings.
	DataCatalogEncryptionSettings DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsOutput `pulumi:"dataCatalogEncryptionSettings"`
}

// NewDataCatalogEncryptionSettings registers a new resource with the given unique name, arguments, and options.
func NewDataCatalogEncryptionSettings(ctx *pulumi.Context,
	name string, args *DataCatalogEncryptionSettingsArgs, opts ...pulumi.ResourceOption) (*DataCatalogEncryptionSettings, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DataCatalogEncryptionSettings == nil {
		return nil, errors.New("invalid value for required argument 'DataCatalogEncryptionSettings'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DataCatalogEncryptionSettings
	err := ctx.RegisterResource("aws:glue/dataCatalogEncryptionSettings:DataCatalogEncryptionSettings", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDataCatalogEncryptionSettings gets an existing DataCatalogEncryptionSettings resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDataCatalogEncryptionSettings(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DataCatalogEncryptionSettingsState, opts ...pulumi.ResourceOption) (*DataCatalogEncryptionSettings, error) {
	var resource DataCatalogEncryptionSettings
	err := ctx.ReadResource("aws:glue/dataCatalogEncryptionSettings:DataCatalogEncryptionSettings", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DataCatalogEncryptionSettings resources.
type dataCatalogEncryptionSettingsState struct {
	// The ID of the Data Catalog to set the security configuration for. If none is provided, the AWS account ID is used by default.
	CatalogId *string `pulumi:"catalogId"`
	// The security configuration to set. see Data Catalog Encryption Settings.
	DataCatalogEncryptionSettings *DataCatalogEncryptionSettingsDataCatalogEncryptionSettings `pulumi:"dataCatalogEncryptionSettings"`
}

type DataCatalogEncryptionSettingsState struct {
	// The ID of the Data Catalog to set the security configuration for. If none is provided, the AWS account ID is used by default.
	CatalogId pulumi.StringPtrInput
	// The security configuration to set. see Data Catalog Encryption Settings.
	DataCatalogEncryptionSettings DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsPtrInput
}

func (DataCatalogEncryptionSettingsState) ElementType() reflect.Type {
	return reflect.TypeOf((*dataCatalogEncryptionSettingsState)(nil)).Elem()
}

type dataCatalogEncryptionSettingsArgs struct {
	// The ID of the Data Catalog to set the security configuration for. If none is provided, the AWS account ID is used by default.
	CatalogId *string `pulumi:"catalogId"`
	// The security configuration to set. see Data Catalog Encryption Settings.
	DataCatalogEncryptionSettings DataCatalogEncryptionSettingsDataCatalogEncryptionSettings `pulumi:"dataCatalogEncryptionSettings"`
}

// The set of arguments for constructing a DataCatalogEncryptionSettings resource.
type DataCatalogEncryptionSettingsArgs struct {
	// The ID of the Data Catalog to set the security configuration for. If none is provided, the AWS account ID is used by default.
	CatalogId pulumi.StringPtrInput
	// The security configuration to set. see Data Catalog Encryption Settings.
	DataCatalogEncryptionSettings DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsInput
}

func (DataCatalogEncryptionSettingsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dataCatalogEncryptionSettingsArgs)(nil)).Elem()
}

type DataCatalogEncryptionSettingsInput interface {
	pulumi.Input

	ToDataCatalogEncryptionSettingsOutput() DataCatalogEncryptionSettingsOutput
	ToDataCatalogEncryptionSettingsOutputWithContext(ctx context.Context) DataCatalogEncryptionSettingsOutput
}

func (*DataCatalogEncryptionSettings) ElementType() reflect.Type {
	return reflect.TypeOf((**DataCatalogEncryptionSettings)(nil)).Elem()
}

func (i *DataCatalogEncryptionSettings) ToDataCatalogEncryptionSettingsOutput() DataCatalogEncryptionSettingsOutput {
	return i.ToDataCatalogEncryptionSettingsOutputWithContext(context.Background())
}

func (i *DataCatalogEncryptionSettings) ToDataCatalogEncryptionSettingsOutputWithContext(ctx context.Context) DataCatalogEncryptionSettingsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataCatalogEncryptionSettingsOutput)
}

func (i *DataCatalogEncryptionSettings) ToOutput(ctx context.Context) pulumix.Output[*DataCatalogEncryptionSettings] {
	return pulumix.Output[*DataCatalogEncryptionSettings]{
		OutputState: i.ToDataCatalogEncryptionSettingsOutputWithContext(ctx).OutputState,
	}
}

// DataCatalogEncryptionSettingsArrayInput is an input type that accepts DataCatalogEncryptionSettingsArray and DataCatalogEncryptionSettingsArrayOutput values.
// You can construct a concrete instance of `DataCatalogEncryptionSettingsArrayInput` via:
//
//	DataCatalogEncryptionSettingsArray{ DataCatalogEncryptionSettingsArgs{...} }
type DataCatalogEncryptionSettingsArrayInput interface {
	pulumi.Input

	ToDataCatalogEncryptionSettingsArrayOutput() DataCatalogEncryptionSettingsArrayOutput
	ToDataCatalogEncryptionSettingsArrayOutputWithContext(context.Context) DataCatalogEncryptionSettingsArrayOutput
}

type DataCatalogEncryptionSettingsArray []DataCatalogEncryptionSettingsInput

func (DataCatalogEncryptionSettingsArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DataCatalogEncryptionSettings)(nil)).Elem()
}

func (i DataCatalogEncryptionSettingsArray) ToDataCatalogEncryptionSettingsArrayOutput() DataCatalogEncryptionSettingsArrayOutput {
	return i.ToDataCatalogEncryptionSettingsArrayOutputWithContext(context.Background())
}

func (i DataCatalogEncryptionSettingsArray) ToDataCatalogEncryptionSettingsArrayOutputWithContext(ctx context.Context) DataCatalogEncryptionSettingsArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataCatalogEncryptionSettingsArrayOutput)
}

func (i DataCatalogEncryptionSettingsArray) ToOutput(ctx context.Context) pulumix.Output[[]*DataCatalogEncryptionSettings] {
	return pulumix.Output[[]*DataCatalogEncryptionSettings]{
		OutputState: i.ToDataCatalogEncryptionSettingsArrayOutputWithContext(ctx).OutputState,
	}
}

// DataCatalogEncryptionSettingsMapInput is an input type that accepts DataCatalogEncryptionSettingsMap and DataCatalogEncryptionSettingsMapOutput values.
// You can construct a concrete instance of `DataCatalogEncryptionSettingsMapInput` via:
//
//	DataCatalogEncryptionSettingsMap{ "key": DataCatalogEncryptionSettingsArgs{...} }
type DataCatalogEncryptionSettingsMapInput interface {
	pulumi.Input

	ToDataCatalogEncryptionSettingsMapOutput() DataCatalogEncryptionSettingsMapOutput
	ToDataCatalogEncryptionSettingsMapOutputWithContext(context.Context) DataCatalogEncryptionSettingsMapOutput
}

type DataCatalogEncryptionSettingsMap map[string]DataCatalogEncryptionSettingsInput

func (DataCatalogEncryptionSettingsMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DataCatalogEncryptionSettings)(nil)).Elem()
}

func (i DataCatalogEncryptionSettingsMap) ToDataCatalogEncryptionSettingsMapOutput() DataCatalogEncryptionSettingsMapOutput {
	return i.ToDataCatalogEncryptionSettingsMapOutputWithContext(context.Background())
}

func (i DataCatalogEncryptionSettingsMap) ToDataCatalogEncryptionSettingsMapOutputWithContext(ctx context.Context) DataCatalogEncryptionSettingsMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataCatalogEncryptionSettingsMapOutput)
}

func (i DataCatalogEncryptionSettingsMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*DataCatalogEncryptionSettings] {
	return pulumix.Output[map[string]*DataCatalogEncryptionSettings]{
		OutputState: i.ToDataCatalogEncryptionSettingsMapOutputWithContext(ctx).OutputState,
	}
}

type DataCatalogEncryptionSettingsOutput struct{ *pulumi.OutputState }

func (DataCatalogEncryptionSettingsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataCatalogEncryptionSettings)(nil)).Elem()
}

func (o DataCatalogEncryptionSettingsOutput) ToDataCatalogEncryptionSettingsOutput() DataCatalogEncryptionSettingsOutput {
	return o
}

func (o DataCatalogEncryptionSettingsOutput) ToDataCatalogEncryptionSettingsOutputWithContext(ctx context.Context) DataCatalogEncryptionSettingsOutput {
	return o
}

func (o DataCatalogEncryptionSettingsOutput) ToOutput(ctx context.Context) pulumix.Output[*DataCatalogEncryptionSettings] {
	return pulumix.Output[*DataCatalogEncryptionSettings]{
		OutputState: o.OutputState,
	}
}

// The ID of the Data Catalog to set the security configuration for. If none is provided, the AWS account ID is used by default.
func (o DataCatalogEncryptionSettingsOutput) CatalogId() pulumi.StringOutput {
	return o.ApplyT(func(v *DataCatalogEncryptionSettings) pulumi.StringOutput { return v.CatalogId }).(pulumi.StringOutput)
}

// The security configuration to set. see Data Catalog Encryption Settings.
func (o DataCatalogEncryptionSettingsOutput) DataCatalogEncryptionSettings() DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsOutput {
	return o.ApplyT(func(v *DataCatalogEncryptionSettings) DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsOutput {
		return v.DataCatalogEncryptionSettings
	}).(DataCatalogEncryptionSettingsDataCatalogEncryptionSettingsOutput)
}

type DataCatalogEncryptionSettingsArrayOutput struct{ *pulumi.OutputState }

func (DataCatalogEncryptionSettingsArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DataCatalogEncryptionSettings)(nil)).Elem()
}

func (o DataCatalogEncryptionSettingsArrayOutput) ToDataCatalogEncryptionSettingsArrayOutput() DataCatalogEncryptionSettingsArrayOutput {
	return o
}

func (o DataCatalogEncryptionSettingsArrayOutput) ToDataCatalogEncryptionSettingsArrayOutputWithContext(ctx context.Context) DataCatalogEncryptionSettingsArrayOutput {
	return o
}

func (o DataCatalogEncryptionSettingsArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*DataCatalogEncryptionSettings] {
	return pulumix.Output[[]*DataCatalogEncryptionSettings]{
		OutputState: o.OutputState,
	}
}

func (o DataCatalogEncryptionSettingsArrayOutput) Index(i pulumi.IntInput) DataCatalogEncryptionSettingsOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DataCatalogEncryptionSettings {
		return vs[0].([]*DataCatalogEncryptionSettings)[vs[1].(int)]
	}).(DataCatalogEncryptionSettingsOutput)
}

type DataCatalogEncryptionSettingsMapOutput struct{ *pulumi.OutputState }

func (DataCatalogEncryptionSettingsMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DataCatalogEncryptionSettings)(nil)).Elem()
}

func (o DataCatalogEncryptionSettingsMapOutput) ToDataCatalogEncryptionSettingsMapOutput() DataCatalogEncryptionSettingsMapOutput {
	return o
}

func (o DataCatalogEncryptionSettingsMapOutput) ToDataCatalogEncryptionSettingsMapOutputWithContext(ctx context.Context) DataCatalogEncryptionSettingsMapOutput {
	return o
}

func (o DataCatalogEncryptionSettingsMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*DataCatalogEncryptionSettings] {
	return pulumix.Output[map[string]*DataCatalogEncryptionSettings]{
		OutputState: o.OutputState,
	}
}

func (o DataCatalogEncryptionSettingsMapOutput) MapIndex(k pulumi.StringInput) DataCatalogEncryptionSettingsOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DataCatalogEncryptionSettings {
		return vs[0].(map[string]*DataCatalogEncryptionSettings)[vs[1].(string)]
	}).(DataCatalogEncryptionSettingsOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DataCatalogEncryptionSettingsInput)(nil)).Elem(), &DataCatalogEncryptionSettings{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataCatalogEncryptionSettingsArrayInput)(nil)).Elem(), DataCatalogEncryptionSettingsArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataCatalogEncryptionSettingsMapInput)(nil)).Elem(), DataCatalogEncryptionSettingsMap{})
	pulumi.RegisterOutputType(DataCatalogEncryptionSettingsOutput{})
	pulumi.RegisterOutputType(DataCatalogEncryptionSettingsArrayOutput{})
	pulumi.RegisterOutputType(DataCatalogEncryptionSettingsMapOutput{})
}
