import FWCore.ParameterSet.Config as cms

def HGCalSoARecHitsProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('HGCalSoARecHitsProducer@alpaka',
    detector = cms.string('EE'),
    recHits = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    maxNumberOfThickIndices = cms.uint32(6),
    fcPerEle = cms.float(0.000160205062),
    fcPerMip = cms.required.vfloat,
    thicknessCorrection = cms.required.vfloat,
    noises = cms.required.vfloat,
    dEdXweights = cms.required.vfloat,
    ecut = cms.float(3),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
