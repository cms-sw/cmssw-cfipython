import FWCore.ParameterSet.Config as cms

def CaloTowersReCreator(**kwargs):
  mod = cms.EDProducer('CaloTowersReCreator',
    EBWeight = cms.double(1),
    HBEScale = cms.double(50),
    HEDWeight = cms.double(1),
    EEWeight = cms.double(1),
    HF1Weight = cms.double(1),
    HOWeight = cms.double(1),
    HESWeight = cms.double(1),
    HF2Weight = cms.double(1),
    HESEScale = cms.double(50),
    HEDEScale = cms.double(50),
    EBEScale = cms.double(50),
    HBWeight = cms.double(1),
    EEEScale = cms.double(50),
    MomHBDepth = cms.double(0.2),
    MomHEDepth = cms.double(0.4),
    MomEBDepth = cms.double(0.3),
    MomEEDepth = cms.double(0),
    HBGrid = cms.vdouble(
      0,
      2,
      4,
      5,
      9,
      20,
      30,
      50,
      100,
      1000
    ),
    EEWeights = cms.vdouble(
      0.51,
      1.39,
      1.71,
      2.37,
      2.32,
      2.2,
      2.1,
      1.98,
      1.8
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
      2,
      4,
      5,
      9,
      20,
      30,
      50,
      100,
      300
    ),
    HBWeights = cms.vdouble(
      2,
      1.86,
      1.69,
      1.55,
      1.37,
      1.19,
      1.13,
      1.11,
      1.09,
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
      1.7,
      1.57,
      1.54,
      1.49,
      1.41,
      1.26,
      1.19,
      1.15,
      1.12,
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
      0.86,
      1.47,
      1.66,
      2.01,
      1.98,
      1.86,
      1.83,
      1.74,
      1.65
    ),
    HF1Weights = cms.vdouble(
      1,
      1,
      1,
      1,
      1
    ),
    HESGrid = cms.vdouble(
      0,
      2,
      4,
      5,
      9,
      20,
      30,
      50,
      100,
      1000
    ),
    HESWeights = cms.vdouble(
      1.7,
      1.57,
      1.54,
      1.49,
      1.41,
      1.26,
      1.19,
      1.15,
      1.12,
      1
    ),
    HEDGrid = cms.vdouble(
      0,
      2,
      4,
      5,
      9,
      20,
      30,
      50,
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
      2,
      4,
      5,
      9,
      20,
      30,
      50,
      100,
      300
    ),
    caloLabel = cms.InputTag('calotowermaker'),
    MomConstrMethod = cms.int32(1),
    HcalPhase = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
