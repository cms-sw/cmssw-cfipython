import FWCore.ParameterSet.Config as cms

def NonProducer(**kwargs):
  mod = cms.EDProducer('NonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
