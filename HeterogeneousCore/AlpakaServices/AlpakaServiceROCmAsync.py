import FWCore.ParameterSet.Config as cms

def AlpakaServiceROCmAsync(**kwargs):
  mod = cms.Service('AlpakaServiceROCmAsync',
    enabled = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
