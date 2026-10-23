import FWCore.ParameterSet.Config as cms

def CastorDumpConditions(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorDumpConditions',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
