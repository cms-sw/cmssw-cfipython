import FWCore.ParameterSet.Config as cms

def TGraphWriter(**kwargs):
  mod = cms.EDAnalyzer('TGraphWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
