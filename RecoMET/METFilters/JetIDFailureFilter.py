import FWCore.ParameterSet.Config as cms

def JetIDFailureFilter(**kwargs):
  mod = cms.EDFilter('JetIDFailureFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
