import FWCore.ParameterSet.Config as cms

ctppsPixelClusters = cms.EDProducer('CTPPSPixelClusterProducer',
  RPixVerbosity = cms.untracked.int32(0),
  label = cms.string('ctppsPixelDigis'),
  SeedADCThreshold = cms.int32(2),
  ADCThreshold = cms.int32(2),
  ElectronADCGain = cms.double(135),
  VCaltoElectronGain = cms.int32(50),
  VCaltoElectronOffset = cms.int32(-411),
  doSingleCalibration = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
