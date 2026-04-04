import FWCore.ParameterSet.Config as cms

def AlpakaTestWrapperAdditionModule_alpaka(*args, **kwargs):
  mod = cms.EDAnalyzer('AlpakaTestWrapperAdditionModule@alpaka',
    size = cms.uint32(1048576),
    alpaka = cms.untracked.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
