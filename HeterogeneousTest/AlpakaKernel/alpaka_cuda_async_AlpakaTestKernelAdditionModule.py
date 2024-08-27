import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_AlpakaTestKernelAdditionModule(**kwargs):
  mod = cms.EDAnalyzer('alpaka_cuda_async::AlpakaTestKernelAdditionModule',
    size = cms.uint32(1048576),
    alpaka = cms.untracked.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
