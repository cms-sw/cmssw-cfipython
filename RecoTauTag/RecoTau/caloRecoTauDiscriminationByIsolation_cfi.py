import FWCore.ParameterSet.Config as cms

caloRecoTauDiscriminationByIsolation = cms.EDProducer('CaloRecoTauDiscriminationByIsolation',
  CaloTauProducer = cms.InputTag('fixme'),
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
