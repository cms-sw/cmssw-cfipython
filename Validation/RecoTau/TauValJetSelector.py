import FWCore.ParameterSet.Config as cms

def TauValJetSelector(**kwargs):
  mod = cms.EDFilter('TauValJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod