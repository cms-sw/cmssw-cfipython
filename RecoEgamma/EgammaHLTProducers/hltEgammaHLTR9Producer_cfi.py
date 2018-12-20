import FWCore.ParameterSet.Config as cms

hltEgammaHLTR9Producer = cms.EDProducer('EgammaHLTR9Producer',
  recoEcalCandidateProducer = cms.InputTag('hltRecoEcalCandidate'),
  ecalRechitEB = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB'),
  ecalRechitEE = cms.InputTag('hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE'),
  useSwissCross = cms.bool(False)
)
