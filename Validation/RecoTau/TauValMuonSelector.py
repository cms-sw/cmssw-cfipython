import FWCore.ParameterSet.Config as cms

def TauValMuonSelector(**kwargs):
  mod = cms.EDFilter('TauValMuonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
