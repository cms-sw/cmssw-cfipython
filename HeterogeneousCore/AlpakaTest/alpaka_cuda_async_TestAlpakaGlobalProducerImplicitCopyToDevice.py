import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_TestAlpakaGlobalProducerImplicitCopyToDevice(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::TestAlpakaGlobalProducerImplicitCopyToDevice',
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
