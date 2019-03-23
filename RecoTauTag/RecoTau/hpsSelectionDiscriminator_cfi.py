import FWCore.ParameterSet.Config as cms

hpsSelectionDiscriminator = cms.EDProducer('PFRecoTauDiscriminationByHPSSelection',
  PFTauProducer = cms.InputTag('combinatoricRecoTaus'),
  verbosity = cms.int32(0),
  minTauPt = cms.double(0),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and')
  ),
  matchingCone = cms.double(0.5),
  minPixelHits = cms.int32(1),
  requireTauChargedHadronsToBeChargedPFCands = cms.bool(False)
)
