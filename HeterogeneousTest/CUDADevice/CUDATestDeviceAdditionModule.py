import FWCore.ParameterSet.Config as cms

def CUDATestDeviceAdditionModule(*args, **kwargs):
  mod = cms.EDAnalyzer('CUDATestDeviceAdditionModule',
    size = cms.uint32(1048576),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
