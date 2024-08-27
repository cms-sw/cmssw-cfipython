import FWCore.ParameterSet.Config as cms

def DeleteEarlyProducer(**kwargs):
  mod = cms.EDProducer('DeleteEarlyProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
