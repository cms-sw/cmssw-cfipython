import FWCore.ParameterSet.Config as cms

def L1TEventInfoClient(**kwargs):
  mod = cms.EDProducer('L1TEventInfoClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
