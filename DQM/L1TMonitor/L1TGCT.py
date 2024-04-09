import FWCore.ParameterSet.Config as cms

def L1TGCT(**kwargs):
  mod = cms.EDProducer('L1TGCT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod