import FWCore.ParameterSet.Config as cms

def GLBMuonAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GLBMuonAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
