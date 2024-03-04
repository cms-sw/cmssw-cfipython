import FWCore.ParameterSet.Config as cms

def TrajectorySeedProducer(**kwargs):
  mod = cms.EDProducer('TrajectorySeedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
