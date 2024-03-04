import FWCore.ParameterSet.Config as cms

def HcalCableMapper(**kwargs):
  mod = cms.EDAnalyzer('HcalCableMapper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
