import FWCore.ParameterSet.Config as cms

def L1TRCT(**kwargs):
  mod = cms.EDProducer('L1TRCT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod