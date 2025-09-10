import FWCore.ParameterSet.Config as cms

def EgammaSuperClusters(*args, **kwargs):
  mod = cms.EDProducer('EgammaSuperClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
