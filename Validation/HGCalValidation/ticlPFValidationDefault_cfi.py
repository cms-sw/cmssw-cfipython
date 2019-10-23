import FWCore.ParameterSet.Config as cms

ticlPFValidationDefault = cms.EDAnalyzer('TICLPFValidation',
  folder = cms.string('HGCAL/'),
  ticlPFCandidates = cms.InputTag('pfTICLProducer'),
  mightGet = cms.optional.untracked.vstring
)
