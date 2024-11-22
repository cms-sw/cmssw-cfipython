import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_TestAlpakaProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::TestAlpakaProducer',
    size = cms.required.int32,
    size2 = cms.required.int32,
    size3 = cms.required.int32,
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
