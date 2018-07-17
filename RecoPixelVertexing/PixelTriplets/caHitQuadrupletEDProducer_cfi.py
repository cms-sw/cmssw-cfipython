import FWCore.ParameterSet.Config as cms

caHitQuadrupletEDProducer = cms.EDProducer('CAHitQuadrupletEDProducer',
  doublets = cms.InputTag('hitPairEDProducer'),
  extraHitRPhitolerance = cms.double(0.1),
  fitFastCircle = cms.bool(False),
  fitFastCircleChi2Cut = cms.bool(False),
  useBendingCorrection = cms.bool(False),
  CAThetaCut = cms.double(0.00125),
  CAPhiCut = cms.double(10),
  CAHardPtCut = cms.double(0),
  maxChi2 = cms.PSet(
    pt1 = cms.double(0.2),
    pt2 = cms.double(1.5),
    value1 = cms.double(500),
    value2 = cms.double(50),
    enabled = cms.bool(True)
  ),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string('none')
  )
)
