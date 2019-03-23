import FWCore.ParameterSet.Config as cms

caloRecoTauDiscriminationByNProngs = cms.EDProducer('CaloRecoTauDiscriminationByNProngs',
  nProngs = cms.uint32(0),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  ),
  CaloTauProducer = cms.InputTag('caloRecoTauProducer'),
  BooleanOutput = cms.bool(True)
)
