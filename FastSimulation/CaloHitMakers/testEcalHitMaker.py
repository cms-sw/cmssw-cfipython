import FWCore.ParameterSet.Config as cms

def testEcalHitMaker(*args, **kwargs):
  mod = cms.EDAnalyzer('testEcalHitMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
