import FWCore.ParameterSet.Config as cms

def DQMMessageLoggerClient(**kwargs):
  mod = cms.EDAnalyzer('DQMMessageLoggerClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
