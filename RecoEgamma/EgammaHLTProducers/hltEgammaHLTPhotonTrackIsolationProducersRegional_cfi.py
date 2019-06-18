import FWCore.ParameterSet.Config as cms

hltEgammaHLTPhotonTrackIsolationProducersRegional = cms.EDProducer('EgammaHLTPhotonTrackIsolationProducersRegional',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
  trackProducer = cms.InputTag('hltL1SeededEgammaRegionalCTFFinalFitWithMaterial'),
  countTracks = cms.bool(False),
  egTrkIsoPtMin = cms.double(1),
  egTrkIsoConeSize = cms.double(0.29),
  egTrkIsoZSpan = cms.double(999999),
  egTrkIsoRSpan = cms.double(999999),
  egTrkIsoVetoConeSize = cms.double(0.06),
  egTrkIsoStripBarrel = cms.double(0.03),
  egTrkIsoStripEndcap = cms.double(0.03),
  mightGet = cms.optional.untracked.vstring
)
