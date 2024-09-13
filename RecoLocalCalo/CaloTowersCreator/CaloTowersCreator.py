import FWCore.ParameterSet.Config as cms

def CaloTowersCreator(**kwargs):
  mod = cms.EDProducer('CaloTowersCreator',
    EBSumThreshold = cms.double(0.2),
    HF2Weight = cms.double(1),
    EBWeight = cms.double(1),
    EESumThreshold = cms.double(0.45),
    HOThreshold0 = cms.double(1.1),
    HOThresholdPlus1 = cms.double(3.5),
    HOThresholdMinus1 = cms.double(3.5),
    HOThresholdPlus2 = cms.double(3.5),
    HOThresholdMinus2 = cms.double(3.5),
    HBThreshold = cms.double(0.7),
    HBThreshold1 = cms.double(0.7),
    HBThreshold2 = cms.double(0.7),
    HF1Threshold = cms.double(0.5),
    HEDWeight = cms.double(1),
    EEWeight = cms.double(1),
    HESWeight = cms.double(1),
    HF1Weight = cms.double(1),
    HOWeight = cms.double(1),
    EBThreshold = cms.double(0.07),
    EEThreshold = cms.double(0.3),
    HcalThreshold = cms.double(-1000),
    HF2Threshold = cms.double(0.85),
    HESThreshold = cms.double(0.8),
    HESThreshold1 = cms.double(0.8),
    HEDThreshold = cms.double(0.8),
    HEDThreshold1 = cms.double(0.8),
    EcutTower = cms.double(-1000),
    HBWeight = cms.double(1),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0),
    UseHO = cms.bool(True),
    UseEtEBTreshold = cms.bool(False),
    UseSymEBTreshold = cms.bool(True),
    UseEtEETreshold = cms.bool(False),
    UseSymEETreshold = cms.bool(True),
    UseHcalRecoveredHits = cms.bool(True),
    UseEcalRecoveredHits = cms.bool(False),
    UseRejectedHitsOnly = cms.bool(False),
    UseRejectedRecoveredHcalHits = cms.bool(True),
    UseRejectedRecoveredEcalHits = cms.bool(False),
    missingHcalRescaleFactorForEcal = cms.double(0),
    AllowMissingInputs = cms.bool(False),
    HBGrid = cms.vdouble(
      -1,
      1,
      10,
      100,
      1000
    ),
    EEWeights = cms.vdouble(
      1,
      1,
      1,
      1,
      1
    ),
    HF2Weights = cms.vdouble(
      1,
      1,
      1,
      1,
      1
    ),
    HOWeights = cms.vdouble(
      1,
      1,
      1,
      1,
      1
    ),
    EEGrid = cms.vdouble(
      -1,
      1,
      10,
      100,
      1000
    ),
    HBWeights = cms.vdouble(
      1,
      1,
      1,
      1,
      1
    ),
    HF2Grid = cms.vdouble(
      -1,
      1,
      10,
      100,
      1000
    ),
    HEDWeights = cms.vdouble(
      1,
      1,
      1,
      1,
      1
    ),
    HF1Grid = cms.vdouble(
      -1,
      1,
      10,
      100,
      1000
    ),
    EBWeights = cms.vdouble(
      1,
      1,
      1,
      1,
      1
    ),
    HF1Weights = cms.vdouble(
      1,
      1,
      1,
      1,
      1
    ),
    HESGrid = cms.vdouble(
      -1,
      1,
      10,
      100,
      1000
    ),
    HESWeights = cms.vdouble(
      1,
      1,
      1,
      1,
      1
    ),
    HEDGrid = cms.vdouble(
      -1,
      1,
      10,
      100,
      1000
    ),
    HOGrid = cms.vdouble(
      -1,
      1,
      10,
      100,
      1000
    ),
    EBGrid = cms.vdouble(
      -1,
      1,
      10,
      100,
      1000
    ),
    hfInput = cms.InputTag('hfreco'),
    hbheInput = cms.InputTag('hbhereco'),
    hoInput = cms.InputTag('horeco'),
    ecalInputs = cms.VInputTag(
      'ecalRecHit:EcalRecHitsEB',
      'ecalRecHit:EcalRecHitsEE'
    ),
    MomConstrMethod = cms.int32(1),
    HcalAcceptSeverityLevel = cms.uint32(9),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring(
      'kTime',
      'kWeird',
      'kBad'
    ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32(9999),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(),
    HcalPhase = cms.int32(0),
    usePFThresholdsFromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
