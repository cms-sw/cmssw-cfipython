import FWCore.ParameterSet.Config as cms

def ComparePtLUT(**kwargs):
  mod = cms.EDAnalyzer('ComparePtLUT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
