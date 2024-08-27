import FWCore.ParameterSet.Config as cms

def BsJpsiPhiFilter(**kwargs):
  mod = cms.EDFilter('BsJpsiPhiFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
