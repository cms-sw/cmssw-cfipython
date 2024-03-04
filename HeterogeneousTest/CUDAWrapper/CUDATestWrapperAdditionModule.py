import FWCore.ParameterSet.Config as cms

def CUDATestWrapperAdditionModule(**kwargs):
  mod = cms.EDAnalyzer('CUDATestWrapperAdditionModule',
    size = cms.uint32(1048576),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
