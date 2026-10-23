import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_TestAlpakaStreamFixedQueueProducerE(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::TestAlpakaStreamFixedQueueProducerE',
    eventSetupSource = cms.ESInputTag('', ''),
    source = cms.InputTag(''),
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
