import FWCore.ParameterSet.Config as cms

def DDTestMuonNumbering(*args, **kwargs):
  mod = cms.EDAnalyzer('DDTestMuonNumbering',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
