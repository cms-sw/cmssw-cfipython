import FWCore.ParameterSet.Config as cms

def CSCFileReader(*args, **kwargs):
  mod = cms.EDProducer('CSCFileReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
