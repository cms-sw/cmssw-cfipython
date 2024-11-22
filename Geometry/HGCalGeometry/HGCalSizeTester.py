import FWCore.ParameterSet.Config as cms

def HGCalSizeTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalSizeTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
