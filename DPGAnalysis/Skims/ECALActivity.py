import FWCore.ParameterSet.Config as cms

def ECALActivity(**kwargs):
  mod = cms.EDFilter('ECALActivity',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
