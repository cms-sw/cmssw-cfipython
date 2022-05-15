import FWCore.ParameterSet.Config as cms

onlineBeamMonitor = cms.EDProducer('OnlineBeamMonitor',
  MonitorName = cms.untracked.string('YourSubsystemName'),
  AppendRunToFileName = cms.untracked.bool(False),
  WriteDIPAscii = cms.untracked.bool(True),
  DIPFileName = cms.untracked.string('BeamFitResultsForDIP.txt'),
  mightGet = cms.optional.untracked.vstring
)
