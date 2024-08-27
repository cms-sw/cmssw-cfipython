import FWCore.ParameterSet.Config as cms

def AlpakaTestOpaqueAdditionModule_alpaka(**kwargs):
  mod = cms.EDAnalyzer('AlpakaTestOpaqueAdditionModule@alpaka',
    size = cms.uint32(1048576),
    alpaka = cms.untracked.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
