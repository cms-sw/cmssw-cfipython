import FWCore.ParameterSet.Config as cms

def MakePtLUT(*args, **kwargs):
  mod = cms.EDAnalyzer('MakePtLUT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
