import FWCore.ParameterSet.Config as cms

def InputDataProducer(**kwargs):
  mod = cms.EDProducer('InputDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
