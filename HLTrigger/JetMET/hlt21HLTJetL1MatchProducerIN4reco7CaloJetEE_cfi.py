import FWCore.ParameterSet.Config as cms

hlt21HLTJetL1MatchProducerIN4reco7CaloJetEE = cms.EDProducer('HLTCaloJetL1MatchProducer',
  jetsInput = cms.InputTag('hltAntiKT5PFJets'),
  L1TauJets = cms.InputTag('hltL1extraParticles', 'Tau'),
  L1CenJets = cms.InputTag('hltL1extraParticles', 'Central'),
  L1ForJets = cms.InputTag('hltL1extraParticles', 'Forward'),
  DeltaR = cms.double(0.5)
)
