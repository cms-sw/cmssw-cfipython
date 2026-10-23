import FWCore.ParameterSet.Config as cms

def DTTimeUtility(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTimeUtility',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
