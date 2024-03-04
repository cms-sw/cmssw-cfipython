import FWCore.ParameterSet.Config as cms

def TestAlpakaGlobalProducerNullES_alpaka(**kwargs):
  mod = cms.EDProducer('TestAlpakaGlobalProducerNullES@alpaka',
    eventSetupSource = cms.ESInputTag('', ''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
