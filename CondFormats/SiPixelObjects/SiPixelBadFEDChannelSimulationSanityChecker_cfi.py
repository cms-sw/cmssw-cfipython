import FWCore.ParameterSet.Config as cms

SiPixelBadFEDChannelSimulationSanityChecker = cms.EDAnalyzer('SiPixelBadFEDChannelSimulationSanityChecker',
  printDebug = cms.untracked.bool(True)
)
