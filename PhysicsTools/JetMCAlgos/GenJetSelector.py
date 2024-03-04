import FWCore.ParameterSet.Config as cms

def GenJetSelector(**kwargs):
  mod = cms.EDFilter('GenJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
