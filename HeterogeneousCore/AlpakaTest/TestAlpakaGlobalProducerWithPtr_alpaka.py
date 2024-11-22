import FWCore.ParameterSet.Config as cms

def TestAlpakaGlobalProducerWithPtr_alpaka(*args, **kwargs):
  mod = cms.EDProducer('TestAlpakaGlobalProducerWithPtr@alpaka',
    size = cms.required.int32,
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
