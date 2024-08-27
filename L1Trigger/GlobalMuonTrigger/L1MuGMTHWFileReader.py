import FWCore.ParameterSet.Config as cms

def L1MuGMTHWFileReader(**kwargs):
  mod = cms.Source('L1MuGMTHWFileReader')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
