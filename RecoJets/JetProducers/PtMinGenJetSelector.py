import FWCore.ParameterSet.Config as cms

def PtMinGenJetSelector(**kwargs):
  mod = cms.EDFilter('PtMinGenJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
