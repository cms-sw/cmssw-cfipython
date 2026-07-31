import FWCore.ParameterSet.Config as cms

def MTDUncalibratedRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('MTDUncalibratedRecHitProducer',
    barrelDigis = cms.InputTag('mix', 'FTLBarrel'),
    endcapDigis = cms.InputTag('mix', 'FTEndcap'),
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
