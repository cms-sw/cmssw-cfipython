import FWCore.ParameterSet.Config as cms

def CSCDaqInfo(*args, **kwargs):
  mod = cms.EDProducer('CSCDaqInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
