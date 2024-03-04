import FWCore.ParameterSet.Config as cms

def AlpakaServiceCudaAsync(**kwargs):
  mod = cms.Service('AlpakaServiceCudaAsync',
    enabled = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
