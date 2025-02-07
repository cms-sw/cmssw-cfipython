import FWCore.ParameterSet.Config as cms

def testSiStripHistId(*args, **kwargs):
  mod = cms.EDAnalyzer('testSiStripHistId',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
