import FWCore.ParameterSet.Config as cms

def DTTFMasksTester(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTFMasksTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
