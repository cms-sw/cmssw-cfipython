import FWCore.ParameterSet.Config as cms

PixelCPEFastESProducer = cms.ESProducer('PixelCPEFastESProducer',
  LoadTemplatesFromDB = cms.bool(True),
  Alpha2Order = cms.bool(True),
  ClusterProbComputationFlag = cms.int32(0),
  useLAWidthFromDB = cms.bool(True),
  lAOffset = cms.double(0),
  lAWidthBPix = cms.double(0),
  lAWidthFPix = cms.double(0),
  doLorentzFromAlignment = cms.bool(False),
  useLAFromDB = cms.bool(True),
  EdgeClusterErrorX = cms.double(50),
  EdgeClusterErrorY = cms.double(85),
  UseErrorsFromTemplates = cms.bool(True),
  TruncatePixelCharge = cms.bool(True),
  ComponentName = cms.string('PixelCPEFast'),
  MagneticFieldRecord = cms.ESInputTag('', ''),
  appendToDataLabel = cms.string('')
)
