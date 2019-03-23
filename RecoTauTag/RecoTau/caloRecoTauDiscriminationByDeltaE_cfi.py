import FWCore.ParameterSet.Config as cms

caloRecoTauDiscriminationByDeltaE = cms.EDProducer('CaloRecoTauDiscriminationByDeltaE',
  deltaEmin = cms.double(-0.15),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  ),
  deltaEmax = cms.double(1),
  BooleanOutput = cms.bool(True),
  TauProducer = cms.InputTag('caloRecoTauProducer')
)
