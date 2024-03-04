import FWCore.ParameterSet.Config as cms

def PrintTotemDAQMapping(**kwargs):
  mod = cms.EDAnalyzer('PrintTotemDAQMapping',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
