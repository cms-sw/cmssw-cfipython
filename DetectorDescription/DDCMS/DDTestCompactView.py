import FWCore.ParameterSet.Config as cms

def DDTestCompactView(*args, **kwargs):
  mod = cms.EDAnalyzer('DDTestCompactView',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
