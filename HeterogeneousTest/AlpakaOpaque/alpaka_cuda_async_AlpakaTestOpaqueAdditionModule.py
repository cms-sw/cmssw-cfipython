import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_AlpakaTestOpaqueAdditionModule(*args, **kwargs):
  mod = cms.EDAnalyzer('alpaka_cuda_async::AlpakaTestOpaqueAdditionModule',
    size = cms.uint32(1048576),
    alpaka = cms.untracked.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
