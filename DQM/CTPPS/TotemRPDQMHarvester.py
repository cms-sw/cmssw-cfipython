import FWCore.ParameterSet.Config as cms

def TotemRPDQMHarvester(**kwargs):
  mod = cms.EDProducer('TotemRPDQMHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
