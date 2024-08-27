import FWCore.ParameterSet.Config as cms

def MuScleFitGenFilter(**kwargs):
  mod = cms.EDFilter('MuScleFitGenFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
