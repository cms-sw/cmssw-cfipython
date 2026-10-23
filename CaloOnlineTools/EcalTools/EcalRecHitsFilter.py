import FWCore.ParameterSet.Config as cms

def EcalRecHitsFilter(*args, **kwargs):
  mod = cms.EDFilter('EcalRecHitsFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
