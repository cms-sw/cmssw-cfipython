import FWCore.ParameterSet.Config as cms

def CPU(*args, **kwargs):
  mod = cms.Service('CPU',
    reportCPUProperties = cms.untracked.bool(False),
    disableJobReportOutput = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
