import FWCore.ParameterSet.Config as cms

def MuonOffsetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('MuonOffsetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
