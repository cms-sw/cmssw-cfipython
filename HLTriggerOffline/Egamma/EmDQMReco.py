import FWCore.ParameterSet.Config as cms

def EmDQMReco(*args, **kwargs):
  mod = cms.EDProducer('EmDQMReco',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
