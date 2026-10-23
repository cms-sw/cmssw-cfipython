import FWCore.ParameterSet.Config as cms

def HGCalTestRecHitTool(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTestRecHitTool',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
