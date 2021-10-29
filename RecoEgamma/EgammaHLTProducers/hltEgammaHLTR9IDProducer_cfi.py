import FWCore.ParameterSet.Config as cms

hltEgammaHLTR9IDProducer = cms.EDProducer('EgammaHLTR9IDProducer',
  recoEcalCandidateProducer = cms.InputTag('hltRecoEcalCandidate'),
  ecalRechitEB = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB'),
  ecalRechitEE = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE'),
  mightGet = cms.optional.untracked.vstring
)
