import FWCore.ParameterSet.Config as cms

hltHcalPFClusterIsolationProducerRecoRecoEcalCandidate = cms.EDProducer('EgammaHLTHcalPFClusterIsolationProducer',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
  pfClusterProducerHCAL = cms.InputTag('hltParticleFlowClusterHCAL'),
  useHF = cms.bool(False),
  pfClusterProducerHFEM = cms.InputTag(''),
  pfClusterProducerHFHAD = cms.InputTag(''),
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
  useEt = cms.bool(True),
  effectiveAreas = cms.vdouble(
    0.2,
    0.25
  ),
  absEtaLowEdges = cms.vdouble(
    0,
    1.479
  ),
  mightGet = cms.optional.untracked.vstring
)
