import FWCore.ParameterSet.Config as cms

def myRawAna(**kwargs):
  mod = cms.EDAnalyzer('myRawAna',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
