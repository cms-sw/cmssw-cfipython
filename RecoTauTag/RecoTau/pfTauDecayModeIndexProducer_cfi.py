import FWCore.ParameterSet.Config as cms

pfTauDecayModeIndexProducer = cms.EDProducer('PFRecoTauDecayModeIndexProducer',
  PFTauDecayModeProducer = cms.InputTag('pfRecoTauDecayModeProducer'),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and')
  ),
  PFTauProducer = cms.InputTag('pfRecoTauProducer')
)
