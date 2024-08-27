import FWCore.ParameterSet.Config as cms

def GenJetClosestMatchSelector(**kwargs):
  mod = cms.EDFilter('GenJetClosestMatchSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
