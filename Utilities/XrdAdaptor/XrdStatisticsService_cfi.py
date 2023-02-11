import FWCore.ParameterSet.Config as cms

XrdStatisticsService = cms.Service('XrdStatisticsService',
  reportToFJR = cms.untracked.bool(True)
)
