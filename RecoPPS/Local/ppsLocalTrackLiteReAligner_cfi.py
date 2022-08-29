import FWCore.ParameterSet.Config as cms

ppsLocalTrackLiteReAligner = cms.EDProducer('PPSLocalTrackLiteReAligner',
  inputTrackTag = cms.InputTag('ctppsLocalTrackLiteProducer'),
  alignmentTag = cms.ESInputTag('', ''),
  outputTrackTag = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
