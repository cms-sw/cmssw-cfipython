import FWCore.ParameterSet.Config as cms

def CSCDigiProducer(*args, **kwargs):
  mod = cms.EDProducer('CSCDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
