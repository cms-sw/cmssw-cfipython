import FWCore.ParameterSet.Config as cms

def PtMinMuonSelector(**kwargs):
  mod = cms.EDFilter('PtMinMuonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
