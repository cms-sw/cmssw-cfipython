import FWCore.ParameterSet.Config as cms

def ThroughputService(**kwargs):
  mod = cms.Service('ThroughputService',
    eventRange = cms.untracked.uint32(10000),
    eventResolution = cms.untracked.uint32(1),
    printEventSummary = cms.untracked.bool(False),
    enableDQM = cms.untracked.bool(True),
    dqmPathByProcesses = cms.untracked.bool(False),
    dqmPath = cms.untracked.string('HLT/Throughput'),
    timeRange = cms.untracked.double(60000),
    timeResolution = cms.untracked.double(10)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
