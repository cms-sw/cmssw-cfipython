import FWCore.ParameterSet.Config as cms

def MiniAODTaggerHarvester(**kwargs):
  mod = cms.EDProducer('MiniAODTaggerHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
