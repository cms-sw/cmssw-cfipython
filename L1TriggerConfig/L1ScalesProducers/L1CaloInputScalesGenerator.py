import FWCore.ParameterSet.Config as cms

def L1CaloInputScalesGenerator(*args, **kwargs):
  mod = cms.EDAnalyzer('L1CaloInputScalesGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
