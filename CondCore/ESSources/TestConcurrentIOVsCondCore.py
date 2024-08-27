import FWCore.ParameterSet.Config as cms

def TestConcurrentIOVsCondCore(**kwargs):
  mod = cms.EDAnalyzer('TestConcurrentIOVsCondCore',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
