import FWCore.ParameterSet.Config as cms

def JPTJetSelector(**kwargs):
  mod = cms.EDFilter('JPTJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
