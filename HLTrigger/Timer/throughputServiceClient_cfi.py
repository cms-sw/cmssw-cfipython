import FWCore.ParameterSet.Config as cms

throughputServiceClient = cms.EDAnalyzer('ThroughputServiceClient',
  dqmPath = cms.untracked.string('HLT/Throughput')
)
