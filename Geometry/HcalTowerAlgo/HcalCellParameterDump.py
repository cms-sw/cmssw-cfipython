import FWCore.ParameterSet.Config as cms

def HcalCellParameterDump(**kwargs):
  mod = cms.EDAnalyzer('HcalCellParameterDump',
    SubDetector = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
