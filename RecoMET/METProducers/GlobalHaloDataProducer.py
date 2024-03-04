import FWCore.ParameterSet.Config as cms

def GlobalHaloDataProducer(**kwargs):
  mod = cms.EDProducer('GlobalHaloDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
