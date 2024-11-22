import FWCore.ParameterSet.Config as cms

def LaserDQM(*args, **kwargs):
  mod = cms.EDAnalyzer('LaserDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
