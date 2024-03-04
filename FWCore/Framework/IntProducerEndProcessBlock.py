import FWCore.ParameterSet.Config as cms

def IntProducerEndProcessBlock(**kwargs):
  mod = cms.EDProducer('IntProducerEndProcessBlock',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
