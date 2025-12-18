import FWCore.ParameterSet.Config as cms

def JobReportService(*args, **kwargs):
  mod = cms.Service('JobReportService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
