import FWCore.ParameterSet.Config as cms

SiPixelClusterizerDefault = cms.EDProducer('SiPixelClusterProducer',
  src = cms.InputTag('siPixelDigis'),
  ClusterMode = cms.string('PixelThresholdClusterizer'),
  maxNumberOfClusters = cms.int32(-1),
  payloadType = cms.string('Offline'),
  ChannelThreshold = cms.int32(1000),
  MissCalibrate = cms.bool(True),
  SplitClusters = cms.bool(False),
  VCaltoElectronGain = cms.int32(65),
  VCaltoElectronGain_L1 = cms.int32(65),
  VCaltoElectronOffset = cms.int32(-414),
  VCaltoElectronOffset_L1 = cms.int32(-414),
  SeedThreshold = cms.int32(1000),
  ClusterThreshold_L1 = cms.int32(4000),
  ClusterThreshold = cms.int32(4000),
  ElectronPerADCGain = cms.double(135),
  Phase2Calibration = cms.bool(False),
  Phase2ReadoutMode = cms.int32(-1),
  Phase2DigiBaseline = cms.double(1200),
  Phase2KinkADC = cms.int32(8)
)
