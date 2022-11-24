import FWCore.ParameterSet.Config as cms

ecalUncalibRecHitPhase2WeightsProducerGPU = cms.EDProducer('EcalUncalibRecHitPhase2WeightsProducerGPU',
  recHitsLabelEB = cms.string('EcalUncalibRecHitsEB'),
  weights = cms.vdouble(
    -0.121016,
    -0.119899,
    -0.120923,
    -0.0848959,
    0.261041,
    0.509881,
    0.373591,
    0.134899,
    -0.0233605,
    -0.0913195,
    -0.112452,
    -0.118596,
    -0.121737,
    -0.121737,
    -0.121737,
    -0.121737
  ),
  digisLabelEB = cms.InputTag('simEcalUnsuppressedDigis'),
  mightGet = cms.optional.untracked.vstring
)
