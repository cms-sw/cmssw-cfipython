import FWCore.ParameterSet.Config as cms

def HcalLuttoDB(**kwargs):
  mod = cms.EDAnalyzer('HcalLuttoDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
