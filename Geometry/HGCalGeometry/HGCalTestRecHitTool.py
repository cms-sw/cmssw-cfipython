import FWCore.ParameterSet.Config as cms

def HGCalTestRecHitTool(**kwargs):
  mod = cms.EDAnalyzer('HGCalTestRecHitTool',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
