import FWCore.ParameterSet.Config as cms

def testEcalTPGScale(*args, **kwargs):
  mod = cms.EDAnalyzer('testEcalTPGScale',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
