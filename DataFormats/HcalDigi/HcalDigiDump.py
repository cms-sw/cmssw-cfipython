import FWCore.ParameterSet.Config as cms

def HcalDigiDump(**kwargs):
  mod = cms.EDAnalyzer('HcalDigiDump',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
