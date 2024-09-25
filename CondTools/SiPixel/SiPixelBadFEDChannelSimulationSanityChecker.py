import FWCore.ParameterSet.Config as cms

def SiPixelBadFEDChannelSimulationSanityChecker(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelBadFEDChannelSimulationSanityChecker',
    printDebug = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
