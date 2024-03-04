import FWCore.ParameterSet.Config as cms

def PATMuonRefSelector(**kwargs):
  mod = cms.EDFilter('PATMuonRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
