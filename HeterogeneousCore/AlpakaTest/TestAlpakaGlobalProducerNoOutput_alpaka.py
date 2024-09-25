import FWCore.ParameterSet.Config as cms

def TestAlpakaGlobalProducerNoOutput_alpaka(*args, **kwargs):
  mod = cms.EDProducer('TestAlpakaGlobalProducerNoOutput@alpaka',
    source = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
