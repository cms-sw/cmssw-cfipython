import FWCore.ParameterSet.Config as cms

hltEgammaHLTHcalIsolationProducersRegional = cms.EDProducer('EgammaHLTHcalIsolationProducersRegional',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
  hbheRecHitProducer = cms.InputTag('hltHbhereco'),
  rhoProducer = cms.InputTag('fixedGridRhoFastjetAllCalo'),
  doRhoCorrection = cms.bool(False),
  rhoMax = cms.double(99999999),
  rhoScale = cms.double(1),
  eMinHB = cms.double(0.7),
  eMinHE = cms.double(0.8),
  etMinHB = cms.double(-1),
  etMinHE = cms.double(-1),
  innerCone = cms.double(0),
  outerCone = cms.double(0.15),
  depth = cms.int32(-1),
  doEtSum = cms.bool(False),
  effectiveAreaBarrel = cms.double(0.105),
  effectiveAreaEndcap = cms.double(0.17)
)
