import FWCore.ParameterSet.Config as cms

alcaDiJetsProducer = cms.EDProducer('AlCaDiJetsProducer',
  PFjetInput = cms.InputTag('ak4PFJetsCHS'),
  HBHEInput = cms.InputTag('hbhereco'),
  HFInput = cms.InputTag('hfreco'),
  HOInput = cms.InputTag('horeco'),
  particleFlowInput = cms.InputTag('particleFlow'),
  VertexInput = cms.InputTag('offlinePrimaryVertices'),
  MinPtJet = cms.double(20),
  mightGet = cms.optional.untracked.vstring
)
