import FWCore.ParameterSet.Config as cms

def TestAlpakaGlobalProducerWithPtr_alpaka(**kwargs):
  mod = cms.EDProducer('TestAlpakaGlobalProducerWithPtr@alpaka',
    size = cms.required.int32,
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod