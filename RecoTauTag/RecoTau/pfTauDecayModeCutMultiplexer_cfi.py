import FWCore.ParameterSet.Config as cms

pfTauDecayModeCutMultiplexer = cms.EDProducer('PFTauDecayModeCutMultiplexer',
  PFTauProducer = cms.InputTag('fixme'),
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
