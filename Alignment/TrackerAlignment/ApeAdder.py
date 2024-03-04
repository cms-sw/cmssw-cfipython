import FWCore.ParameterSet.Config as cms

def ApeAdder(**kwargs):
  mod = cms.EDAnalyzer('ApeAdder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
