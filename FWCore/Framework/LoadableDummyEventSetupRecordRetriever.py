import FWCore.ParameterSet.Config as cms

def LoadableDummyEventSetupRecordRetriever(*args, **kwargs):
  mod = cms.ESSource('LoadableDummyEventSetupRecordRetriever',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
