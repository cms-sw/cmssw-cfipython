import FWCore.ParameterSet.Config as cms

def ModelpMSSMFilter(**kwargs):
  mod = cms.EDFilter('ModelpMSSMFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
