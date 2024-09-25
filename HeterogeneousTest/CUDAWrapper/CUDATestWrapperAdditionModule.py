import FWCore.ParameterSet.Config as cms

def CUDATestWrapperAdditionModule(*args, **kwargs):
  mod = cms.EDAnalyzer('CUDATestWrapperAdditionModule',
    size = cms.uint32(1048576),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
