import FWCore.ParameterSet.Config as cms

def L1GtParametersTester(*args, **kwargs):
  mod = cms.EDAnalyzer('L1GtParametersTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
