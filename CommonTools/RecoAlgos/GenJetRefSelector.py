import FWCore.ParameterSet.Config as cms

def GenJetRefSelector(**kwargs):
  mod = cms.EDFilter('GenJetRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
