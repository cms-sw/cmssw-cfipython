import FWCore.ParameterSet.Config as cms

def MakeCoordLUT(*args, **kwargs):
  mod = cms.EDAnalyzer('MakeCoordLUT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod