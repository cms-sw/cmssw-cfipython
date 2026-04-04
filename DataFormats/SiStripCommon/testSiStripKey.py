import FWCore.ParameterSet.Config as cms

def testSiStripKey(*args, **kwargs):
  mod = cms.EDAnalyzer('testSiStripKey',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
