import FWCore.ParameterSet.Config as cms

hltEgammaHLTHcalIsolationDoubleConeProducers = cms.EDProducer('EgammaHLTHcalIsolationDoubleConeProducers',
  recoEcalCandidateProducer = cms.InputTag('hltL1SeededRecoEcalCandidate'),
  hbRecHitProducer = cms.InputTag('hltHbhereco'),
  hfRecHitProducer = cms.InputTag('hltHfreco'),
  egHcalIsoPtMin = cms.double(0),
  egHcalIsoConeSize = cms.double(0.3),
  egHcalExclusion = cms.double(0.15)
)
