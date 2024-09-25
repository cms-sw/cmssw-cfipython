import FWCore.ParameterSet.Config as cms

def EgammaBasicClusters(*args, **kwargs):
  mod = cms.EDProducer('EgammaBasicClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
