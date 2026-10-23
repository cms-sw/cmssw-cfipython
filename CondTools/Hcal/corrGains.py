import FWCore.ParameterSet.Config as cms

def corrGains(*args, **kwargs):
  mod = cms.EDAnalyzer('corrGains',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
