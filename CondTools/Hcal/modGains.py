import FWCore.ParameterSet.Config as cms

def modGains(**kwargs):
  mod = cms.EDAnalyzer('modGains',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
