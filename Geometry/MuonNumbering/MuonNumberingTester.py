import FWCore.ParameterSet.Config as cms

def MuonNumberingTester(*args, **kwargs):
  mod = cms.EDAnalyzer('MuonNumberingTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
