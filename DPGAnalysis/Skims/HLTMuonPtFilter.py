import FWCore.ParameterSet.Config as cms

def HLTMuonPtFilter(**kwargs):
  mod = cms.EDFilter('HLTMuonPtFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
