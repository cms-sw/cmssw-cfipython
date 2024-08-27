import FWCore.ParameterSet.Config as cms

def HcalTBWriter(**kwargs):
  mod = cms.EDAnalyzer('HcalTBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
