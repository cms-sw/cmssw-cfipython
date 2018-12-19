import FWCore.ParameterSet.Config as cms

SiPixelFEDChannelContainerTestWriter = cms.EDAnalyzer('SiPixelFEDChannelContainerTestWriter',
  printDebug = cms.untracked.bool(False),
  record = cms.string('SiPixelStatusScenariosRcd')
)
