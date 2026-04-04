import FWCore.ParameterSet.Config as cms

def AlpakaTestOpaqueAdditionModule_alpaka(*args, **kwargs):
  mod = cms.EDAnalyzer('AlpakaTestOpaqueAdditionModule@alpaka',
    size = cms.uint32(1048576),
    alpaka = cms.untracked.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
