import FWCore.ParameterSet.Config as cms

def DDTestVectors(**kwargs):
  mod = cms.EDAnalyzer('DDTestVectors',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
