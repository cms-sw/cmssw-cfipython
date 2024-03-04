import FWCore.ParameterSet.Config as cms

def MuonRefSelector(**kwargs):
  mod = cms.EDFilter('MuonRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
