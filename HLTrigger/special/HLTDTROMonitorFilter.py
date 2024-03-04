import FWCore.ParameterSet.Config as cms

def HLTDTROMonitorFilter(**kwargs):
  mod = cms.EDFilter('HLTDTROMonitorFilter',
    inputLabel = cms.InputTag('source'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
