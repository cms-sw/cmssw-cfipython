import FWCore.ParameterSet.Config as cms

def CSCDigiValidator(**kwargs):
  mod = cms.EDFilter('CSCDigiValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
