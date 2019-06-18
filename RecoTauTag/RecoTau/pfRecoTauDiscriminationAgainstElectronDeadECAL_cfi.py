import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationAgainstElectronDeadECAL = cms.EDProducer('PFRecoTauDiscriminationAgainstElectronDeadECAL',
  verbosity = cms.int32(0),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(
      cut = cms.required.double,
      Producer = cms.required.InputTag
    ),
    decayMode = cms.PSet(
      cut = cms.required.double,
      Producer = cms.required.InputTag
    )
  ),
  dR = cms.double(0.08),
  PFTauProducer = cms.InputTag('pfTauProducer'),
  minStatus = cms.uint32(12),
  mightGet = cms.optional.untracked.vstring
)
