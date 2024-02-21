import FWCore.ParameterSet.Config as cms

hltEgammaHLTClusterShapeProducer = cms.EDProducer('EgammaHLTClusterShapeProducer',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
  ecalRechitEB = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB'),
  ecalRechitEE = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE'),
  multThresEB = cms.double(1),
  multThresEE = cms.double(1.25),
  mightGet = cms.optional.untracked.vstring
)
