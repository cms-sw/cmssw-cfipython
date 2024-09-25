import FWCore.ParameterSet.Config as cms

def L1ScalesTester(*args, **kwargs):
  mod = cms.EDAnalyzer('L1ScalesTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
