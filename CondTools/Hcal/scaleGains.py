import FWCore.ParameterSet.Config as cms

def scaleGains(**kwargs):
  mod = cms.EDAnalyzer('scaleGains',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
