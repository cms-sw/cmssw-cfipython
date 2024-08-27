import FWCore.ParameterSet.Config as cms

def MuonViewRefSelector(**kwargs):
  mod = cms.EDFilter('MuonViewRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
