import FWCore.ParameterSet.Config as cms

def L1TSummary(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
