import FWCore.ParameterSet.Config as cms

def HLTDTROMonitorFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTDTROMonitorFilter',
    inputLabel = cms.InputTag('source'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
