import FWCore.ParameterSet.Config as cms

hltEcalPFClusterIsolationProducerRecoRecoEcalCandidate = cms.EDProducer('EgammaHLTEcalPFClusterIsolationProducer',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
  pfClusterProducer = cms.InputTag('hltParticleFlowClusterECAL'),
  rhoProducer = cms.InputTag('fixedGridRhoFastjetAllCalo'),
  doRhoCorrection = cms.bool(False),
  rhoMax = cms.double(99999999),
  rhoScale = cms.double(1),
  drMax = cms.double(0.3),
  drVetoBarrel = cms.double(0),
  drVetoEndcap = cms.double(0),
  etaStripBarrel = cms.double(0),
  etaStripEndcap = cms.double(0),
  energyBarrel = cms.double(0),
  energyEndcap = cms.double(0),
  effectiveAreas = cms.vdouble(
    0.29,
    0.21
  ),
  absEtaLowEdges = cms.vdouble(
    0,
    1.479
  ),
  mightGet = cms.optional.untracked.vstring
)
