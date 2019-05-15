import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByDeltaE = cms.EDProducer('PFRecoTauDiscriminationByDeltaE',
  deltaEmin = cms.double(-0.15),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  ),
  deltaEmax = cms.double(1),
  BooleanOutput = cms.bool(True),
  PFTauProducer = cms.InputTag('pfRecoTauProducer')
)
