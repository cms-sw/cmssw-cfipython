import FWCore.ParameterSet.Config as cms

def ROCmTestWrapperAdditionModule(*args, **kwargs):
  mod = cms.EDAnalyzer('ROCmTestWrapperAdditionModule',
    size = cms.uint32(1048576),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
