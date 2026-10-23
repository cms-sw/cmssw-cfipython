import FWCore.ParameterSet.Config as cms

def testSiStripNullKey(*args, **kwargs):
  mod = cms.EDAnalyzer('testSiStripNullKey',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
