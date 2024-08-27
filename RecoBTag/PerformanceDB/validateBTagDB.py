import FWCore.ParameterSet.Config as cms

def validateBTagDB(**kwargs):
  mod = cms.EDAnalyzer('validateBTagDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
