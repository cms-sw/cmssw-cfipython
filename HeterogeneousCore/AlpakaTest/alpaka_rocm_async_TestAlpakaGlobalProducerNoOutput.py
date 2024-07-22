import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_TestAlpakaGlobalProducerNoOutput(**kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::TestAlpakaGlobalProducerNoOutput',
    source = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod