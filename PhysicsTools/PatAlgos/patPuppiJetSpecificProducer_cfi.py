import FWCore.ParameterSet.Config as cms

patPuppiJetSpecificProducer = cms.EDProducer('PATPuppiJetSpecificProducer',
  src = cms.InputTag('slimmedJets')
)
