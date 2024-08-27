import FWCore.ParameterSet.Config as cms

def SwitchProducer(**kwargs):
  mod = cms.EDProducer('SwitchProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
