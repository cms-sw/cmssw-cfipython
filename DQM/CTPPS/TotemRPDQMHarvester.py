import FWCore.ParameterSet.Config as cms

def TotemRPDQMHarvester(*args, **kwargs):
  mod = cms.EDProducer('TotemRPDQMHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
