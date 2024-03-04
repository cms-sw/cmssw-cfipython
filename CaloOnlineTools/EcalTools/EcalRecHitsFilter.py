import FWCore.ParameterSet.Config as cms

def EcalRecHitsFilter(**kwargs):
  mod = cms.EDFilter('EcalRecHitsFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
