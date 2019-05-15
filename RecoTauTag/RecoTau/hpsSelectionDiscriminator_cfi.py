import FWCore.ParameterSet.Config as cms

hpsSelectionDiscriminator = cms.EDProducer('PFRecoTauDiscriminationByHPSSelection',
  PFTauProducer = cms.InputTag('combinatoricRecoTaus'),
  verbosity = cms.int32(0),
  minTauPt = cms.double(0),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and')
  ),
  decayModes = cms.VPSet(
    cms.PSet(
      assumeStripMass = cms.double(-1),
      maxPi0Mass = cms.double(1000000000),
      minPi0Mass = cms.double(-1000),
      nChargedPFCandsMin = cms.uint32(0),
      nTracksMin = cms.uint32(0)
    )
  ),
  matchingCone = cms.double(0.5),
  minPixelHits = cms.int32(1),
  requireTauChargedHadronsToBeChargedPFCands = cms.bool(False)
)
