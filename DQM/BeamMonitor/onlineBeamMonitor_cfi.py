import FWCore.ParameterSet.Config as cms

onlineBeamMonitor = cms.EDProducer('OnlineBeamMonitor',
  MonitorName = cms.untracked.string('YourSubsystemName'),
  mightGet = cms.optional.untracked.vstring
)
