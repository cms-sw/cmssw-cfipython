import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_TestAlpakaGlobalProducerNullES(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::TestAlpakaGlobalProducerNullES',
    eventSetupSource = cms.ESInputTag('', ''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
