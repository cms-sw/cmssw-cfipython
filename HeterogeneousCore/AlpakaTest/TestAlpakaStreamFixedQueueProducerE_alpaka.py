import FWCore.ParameterSet.Config as cms

def TestAlpakaStreamFixedQueueProducerE_alpaka(*args, **kwargs):
  mod = cms.EDProducer('TestAlpakaStreamFixedQueueProducerE@alpaka',
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
