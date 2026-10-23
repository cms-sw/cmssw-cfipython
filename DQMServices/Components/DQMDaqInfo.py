import FWCore.ParameterSet.Config as cms

def DQMDaqInfo(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMDaqInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
