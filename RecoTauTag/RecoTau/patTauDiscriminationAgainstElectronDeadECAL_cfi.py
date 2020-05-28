import FWCore.ParameterSet.Config as cms

patTauDiscriminationAgainstElectronDeadECAL = cms.EDProducer('PATTauDiscriminationAgainstElectronDeadECAL',
  dR = cms.double(0.08),
  minStatus = cms.uint32(12),
  extrapolateToECalEntrance = cms.bool(True),
  verbosity = cms.int32(0),
  PATTauProducer = cms.InputTag('fixme'),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('AND'),
    leadTrack = cms.PSet(
      cut = cms.double(0),
      Producer = cms.InputTag('fixme')
    ),
    decayMode = cms.PSet(
      cut = cms.double(0),
      Producer = cms.InputTag('fixme')
    )
  )
)
