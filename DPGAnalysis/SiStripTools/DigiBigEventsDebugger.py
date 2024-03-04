import FWCore.ParameterSet.Config as cms

def DigiBigEventsDebugger(**kwargs):
  mod = cms.EDAnalyzer('DigiBigEventsDebugger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
