import FWCore.ParameterSet.Config as cms

SiPixelFEDChannelContainerFromQualityConverter = cms.EDAnalyzer('SiPixelFEDChannelContainerFromQualityConverter',
  printDebug = cms.untracked.bool(False),
  removeEmptyPayloads = cms.untracked.bool(False),
  record = cms.string('SiPixelStatusScenariosRcd'),
  mightGet = cms.optional.untracked.vstring
)
