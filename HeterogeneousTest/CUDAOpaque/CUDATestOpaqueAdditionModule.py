import FWCore.ParameterSet.Config as cms

def CUDATestOpaqueAdditionModule(*args, **kwargs):
  mod = cms.EDAnalyzer('CUDATestOpaqueAdditionModule',
    size = cms.uint32(1048576),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
