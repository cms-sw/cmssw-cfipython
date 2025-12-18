import FWCore.ParameterSet.Config as cms

def DTTFParametersTester(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTFParametersTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
