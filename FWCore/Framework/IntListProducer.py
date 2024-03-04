import FWCore.ParameterSet.Config as cms

def IntListProducer(**kwargs):
  mod = cms.EDProducer('IntListProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
