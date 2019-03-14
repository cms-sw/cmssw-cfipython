import FWCore.ParameterSet.Config as cms

throughputServiceClient = cms.EDProducer('ThroughputServiceClient',
  dqmPath = cms.untracked.string('HLT/Throughput')
)
