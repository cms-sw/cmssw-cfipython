import FWCore.ParameterSet.Config as cms

def PutOrMergeTestSource(*args, **kwargs):
  mod = cms.Source('PutOrMergeTestSource')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
