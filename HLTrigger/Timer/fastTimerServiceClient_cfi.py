import FWCore.ParameterSet.Config as cms

fastTimerServiceClient = cms.EDAnalyzer('FastTimerServiceClient',
  dqmPath = cms.untracked.string('HLT/TimerService')
)
