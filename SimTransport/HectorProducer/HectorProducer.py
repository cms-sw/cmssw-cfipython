import FWCore.ParameterSet.Config as cms

def HectorProducer(**kwargs):
  mod = cms.EDProducer('HectorProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
