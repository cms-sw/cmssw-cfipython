import FWCore.ParameterSet.Config as cms

def ComparePtLUT(*args, **kwargs):
  mod = cms.EDAnalyzer('ComparePtLUT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
