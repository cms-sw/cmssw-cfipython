import FWCore.ParameterSet.Config as cms

def PFMETProducerMVA(**kwargs):
  mod = cms.EDProducer('PFMETProducerMVA',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
