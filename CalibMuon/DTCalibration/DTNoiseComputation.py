import FWCore.ParameterSet.Config as cms

def DTNoiseComputation(*args, **kwargs):
  mod = cms.EDAnalyzer('DTNoiseComputation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
