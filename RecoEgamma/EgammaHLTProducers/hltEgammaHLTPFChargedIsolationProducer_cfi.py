import FWCore.ParameterSet.Config as cms

hltEgammaHLTPFChargedIsolationProducer = cms.EDProducer('EgammaHLTPFChargedIsolationProducer',
  electronProducer = cms.InputTag('hltEle27WP80PixelMatchElectronsL1SeededPF'),
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidatePF'),
  pfCandidatesProducer = cms.InputTag('hltParticleFlowReg'),
  beamSpotProducer = cms.InputTag('hltOnlineBeamSpot'),
  useGsfTrack = cms.bool(False),
  useSCRefs = cms.bool(False),
  drMax = cms.double(0.3),
  drVetoBarrel = cms.double(0.02),
  drVetoEndcap = cms.double(0.02),
  ptMin = cms.double(0),
  dzMax = cms.double(0.2),
  dxyMax = cms.double(0.1),
  pfCandidateType = cms.int32(1)
)
