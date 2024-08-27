import FWCore.ParameterSet.Config as cms

def corrGains(**kwargs):
  mod = cms.EDAnalyzer('corrGains',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
