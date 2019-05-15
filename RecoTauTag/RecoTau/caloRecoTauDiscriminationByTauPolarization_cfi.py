import FWCore.ParameterSet.Config as cms

caloRecoTauDiscriminationByTauPolarization = cms.EDProducer('CaloRecoTauDiscriminationByTauPolarization',
  CaloTauProducer = cms.InputTag('caloRecoTauProducer'),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  ),
  rtau = cms.double(0.8),
  PVProducer = cms.InputTag('offlinePrimaryVertices'),
  BooleanOutput = cms.bool(True)
)
