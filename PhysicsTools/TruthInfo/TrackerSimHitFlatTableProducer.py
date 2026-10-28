import FWCore.ParameterSet.Config as cms

def TrackerSimHitFlatTableProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackerSimHitFlatTableProducer',
    objName = cms.string('trackersimhits'),
    label_simhits = cms.VInputTag(
      'g4SimHits:TrackerHitsPixelBarrelLowTof',
      'g4SimHits:TrackerHitsPixelBarrelHighTof',
      'g4SimHits:TrackerHitsPixelEndcapLowTof',
      'g4SimHits:TrackerHitsPixelEndcapHighTof'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
