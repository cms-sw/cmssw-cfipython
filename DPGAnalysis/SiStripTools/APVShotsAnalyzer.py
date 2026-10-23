import FWCore.ParameterSet.Config as cms

def APVShotsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('APVShotsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
