import FWCore.ParameterSet.Config as cms

FastTimerService = cms.Service('FastTimerService',
  printEventSummary = cms.untracked.bool(False),
  printRunSummary = cms.untracked.bool(True),
  printJobSummary = cms.untracked.bool(True),
  enableDQM = cms.untracked.bool(True),
  enableDQMbyModule = cms.untracked.bool(False),
  enableDQMbyPath = cms.untracked.bool(False),
  enableDQMbyLumiSection = cms.untracked.bool(False),
  enableDQMbyProcesses = cms.untracked.bool(False),
  dqmTimeRange = cms.untracked.double(1000),
  dqmTimeResolution = cms.untracked.double(5),
  dqmMemoryRange = cms.untracked.double(1000000),
  dqmMemoryResolution = cms.untracked.double(5000),
  dqmPathTimeRange = cms.untracked.double(100),
  dqmPathTimeResolution = cms.untracked.double(0.5),
  dqmPathMemoryRange = cms.untracked.double(1000000),
  dqmPathMemoryResolution = cms.untracked.double(5000),
  dqmModuleTimeRange = cms.untracked.double(40),
  dqmModuleTimeResolution = cms.untracked.double(0.2),
  dqmModuleMemoryRange = cms.untracked.double(100000),
  dqmModuleMemoryResolution = cms.untracked.double(500),
  dqmLumiSectionsRange = cms.untracked.uint32(2500),
  dqmPath = cms.untracked.string('HLT/TimerService'),
  highlightModules = cms.untracked.VPSet(
  )
)
