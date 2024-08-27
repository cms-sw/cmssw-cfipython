import FWCore.ParameterSet.Config as cms

def WriteTotemDAQMapping(**kwargs):
  mod = cms.EDAnalyzer('WriteTotemDAQMapping',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
