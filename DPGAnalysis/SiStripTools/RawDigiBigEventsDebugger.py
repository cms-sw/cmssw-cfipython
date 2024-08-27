import FWCore.ParameterSet.Config as cms

def RawDigiBigEventsDebugger(**kwargs):
  mod = cms.EDAnalyzer('RawDigiBigEventsDebugger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
