import FWCore.ParameterSet.Config as cms

def MTDRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('MTDRecHitProducer',
    barrelUncalibratedRecHits = cms.InputTag('mtdUncalibratedRecHits', 'FTLBarrel'),
    endcapUncalibratedRecHits = cms.InputTag('mtdUncalibratedRecHits', 'FTLEndcap'),
    BarrelHitsName = cms.string('FTLBarrel'),
    EndcapHitsName = cms.string('FTLEndcap'),
    barrel = cms.PSet(),
    endcap = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
