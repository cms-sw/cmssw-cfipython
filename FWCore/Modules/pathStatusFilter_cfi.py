import FWCore.ParameterSet.Config as cms

pathStatusFilter = cms.EDFilter('PathStatusFilter',
  logicalExpression = cms.string(''),
  verbose = cms.untracked.bool(False)
)
