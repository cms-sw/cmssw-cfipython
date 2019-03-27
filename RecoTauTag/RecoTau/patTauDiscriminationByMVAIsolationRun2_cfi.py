import FWCore.ParameterSet.Config as cms

patTauDiscriminationByMVAIsolationRun2 = cms.EDProducer('PATTauDiscriminationByMVAIsolationRun2',
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
