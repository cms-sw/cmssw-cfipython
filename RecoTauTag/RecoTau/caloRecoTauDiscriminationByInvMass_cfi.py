import FWCore.ParameterSet.Config as cms

caloRecoTauDiscriminationByInvMass = cms.EDProducer('CaloRecoTauDiscriminationByInvMass',
  invMassMin = cms.double(0),
  CaloTauProducer = cms.InputTag('caloRecoTauProducer'),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  ),
  BooleanOutput = cms.bool(True),
  invMassMax = cms.double(1.4)
)
