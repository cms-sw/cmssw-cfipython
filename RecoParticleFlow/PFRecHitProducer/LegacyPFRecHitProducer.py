import FWCore.ParameterSet.Config as cms

def LegacyPFRecHitProducer(**kwargs):
  mod = cms.EDProducer('LegacyPFRecHitProducer',
    src = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
