import FWCore.ParameterSet.Config as cms

def OuterTrackerMCHarvester(**kwargs):
  mod = cms.EDProducer('OuterTrackerMCHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
