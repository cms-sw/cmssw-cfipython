import FWCore.ParameterSet.Config as cms

def PutOrMergeTestSource(**kwargs):
  mod = cms.Source('PutOrMergeTestSource')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
