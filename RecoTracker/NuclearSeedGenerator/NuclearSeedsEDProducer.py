import FWCore.ParameterSet.Config as cms

def NuclearSeedsEDProducer(*args, **kwargs):
  mod = cms.EDProducer('NuclearSeedsEDProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
