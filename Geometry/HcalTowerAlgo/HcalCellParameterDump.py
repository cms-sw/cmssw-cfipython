import FWCore.ParameterSet.Config as cms

def HcalCellParameterDump(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalCellParameterDump',
    SubDetector = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
