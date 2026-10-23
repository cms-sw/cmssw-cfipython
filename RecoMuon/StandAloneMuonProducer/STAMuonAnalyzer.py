import FWCore.ParameterSet.Config as cms

def STAMuonAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('STAMuonAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
