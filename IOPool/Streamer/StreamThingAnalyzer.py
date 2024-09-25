import FWCore.ParameterSet.Config as cms

def StreamThingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('StreamThingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
