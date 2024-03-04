import FWCore.ParameterSet.Config as cms

def EgammaSuperClusters(**kwargs):
  mod = cms.EDProducer('EgammaSuperClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
