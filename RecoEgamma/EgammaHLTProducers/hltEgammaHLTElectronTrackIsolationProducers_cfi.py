import FWCore.ParameterSet.Config as cms

hltEgammaHLTElectronTrackIsolationProducers = cms.EDProducer('EgammaHLTElectronTrackIsolationProducers',
  electronProducer = cms.InputTag('hltEleAnyWP80PixelMatchElectronsL1Seeded'),
  trackProducer = cms.InputTag('hltL1SeededEgammaRegionalCTFFinalFitWithMaterial'),
  recoEcalCandidateProducer = cms.InputTag(''),
  beamSpotProducer = cms.InputTag('hltOnlineBeamSpot'),
  egTrkIsoPtMin = cms.double(1),
  egTrkIsoConeSize = cms.double(0.3),
  egTrkIsoZSpan = cms.double(0.15),
  egTrkIsoRSpan = cms.double(999999),
  egTrkIsoVetoConeSizeBarrel = cms.double(0.03),
  egTrkIsoVetoConeSizeEndcap = cms.double(0.03),
  egTrkIsoStripBarrel = cms.double(0.03),
  egTrkIsoStripEndcap = cms.double(0.03),
  useGsfTrack = cms.bool(False),
  useSCRefs = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
