import FWCore.ParameterSet.Config as cms

throughputServiceClient = cms.EDProducer('ThroughputServiceClient',
  dqmPath = cms.untracked.string('HLT/Throughput'),
  createSummary = cms.untracked.bool(True),
  mightGet = cms.optional.untracked.vstring
)
