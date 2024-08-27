import FWCore.ParameterSet.Config as cms

def GenFilterEfficiencyProducer(**kwargs):
  mod = cms.EDProducer('GenFilterEfficiencyProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
