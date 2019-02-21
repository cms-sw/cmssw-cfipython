import FWCore.ParameterSet.Config as cms

psMonitorClient = cms.EDProducer('PSMonitorClient',
  dqmPath = cms.untracked.string('HLT/PSMonitoring'),
  me = cms.PSet(
    folder = cms.string('HLT/PSMonitoring'),
    name = cms.string('psColumnVSlumi')
  )
)
