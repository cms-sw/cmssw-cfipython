import FWCore.ParameterSet.Config as cms

def OscarMTProducer(**kwargs):
  mod = cms.EDProducer('OscarMTProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
