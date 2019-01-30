import FWCore.ParameterSet.Config as cms

hltEgammaHLTBcHcalIsolationProducersRegional = cms.EDProducer('EgammaHLTBcHcalIsolationProducersRegional',
  recoEcalCandidateProducer = cms.InputTag('hltRecoEcalCandidate'),
  caloTowerProducer = cms.InputTag('hltTowerMakerForAll'),
  rhoProducer = cms.InputTag('fixedGridRhoFastjetAllCalo'),
  doRhoCorrection = cms.bool(False),
  rhoMax = cms.double(999999),
  rhoScale = cms.double(1),
  etMin = cms.double(-1),
  innerCone = cms.double(0),
  outerCone = cms.double(0.15),
  depth = cms.int32(-1),
  doEtSum = cms.bool(False),
  effectiveAreaBarrel = cms.double(0.021),
  effectiveAreaEndcap = cms.double(0.04),
  useSingleTower = cms.bool(False)
)
