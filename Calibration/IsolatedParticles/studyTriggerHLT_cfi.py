import FWCore.ParameterSet.Config as cms

studyTriggerHLT = cms.EDAnalyzer('StudyTriggerHLT',
  verbosity = cms.untracked.int32(0),
  mightGet = cms.optional.untracked.vstring
)
