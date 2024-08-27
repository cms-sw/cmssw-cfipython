import FWCore.ParameterSet.Config as cms

def JobReportService(**kwargs):
  mod = cms.Service('JobReportService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
