import FWCore.ParameterSet.Config as cms

def MessageLoggerClient(**kwargs):
  mod = cms.EDAnalyzer('MessageLoggerClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
