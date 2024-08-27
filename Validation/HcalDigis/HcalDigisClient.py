import FWCore.ParameterSet.Config as cms

def HcalDigisClient(**kwargs):
  mod = cms.EDProducer('HcalDigisClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
