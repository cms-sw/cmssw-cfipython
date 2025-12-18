import FWCore.ParameterSet.Config as cms

def HcalCellSizeCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalCellSizeCheck',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
