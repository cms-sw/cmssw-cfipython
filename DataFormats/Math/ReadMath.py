import FWCore.ParameterSet.Config as cms

def ReadMath(**kwargs):
  mod = cms.EDAnalyzer('ReadMath',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
