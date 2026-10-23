import FWCore.ParameterSet.Config as cms

def HeterogeneousHGCalRecHitsValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('HeterogeneousHGCalRecHitsValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
