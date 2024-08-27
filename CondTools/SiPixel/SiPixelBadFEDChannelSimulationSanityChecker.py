import FWCore.ParameterSet.Config as cms

def SiPixelBadFEDChannelSimulationSanityChecker(**kwargs):
  mod = cms.EDAnalyzer('SiPixelBadFEDChannelSimulationSanityChecker',
    printDebug = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
