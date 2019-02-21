import FWCore.ParameterSet.Config as cms

caHitTripletEDProducer = cms.EDProducer('CAHitTripletEDProducer',
  doublets = cms.InputTag('hitPairEDProducer'),
  extraHitRPhitolerance = cms.double(0.06),
  useBendingCorrection = cms.bool(False),
  CAThetaCut = cms.double(0.00125),
  CAPhiCut = cms.double(0.1),
  CAHardPtCut = cms.double(0),
  maxChi2 = cms.PSet(
    pt1 = cms.double(0.8),
    pt2 = cms.double(2),
    value1 = cms.double(50),
    value2 = cms.double(8),
    enabled = cms.bool(True)
  ),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string('none')
  )
)
