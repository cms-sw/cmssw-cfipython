import FWCore.ParameterSet.Config as cms

def CUDATestKernelAdditionModule(**kwargs):
  mod = cms.EDAnalyzer('CUDATestKernelAdditionModule',
    size = cms.uint32(1048576),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
