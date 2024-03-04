import FWCore.ParameterSet.Config as cms

def PATMuonSelector(**kwargs):
  mod = cms.EDFilter('PATMuonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
