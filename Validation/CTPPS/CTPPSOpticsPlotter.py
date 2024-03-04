import FWCore.ParameterSet.Config as cms

def CTPPSOpticsPlotter(**kwargs):
  mod = cms.EDAnalyzer('CTPPSOpticsPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
