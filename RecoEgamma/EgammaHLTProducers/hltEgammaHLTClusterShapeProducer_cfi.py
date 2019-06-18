import FWCore.ParameterSet.Config as cms

hltEgammaHLTClusterShapeProducer = cms.EDProducer('EgammaHLTClusterShapeProducer',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
  ecalRechitEB = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB'),
  ecalRechitEE = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE'),
  isIeta = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
