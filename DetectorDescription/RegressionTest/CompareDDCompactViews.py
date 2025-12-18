import FWCore.ParameterSet.Config as cms

def CompareDDCompactViews(*args, **kwargs):
  mod = cms.EDAnalyzer('CompareDDCompactViews',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
