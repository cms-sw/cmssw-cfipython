import FWCore.ParameterSet.Config as cms

def testMuonAssociator(*args, **kwargs):
  mod = cms.EDAnalyzer('testMuonAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
