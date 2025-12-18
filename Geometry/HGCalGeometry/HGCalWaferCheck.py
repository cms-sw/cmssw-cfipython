import FWCore.ParameterSet.Config as cms

def HGCalWaferCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalWaferCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
