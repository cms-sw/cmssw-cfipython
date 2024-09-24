import FWCore.ParameterSet.Config as cms

def CTPPSOpticsPlotter(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSOpticsPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
