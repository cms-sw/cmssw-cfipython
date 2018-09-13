import FWCore.ParameterSet.Config as cms

hltHcalPFClusterIsolationProducerRecoRecoChargedCandidate = cms.EDProducer('MuonHLTHcalPFClusterIsolationProducer',
  recoCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
  pfClusterProducerHCAL = cms.InputTag('hltParticleFlowClusterHCAL'),
  useHF = cms.bool(False),
  pfClusterProducerHFEM = cms.InputTag(''),
  pfClusterProducerHFHAD = cms.InputTag(''),
  rhoProducer = cms.InputTag('fixedGridRhoFastjetAllCalo'),
  doRhoCorrection = cms.bool(False),
  rhoMax = cms.double(99999999),
  rhoScale = cms.double(1),
  effectiveAreaBarrel = cms.double(0.101),
  effectiveAreaEndcap = cms.double(0.046),
  drMax = cms.double(0.3),
  drVetoBarrel = cms.double(0),
  drVetoEndcap = cms.double(0),
  etaStripBarrel = cms.double(0),
  etaStripEndcap = cms.double(0),
  energyBarrel = cms.double(0),
  energyEndcap = cms.double(0),
  useEt = cms.bool(True)
)
