import FWCore.ParameterSet.Config as cms

SiPixelFEDChannelContainerWriteFromASCII = cms.EDAnalyzer('SiPixelFEDChannelContainerWriteFromASCII',
  printDebug = cms.untracked.bool(True),
  snapshots = cms.string(''),
  record = cms.string('SiPixelStatusScenariosRcd')
)
