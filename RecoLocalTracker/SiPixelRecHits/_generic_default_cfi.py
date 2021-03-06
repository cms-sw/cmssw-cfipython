import FWCore.ParameterSet.Config as cms

_generic_default = cms.ESProducer('PixelCPEGenericESProducer',
  LoadTemplatesFromDB = cms.bool(True),
  Alpha2Order = cms.bool(True),
  ClusterProbComputationFlag = cms.int32(0),
  useLAWidthFromDB = cms.bool(True),
  lAOffset = cms.double(0),
  lAWidthBPix = cms.double(0),
  lAWidthFPix = cms.double(0),
  eff_charge_cut_highX = cms.double(1),
  eff_charge_cut_highY = cms.double(1),
  eff_charge_cut_lowX = cms.double(0),
  eff_charge_cut_lowY = cms.double(0),
  size_cutX = cms.double(3),
  size_cutY = cms.double(3),
  EdgeClusterErrorX = cms.double(50),
  EdgeClusterErrorY = cms.double(85),
  inflate_errors = cms.bool(False),
  inflate_all_errors_no_trk_angle = cms.bool(False),
  NoTemplateErrorsWhenNoTrkAngles = cms.bool(False),
  UseErrorsFromTemplates = cms.bool(True),
  TruncatePixelCharge = cms.bool(True),
  IrradiationBiasCorrection = cms.bool(False),
  DoCosmics = cms.bool(False),
  Upgrade = cms.bool(False),
  SmallPitch = cms.bool(False),
  ComponentName = cms.string('PixelCPEGeneric'),
  MagneticFieldRecord = cms.ESInputTag('', ''),
  useLAAlignmentOffsets = cms.bool(False),
  DoLorentz = cms.bool(False),
  appendToDataLabel = cms.string('')
)
