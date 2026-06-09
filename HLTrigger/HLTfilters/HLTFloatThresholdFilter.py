import FWCore.ParameterSet.Config as cms

def HLTFloatThresholdFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTFloatThresholdFilter',
    src = cms.InputTag(''),
    threshold = cms.double(-99),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
