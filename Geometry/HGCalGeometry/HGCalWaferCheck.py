import FWCore.ParameterSet.Config as cms

def HGCalWaferCheck(**kwargs):
  mod = cms.EDAnalyzer('HGCalWaferCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
