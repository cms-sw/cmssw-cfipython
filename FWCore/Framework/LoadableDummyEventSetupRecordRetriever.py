import FWCore.ParameterSet.Config as cms

def LoadableDummyEventSetupRecordRetriever(**kwargs):
  mod = cms.ESSource('LoadableDummyEventSetupRecordRetriever',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
