import FWCore.ParameterSet.Config as cms

def PATTauSelector(**kwargs):
  mod = cms.EDFilter('PATTauSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
