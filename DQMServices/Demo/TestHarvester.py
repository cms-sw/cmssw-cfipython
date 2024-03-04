import FWCore.ParameterSet.Config as cms

def TestHarvester(**kwargs):
  mod = cms.EDProducer('TestHarvester',
    folder = cms.string('Harvesting/'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
