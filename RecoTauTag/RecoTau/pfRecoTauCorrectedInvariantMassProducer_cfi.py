import FWCore.ParameterSet.Config as cms

pfRecoTauCorrectedInvariantMassProducer = cms.EDProducer('PFRecoTauCorrectedInvariantMassProducer',
  PFTauDecayModeProducer = cms.required.InputTag,
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
  ),
  mightGet = cms.optional.untracked.vstring
)
