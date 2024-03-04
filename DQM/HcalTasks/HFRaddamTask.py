import FWCore.ParameterSet.Config as cms

def HFRaddamTask(**kwargs):
  mod = cms.EDProducer('HFRaddamTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
