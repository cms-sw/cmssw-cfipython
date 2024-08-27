import FWCore.ParameterSet.Config as cms

def NjettinessAdder(**kwargs):
  mod = cms.EDProducer('NjettinessAdder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
