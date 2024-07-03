import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_HGCalSoARecHitsProducer(**kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::HGCalSoARecHitsProducer',
    detector = cms.string('EE'),
    recHits = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    maxNumberOfThickIndices = cms.uint32(6),
    fcPerEle = cms.double(0.00016020506),
    fcPerMip = cms.required.vdouble,
    thicknessCorrection = cms.required.vdouble,
    noises = cms.required.vdouble,
    dEdXweights = cms.required.vdouble,
    ecut = cms.double(3),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
