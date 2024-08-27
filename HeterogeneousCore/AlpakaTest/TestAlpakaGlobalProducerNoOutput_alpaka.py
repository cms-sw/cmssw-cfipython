import FWCore.ParameterSet.Config as cms

def TestAlpakaGlobalProducerNoOutput_alpaka(**kwargs):
  mod = cms.EDProducer('TestAlpakaGlobalProducerNoOutput@alpaka',
    source = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
