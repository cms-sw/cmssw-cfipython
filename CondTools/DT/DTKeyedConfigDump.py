import FWCore.ParameterSet.Config as cms

def DTKeyedConfigDump(*args, **kwargs):
  mod = cms.EDAnalyzer('DTKeyedConfigDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
