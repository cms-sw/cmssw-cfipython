import FWCore.ParameterSet.Config as cms

def DQMMessageLoggerClient(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMMessageLoggerClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
