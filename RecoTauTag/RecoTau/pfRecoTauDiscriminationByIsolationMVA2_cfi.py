import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByIsolationMVA2 = cms.EDProducer('PFRecoTauDiscriminationByIsolationMVA2',
  verbosity = cms.int32(0),
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