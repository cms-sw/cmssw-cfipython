import FWCore.ParameterSet.Config as cms

createIdealTkAlRecords = cms.EDAnalyzer('CreateIdealTkAlRecords',
  alignToGlobalTag = cms.untracked.bool(False),
  skipSubDetectors = cms.untracked.vstring(),
  createReferenceRcd = cms.untracked.bool(False)
)
