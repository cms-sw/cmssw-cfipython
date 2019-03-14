import FWCore.ParameterSet.Config as cms

ThroughputService = cms.Service('ThroughputService',
  timeRange = cms.untracked.double(60000),
  timeResolution = cms.untracked.double(10),
  dqmPath = cms.untracked.string('HLT/Throughput')
)
