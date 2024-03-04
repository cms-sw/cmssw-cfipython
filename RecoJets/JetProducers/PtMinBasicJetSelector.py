import FWCore.ParameterSet.Config as cms

def PtMinBasicJetSelector(**kwargs):
  mod = cms.EDFilter('PtMinBasicJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
