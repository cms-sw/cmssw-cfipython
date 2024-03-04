import FWCore.ParameterSet.Config as cms

def UTC_Vd2(**kwargs):
  mod = cms.EDAnalyzer('UTC_Vd2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
