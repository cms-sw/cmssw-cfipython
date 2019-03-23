import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByFlightPathSignificance = cms.EDProducer('PFRecoTauDiscriminationByFlightPathSignificance',
  flightPathSig = cms.double(1.5),
  PVProducer = cms.InputTag('offlinePrimaryVertices'),
  BooleanOutput = cms.bool(True),
  PFTauProducer = cms.InputTag('pfRecoTauProducer'),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  ),
  UsePVerror = cms.bool(True)
)
