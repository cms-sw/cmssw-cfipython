import FWCore.ParameterSet.Config as cms

def testSiStripFedKey(*args, **kwargs):
  mod = cms.EDAnalyzer('testSiStripFedKey',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
