import FWCore.ParameterSet.Config as cms

def CPU(**kwargs):
  mod = cms.Service('CPU',
    reportCPUProperties = cms.untracked.bool(False),
    disableJobReportOutput = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
