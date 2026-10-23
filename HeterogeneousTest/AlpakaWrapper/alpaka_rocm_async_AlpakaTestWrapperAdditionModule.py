import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_AlpakaTestWrapperAdditionModule(*args, **kwargs):
  mod = cms.EDAnalyzer('alpaka_rocm_async::AlpakaTestWrapperAdditionModule',
    size = cms.uint32(1048576),
    alpaka = cms.untracked.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
