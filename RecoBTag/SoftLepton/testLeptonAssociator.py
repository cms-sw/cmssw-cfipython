import FWCore.ParameterSet.Config as cms

def testLeptonAssociator(*args, **kwargs):
  mod = cms.EDAnalyzer('testLeptonAssociator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
