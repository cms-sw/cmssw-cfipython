import FWCore.ParameterSet.Config as cms

def PFRecHitProducerTest(**kwargs):
  mod = cms.EDProducer('PFRecHitProducerTest',
    caloRecHits = cms.untracked.InputTag(''),
    pfRecHitsSource1 = cms.required.untracked.InputTag,
    pfRecHitsSource2 = cms.required.untracked.InputTag,
    pfRecHitsType1 = cms.untracked.string('legacy'),
    pfRecHitsType2 = cms.untracked.string('alpaka'),
    title = cms.untracked.string(''),
    dumpFirstEvent = cms.untracked.bool(False),
    dumpFirstError = cms.untracked.bool(False),
    strictCompare = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
