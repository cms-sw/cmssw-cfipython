import FWCore.ParameterSet.Config as cms

def DTHVDump(*args, **kwargs):
  mod = cms.EDAnalyzer('DTHVDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
