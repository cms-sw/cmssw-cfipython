import FWCore.ParameterSet.Config as cms

def DTCompactMapDump(*args, **kwargs):
  mod = cms.EDAnalyzer('DTCompactMapDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
