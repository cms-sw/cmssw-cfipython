import FWCore.ParameterSet.Config as cms

def TestAlpakaStreamSynchronizingProducer_alpaka(**kwargs):
  mod = cms.EDProducer('TestAlpakaStreamSynchronizingProducer@alpaka',
    source = cms.required.InputTag,
    intSource = cms.required.InputTag,
    expectedInt = cms.required.int32,
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
