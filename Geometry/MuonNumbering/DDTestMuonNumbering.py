import FWCore.ParameterSet.Config as cms

def DDTestMuonNumbering(**kwargs):
  mod = cms.EDAnalyzer('DDTestMuonNumbering',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
