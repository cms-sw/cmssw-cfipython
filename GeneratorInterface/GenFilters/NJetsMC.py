import FWCore.ParameterSet.Config as cms

def NJetsMC(**kwargs):
  mod = cms.EDFilter('NJetsMC',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
