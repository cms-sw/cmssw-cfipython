import FWCore.ParameterSet.Config as cms

def MuonPtFilter(**kwargs):
  mod = cms.EDFilter('MuonPtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
