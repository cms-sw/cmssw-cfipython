import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationByHPSSelection(*args, **kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationByHPSSelection',
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
      ),
      template = cms.PSetTemplate(
        minPi0Mass = cms.double(-1000),
        maxMass = cms.required.string,
        maxPi0Mass = cms.double(1000000000),
        nPiZeros = cms.required.uint32,
        minMass = cms.required.double,
        nChargedPFCandsMin = cms.uint32(0),
        nTracksMin = cms.uint32(0),
        nCharged = cms.required.uint32,
        applyBendCorrection = cms.PSet(
          phi = cms.required.bool,
          eta = cms.required.bool,
          mass = cms.required.bool
        ),
        assumeStripMass = cms.double(-1)
      )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
