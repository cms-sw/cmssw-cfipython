import FWCore.ParameterSet.Config as cms

hltHcalMETNoiseFilter = cms.EDFilter('HLTHcalMETNoiseFilter',
  HcalNoiseRBXCollection = cms.InputTag('hltHcalNoiseInfoProducer'),
  severity = cms.int32(1),
  maxNumRBXs = cms.int32(2),
  numRBXsToConsider = cms.int32(2),
  needEMFCoincidence = cms.bool(True),
  minRBXEnergy = cms.double(50),
  minRatio = cms.double(-999),
  maxRatio = cms.double(999),
  minHPDHits = cms.int32(17),
  minRBXHits = cms.int32(999),
  minHPDNoOtherHits = cms.int32(10),
  minZeros = cms.int32(10),
  minHighEHitTime = cms.double(-9999),
  maxHighEHitTime = cms.double(9999),
  maxRBXEMF = cms.double(0.02),
  minRecHitE = cms.double(1.5),
  minLowHitE = cms.double(10),
  minHighHitE = cms.double(25),
  minR45HitE = cms.double(5),
  TS4TS5EnergyThreshold = cms.double(50),
  TS4TS5UpperThreshold = cms.vdouble(
    70,
    90,
    100,
    400,
    4000
  ),
  TS4TS5UpperCut = cms.vdouble(
    1,
    0.8,
    0.75,
    0.72,
    0.72
  ),
  TS4TS5LowerThreshold = cms.vdouble(
    100,
    120,
    150,
    200,
    300,
    400,
    500
  ),
  TS4TS5LowerCut = cms.vdouble(
    -1,
    -0.7,
    -0.4,
    -0.2,
    -0.08,
    0,
    0.1
  )
)
