import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByInvMass = cms.EDProducer('PFRecoTauDiscriminationByInvMass',
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  ),
  select = cms.PSet(),
  PFTauProducer = cms.InputTag('pfRecoTauProducer')
)
