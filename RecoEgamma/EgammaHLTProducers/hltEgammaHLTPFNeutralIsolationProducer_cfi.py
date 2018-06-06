import FWCore.ParameterSet.Config as cms

hltEgammaHLTPFNeutralIsolationProducer = cms.EDProducer('EgammaHLTPFNeutralIsolationProducer',
  electronProducer = cms.InputTag('hltEle27WP80PixelMatchElectronsL1SeededPF'),
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
  pfCandidatesProducer = cms.InputTag('hltParticleFlowReg'),
  rhoProducer = cms.InputTag('fixedGridRhoFastjetAllCalo'),
  doRhoCorrection = cms.bool(False),
  rhoMax = cms.double(99999999),
  rhoScale = cms.double(1),
  effectiveAreaBarrel = cms.double(0.101),
  effectiveAreaEndcap = cms.double(0.046),
  useSCRefs = cms.bool(False),
  drMax = cms.double(0.3),
  drVetoBarrel = cms.double(0),
  drVetoEndcap = cms.double(0),
  etaStripBarrel = cms.double(0),
  etaStripEndcap = cms.double(0),
  energyBarrel = cms.double(0),
  energyEndcap = cms.double(0),
  pfCandidateType = cms.int32(5)
)
