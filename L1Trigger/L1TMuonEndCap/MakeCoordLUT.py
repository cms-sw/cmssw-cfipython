import FWCore.ParameterSet.Config as cms

def MakeCoordLUT(**kwargs):
  mod = cms.EDAnalyzer('MakeCoordLUT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
