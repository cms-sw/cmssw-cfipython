import FWCore.ParameterSet.Config as cms

TimerService = cms.Service('TimerService',
  useCPUtime = cms.untracked.bool(True)
)
