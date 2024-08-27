import FWCore.ParameterSet.Config as cms

def HGCalTestRecHitTools(**kwargs):
  mod = cms.EDAnalyzer('HGCalTestRecHitTools',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
