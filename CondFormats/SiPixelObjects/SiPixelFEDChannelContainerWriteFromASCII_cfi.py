import FWCore.ParameterSet.Config as cms

SiPixelFEDChannelContainerWriteFromASCII = cms.EDAnalyzer('SiPixelFEDChannelContainerWriteFromASCII',
  printDebug = cms.untracked.bool(True),
  addDefault = cms.untracked.bool(True),
  snapshots = cms.string(''),
  record = cms.string('SiPixelStatusScenariosRcd'),
  mightGet = cms.optional.untracked.vstring
)
