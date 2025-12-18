import FWCore.ParameterSet.Config as cms

def DDTestFilteredView(*args, **kwargs):
  mod = cms.EDAnalyzer('DDTestFilteredView',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
