import FWCore.ParameterSet.Config as cms

def TauDQMHistEffProducer(**kwargs):
  mod = cms.EDProducer('TauDQMHistEffProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
