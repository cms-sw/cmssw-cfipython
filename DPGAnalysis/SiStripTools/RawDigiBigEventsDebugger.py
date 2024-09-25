import FWCore.ParameterSet.Config as cms

def RawDigiBigEventsDebugger(*args, **kwargs):
  mod = cms.EDAnalyzer('RawDigiBigEventsDebugger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
