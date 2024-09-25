import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_HGCalSoARecHitsProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::HGCalSoARecHitsProducer',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
