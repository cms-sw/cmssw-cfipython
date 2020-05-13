import FWCore.ParameterSet.Config as cms

ticlPFValidationDefault = cms.EDProducer('TICLPFValidation',
  folder = cms.string('HGCAL/'),
  ticlPFCandidates = cms.InputTag('pfTICL'),
  mightGet = cms.optional.untracked.vstring
)
