import FWCore.ParameterSet.Config as cms

def testReader(*args, **kwargs):
  mod = cms.EDAnalyzer('testReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
