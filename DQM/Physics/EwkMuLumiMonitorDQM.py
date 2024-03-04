import FWCore.ParameterSet.Config as cms

def EwkMuLumiMonitorDQM(**kwargs):
  mod = cms.EDProducer('EwkMuLumiMonitorDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
