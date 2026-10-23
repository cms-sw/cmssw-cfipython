import FWCore.ParameterSet.Config as cms

def TestConcurrentIOVsCondCore(*args, **kwargs):
  mod = cms.EDAnalyzer('TestConcurrentIOVsCondCore',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
