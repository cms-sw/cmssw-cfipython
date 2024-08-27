import FWCore.ParameterSet.Config as cms

def EcalUncalibRecHitPhase2WeightsProducer(**kwargs):
  mod = cms.EDProducer('EcalUncalibRecHitPhase2WeightsProducer',
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    tRise = cms.double(0.2),
    tFall = cms.double(2),
    ampWeights = cms.vdouble(
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
    timeWeights = cms.vdouble(
      0.429452,
      0.442762,
      0.413327,
      0.858327,
      4.42324,
      2.04369,
      -3.42426,
      -4.16258,
      -2.36061,
      -0.725371,
      0.0727267,
      0.326005,
      0.402035,
      0.404287,
      0.434207,
      0.422775
    ),
    BarrelDigis = cms.InputTag('simEcalUnsuppressedDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
