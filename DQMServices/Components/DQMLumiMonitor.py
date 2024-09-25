import FWCore.ParameterSet.Config as cms

def DQMLumiMonitor(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMLumiMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
