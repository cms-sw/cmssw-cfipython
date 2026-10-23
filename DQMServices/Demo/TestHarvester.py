import FWCore.ParameterSet.Config as cms

def TestHarvester(*args, **kwargs):
  mod = cms.EDProducer('TestHarvester',
    folder = cms.string('Harvesting/'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
