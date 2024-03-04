import FWCore.ParameterSet.Config as cms

def CUDATestDeviceAdditionModule(**kwargs):
  mod = cms.EDAnalyzer('CUDATestDeviceAdditionModule',
    size = cms.uint32(1048576),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
