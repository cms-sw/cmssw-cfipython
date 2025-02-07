import FWCore.ParameterSet.Config as cms

def DTMapWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTMapWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
