import FWCore.ParameterSet.Config as cms

def MiniAODTaggerHarvester(*args, **kwargs):
  mod = cms.EDProducer('MiniAODTaggerHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
