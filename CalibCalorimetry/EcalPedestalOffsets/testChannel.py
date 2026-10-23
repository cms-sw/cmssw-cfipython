import FWCore.ParameterSet.Config as cms

def testChannel(*args, **kwargs):
  mod = cms.EDAnalyzer('testChannel',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
