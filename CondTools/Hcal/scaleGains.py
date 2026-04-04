import FWCore.ParameterSet.Config as cms

def scaleGains(*args, **kwargs):
  mod = cms.EDAnalyzer('scaleGains',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
