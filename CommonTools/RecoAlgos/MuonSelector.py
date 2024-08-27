import FWCore.ParameterSet.Config as cms

def MuonSelector(**kwargs):
  mod = cms.EDFilter('MuonSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
