import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_TestAlpakaVerifyObjectOnDevice(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::TestAlpakaVerifyObjectOnDevice',
    source = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
